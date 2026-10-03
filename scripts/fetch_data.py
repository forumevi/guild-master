import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("MINDS_BUILDER_API_KEY")
ALIAS = os.getenv("MIND_ALIAS", "main")

if not API_KEY:
    raise ValueError("API Key not found in .env file!")

BASE_URL_CG = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {
    "ids": "axie-infinity,the-sandbox,gala", # İzleme listemiz
    "vs_currencies": "usd",
    "include_24hr_vol": True,
    "include_market_cap": True
}

try:
    print(f"[INFO] Fetching live data from CoinGecko...")
    cg_response = requests.get(BASE_URL_CG, params=PARAMS)
    cg_response.raise_for_status()
    market_data = cg_response.json()
    
    # Veriyi Mind'ın anlayacağı formata sok
    payload_to_mind = {
        "type": "daily_snapshot",
        "source": "coingecko_live",
        "data": market_data,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z"
    }
    
    headers = {"Content-Type": "application/json", "X-Api-Key": API_KEY}
    body = {"alias": ALIAS, "messageText": json.dumps(payload_to_mind)}
    
    minds_url = "https://api.build.hellominds.ai/v1/messaging/message"
    response = requests.post(minds_url, headers=headers, json=body)
    
    if response.status_code == 200:
        print("[SUCCESS] Live data sent to GuildMaster!")
        print(response.json())
    else:
        print(f"[ERROR] Failed to send to Minds: {response.text}")

except Exception as e:
    print(f"[EXCEPTION] {e}")