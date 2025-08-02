from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from telegram import Bot
import time

URL = "https://www.vinted.pl/catalog?search_text=nike%20shoes%20men&price_from=0&currency=PLN&page=1&price_to=100"
TOKEN = "8479013387:AAGBS9yh_Z5N9vhKtM4iFJvtgdfnJywc3wE"
CHAT_ID = "6384587684"
bot = Bot(token=TOKEN)

seen = set()

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

def check():
    driver.get(URL)
    time.sleep(5)
    links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/items/"]')
    for link in links:
        href = link.get_attribute("href")
        if href not in seen:
            bot.send_message(chat_id=CHAT_ID, text=href)
            seen.add(href)

while True:
    try:
        check()
        time.sleep(60)  # Ogni minuto
    except Exception as e:
        print(f"Errore: {e}")
        time.sleep(60)

