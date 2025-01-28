import os
import requests

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Телеграм токен и ID чата
TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_to_telegram(flats):
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    for flat in flats:
        message = (
            f"<b>Адрес:</b> {flat['address']}\n"
            f"<b>Ссылка:</b> {flat['link']}\n"
            f"<b>Цена:</b> {flat['price']}\n"
            f"<b>Детали:</b> {flat['details']}\n"
            f"<a href='{flat['image_url']}'>Изображение</a>"
        )
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        requests.post(telegram_url, data=payload)
