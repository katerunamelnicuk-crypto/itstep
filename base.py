import sqlite3, requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://sinoptik.ua/погода-львів"
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
temp = soup.find("p", class_="R1ENpvZz").text

db = sqlite3.connect('lviv_weather.db')
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS weather (dt TEXT, temp TEXT)")
now = datetime.now().strftime("%H:%M")
cursor.execute("INSERT INTO weather VALUES (?, ?)", (now, temp))

db.commit()
db.close()

print(f"Час: {now};")
print(f"Температура: {temp}")