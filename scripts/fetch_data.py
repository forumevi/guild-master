"""
Guild Master data bridge.
Fetches 8 days of daily price/volume from CoinGecko, computes simple warning
signals in plain Python (deterministic, no LLM), then sends the result to the
Mind through the Builder API.
"""
import os
import sys
import time
import json
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MINDS_BUILDER_API_KEY")
ALIAS = os.getenv("MIND_ALIAS", "main")

if not API_KEY:
    sys.exit("ERROR: MINDS_BUILDER_API_KEY is not set in .env")

COINS = {"AXS": "axie-infinity", "SAND": "the-sandbox", "GALA": "gala"}
VOLUME_DROP_PCT = -30   # Flag if latest volume is 30%+ below previous 7-day average
PRICE_DROP_PCT = -15    # Flag if price fell 15%+ over the 8-day window
MINDS_URL = "https://api.build.hellominds.ai/v1/messaging/message"

def pct(new, old):
    return round((new - old) / old * 100, 1) if old else None

def analyse(symbol, coin_id):
    try:
        r = requests.get(
            f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart",
            params={"vs_currency": "usd", "days": 8, "interval": "daily"},
            timeout=30,
        )
        r.raise_for_status()
        data = r.json()
        
        prices = [p[1] for p in data.get("prices", [])]
        vols = [v[1] for v in data.get("total_volumes", [])]

        if len(prices) < 2 or len(vols) < 2:
            return {"symbol": symbol, "error": "Insufficient data"}

        # Calculate metrics
        volume_change = pct(vols[-1], sum(vols[:-1]) / len(vols[:-1]))
        price_change = pct(prices[-1], prices[0])

        flags = []
        if volume_change is not None and volume_change <= VOLUME_DROP_PCT:
            flags.append("volume_drop_warning")
        if price_change is not None and price_change <= PRICE_DROP_PCT:
            flags.append("price_drop_warning")

        return {
            "symbol": symbol,
            "price_usd": round(prices[-1], 6),
            "volume_vs_prev_avg_pct": volume_change,
            "price_change_window_pct": price_change,
            "flags": flags,
        }
    except Exception as e:
        return {"symbol": symbol, "error": str(e)}

def main():
    results = []
    for symbol, coin_id in COINS.items():
        results.append(analyse(symbol, coin_id))
        time.sleep(2)  # Stay under CoinGecko's public rate limit

    payload = {
        "type": "daily_signals",
        "source": "coingecko_market_chart",
        "computed_by": "python_rules_engine",
        "thresholds": {"volume_drop_pct": VOLUME_DROP_PCT, "price_drop_pct": PRICE_DROP_PCT},
        "tokens": results,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }

    resp = requests.post(
        MINDS_URL,
        headers={"Content-Type": "application/json", "X-Api-Key": API_KEY},
        json={"alias": ALIAS, "messageText": json.dumps(payload)},
        timeout=60,
    )
    
    # Safe logging: Do not print response body in public Actions logs
    print(f"[INFO] Minds API status: {resp.status_code}")
    if resp.status_code != 200:
        print(f"[ERROR] Response: {resp.text}")
        sys.exit(1)
    else:
        print("[SUCCESS] Deterministic signals sent to GuildMaster.")

if __name__ == "__main__":
    main()