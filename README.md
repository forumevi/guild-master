# Guild Master: Persistent GameFi Community Intelligence

**Author:** Tamer Kalender  
**Contact:** forumevi@msn.com | @tamerk2 (Telegram)  
**Platform:** HelloMinds by Animoca Brands  

## 🚀 Overview
Guild Master is a persistent AI analyst designed for GameFi studios. It monitors community traffic, correlates it with live market data via a deterministic Python bridge, and delivers private, actionable reports exclusively to authorized stewards. 

*Note: This project is currently in internal alpha testing with controlled accounts to validate core mechanics before public deployment.*

## 🛠️ Architecture
1. **Data Layer (Python):** Fetches 8-day market charts from CoinGecko and computes deterministic warning flags (e.g., volume drop >30%, price drop >15%) locally. This minimizes LLM compute costs and ensures predictable behavior.
2. **Bridge Layer (Builder API):** Sends structured, pre-analyzed JSON payloads to the Mind via `POST /v1/messaging/message`.
3. **Intelligence Layer (HelloMinds):** 
   - Utilizes persistent memory to track evolving player sentiment over time.
   - Respects Circle access controls to ensure sensitive financial reports are not broadcast publicly, preventing community FUD.

## 🧪 Verification & Evidence
We focus on measurable, verifiable execution:
- **CLI & API Connectivity:** Verified via `minds doctor --pretty`.
- **Live Data Bridge:** Python script successfully pulls AXS/SAND/GALA prices, computes local signals, and pushes JSON to the Mind. 
- **Cost Efficiency:** Measured ~38 Cognition Credits for the initial setup and testing phase. Optimization confirmed: the majority of credits are spent on LLM reasoning, while web search/compute is minimized via the Python bridge.
- **Security Validation:** Confirmed that the bot can read group messages when granted Admin privileges (as per platform documentation for group bots), while maintaining strict private reporting channels to the Steward.

## 📂 Project Structure
```text
├── .github/workflows/
│   └── daily-data.yml      # GitHub Action for scheduled data fetching
├── scripts/
│   ├── bridge_test.py      # Initial API connectivity and payload test
│   └── fetch_data.py       # Deterministic CoinGecko data puller and signal generator
├── .env.example            # Template for API keys (NO KEYS COMMITTED)
├── .gitignore              # Ensures .env and local files are not tracked
└── README.md               # This file

🔗 Links
HelloMinds Profile: hellominds.ai/profile/minds/69b28b3e-f36b-1410-8467-00039ce7df11
GitHub Repository: github.com/forumevi/guild-master