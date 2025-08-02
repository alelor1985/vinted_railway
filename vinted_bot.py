import requests
from bs4 import BeautifulSoup
from telegram import Bot
import time

URL = "https://www.vinted.pl/men/obuwie?price_to=100"
TOKEN = "8479013387:AAGBS9yh_Z5N9vhKtM4iFJvtgdfnJywc3wE"
CHAT_ID = "6384587684"
bot = Bot(token=TOKEN)

seen = set()

def check():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('a', href=True)

    for item in items:
        href = item['href']
        if "/items/" in href:
            full_link = "https://www.vinted.pl" + href
            if full_link not in seen:
                bot.send_message(chat_id=CHAT_ID, text=full_link)
                seen.add(full_link)

while True:
    try:
        check()
        time.sleep(1800)  # ogni 30 minuti
    except Exception as e:
        print("Errore:", e)
        time.sleep(60)
