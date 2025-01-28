import os

from sqlite_client import save_flat, setup_database, is_flat_new
from telegram_utils import send_to_telegram
from parser import parse_flats

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

url = os.getenv("URL") 

conn = setup_database()


while True:
    all_flats = parse_flats(url)
    new_flats = []

    for flat in all_flats:
        if is_flat_new(conn, flat['link']):
            save_flat(conn, flat)
            new_flats.append(flat)

    if new_flats:
        send_to_telegram(new_flats)
    else:
        print("Нет новых квартир для отправки.")

conn.close()

