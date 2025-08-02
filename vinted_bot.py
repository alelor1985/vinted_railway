import requests
from bs4 import BeautifulSoup
from telegram import Bot
import time

# --- CONFIGURAZIONE ---
URL = "https://www.vinted.pl/catalog?search_text=nike+shoes+men&price_from=0&price_to=100"
TOKEN = "8479013387:AAGBS9yh_Z5N9vhKtM4iFJvtgdfnJywc3wE"
CHAT_ID = "6384587684"
bot = Bot(token=TOKEN)

seen = set()

def check():
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("a", class_="catalog-item")
    
    for i in items:
        link = "https://www.vinted.pl" + i.get("href")
        if link not in seen:
            bot.send_message(chat_id=CHAT_ID, text=link)
            seen.add(link)

while True:
    check()
    time.sleep(1800)  # ogni 30 minuti

