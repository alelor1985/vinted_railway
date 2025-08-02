import asyncio
from telegram import Bot
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.asyncio import AsyncIOScheduler

URL = "https://www.vinted.pl/catalog?search_text=nike%20shoes%20men&price_from=0&currency=PLN&page=1&price_to=100"
TOKEN = "8479013387:AAGBS9yh_Z5N9vhKtM4iFJvtgdfnJywc3wE"
CHAT_ID = "6384587684"
bot = Bot(token=TOKEN)

seen = set()

async def check():
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("a", class_="catalog-item")

    for i in items:
        link = "https://www.vinted.pl" + i.get("href")
        if link not in seen:
            await bot.send_message(chat_id=CHAT_ID, text=link)
            seen.add(link)

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check, 'interval', minutes=30)
    scheduler.start()

    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())

