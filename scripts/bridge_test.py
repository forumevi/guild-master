import requests
import json
import os
from dotenv import load_dotenv

# .env dosyasındaki anahtarı yükle
load_dotenv()
API_KEY = os.getenv("MINDS_BUILDER_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found in .env file!")

BASE_URL = "https://api.build.hellominds.ai/v1/messaging/message"

# Simüle edilmiş CoinGecko verisi (Jüriye sunacağımız gerçek senaryo)
mock_economic_data = {
    "type": "economic_alert",
    "token": "AXS",
    "signal": "volume_drop_warning",
    "details": "7 günlük ortalamaya göre hacim %45 düştü.",
    "timestamp": "2026-10-04T10:00:00Z"
}

headers = {
    "Content-Type": "application/json",
    "X-Api-Key": API_KEY
}

payload = {
    "alias": "main", # Az önce oluşturduğumuz alias
    "messageText": json.dumps(mock_economic_data) # Veriyi string'e çeviriyoruz
}

try:
    print(f"[INFO] Sending data to Mind via Builder API...")
    response = requests.post(BASE_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("[SUCCESS] Message sent!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"[ERROR] Status Code: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"[EXCEPTION] {e}")