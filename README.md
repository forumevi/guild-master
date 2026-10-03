# Guild Master: Autonomous GameFi Community Intelligence

**Author:** Tamer Kaleander  
**Contact:** [Email] | [Telegram Handle]  
**Platform:** HelloMinds by Animoca Brands  

## 🚀 Overview
Guild Master is a persistent AI agent that monitors GameFi community health and economic signals. It combines a custom Python data bridge (fetching live metrics from CoinGecko via Builder API) with a specialized 'Weekly Economy Digest' Skill on the Minds platform.

Unlike generic bots, it respects the platform's Circle security model by delivering sensitive analytical reports exclusively to authorized stewards via DM/email, preventing community panic (FUD).

## 🛠️ Architecture
1. **Data Layer (Python):** Fetches real-time token prices/volumes from CoinGecko.
2. **Bridge Layer (Builder API):** Sends structured JSON payloads to the Mind.
3. **Intelligence Layer (HelloMinds):** 
   - Persistent Memory: Tracks player sentiment over time.
   - Circle Security: Ensures only verified stakeholders receive warnings.
   - Skill Engine: Executes the "Weekly Economy Digest" playbook.

## 🧪 Verification & Evidence
We do not claim predictions; we provide measured insights.
- **Cost Analysis:** Measured ~38 Cognition Credits for initial setup/testing phase (90% LLM reasoning, <5% Web Search).
- **Live Data Test:** Successfully integrated AXS/SAND/GALA market data into Agent context. See `scripts/fetch_data.py`.
- **Security Model:** Verified Telegram group read-access via Admin privileges while maintaining private reporting channels.

## 📂 Project Structure
```text
├── scripts/
│   ├── bridge_test.py    # Initial API connectivity test
│   └── fetch_data.py     # Live CoinGecko data puller
├── docs/
│   └── cost_analysis.txt # Raw usage logs
├── .env.example          # Template for API keys (NO KEYS COMMITTED)
└── README.md             # This file