import requests
from bs4 import BeautifulSoup

class Dolaru:
    def __init__(self):
        soup = BeautifulSoup(requests.get("https://bank.gov.ua/ua/markets/exchangerates").content, "html.parser")
        for row in soup.find_all("tr"):
            if "Долар США" in row.text:
                self.rate = float(row.find_all("td")[-1].text.replace(',', '.'))
                break

conv = Dolaru()
tuk = float(input("Введіть суму в гривнях: "))
print(f"Результат: {tuk / conv.rate:.2f} $")