import os
import json
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

MESSAGES_FILE = "messages.json"

def send_message(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    r = requests.post(url, json=payload, timeout=10)
    r.raise_for_status()

def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
        messages = json.load(f)

    if today in messages:
        send_message(messages[today])

if __name__ == "__main__":
    main()
