import sqlite3, requests
from bs4 import BeautifulSoup

class Saitiki:
    def __init__(self):
        self.db = sqlite3.connect("search.db")
        self.db.execute("CREATE TABLE IF NOT EXISTS sites (url TEXT UNIQUE)")

    def manage_db(self, url=None, clear=False):
        if clear: self.db.execute("DELETE FROM sites")
        elif url:
            try: self.db.execute("INSERT INTO sites VALUES (?)", (url,))
            except: print("Вже є, пиши інший")
        self.db.commit()

    def get_rank(self, url, word):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            res = requests.get(url, timeout=5, headers=headers)
            text = BeautifulSoup(res.text, 'html.parser').get_text().lower()
            return text.count(word.lower())
        except: return 0

    def run(self):
        while True:
            cmd = input("\n1:Додати 2:Пошук 3:Очистити 0:Вихід > ")
            if cmd == '1':
                self.manage_db(url=input("URL: "))
            elif cmd == '2':
                word = input("Слово: ")
                urls = [r[0] for r in self.db.execute("SELECT url FROM sites")]
                results = sorted([(u, self.get_rank(u, word)) for u in urls], key=lambda x: x[1], reverse=True)
                for u, c in results: print(f"[{c}] {u}")
            elif cmd == '3':
                self.manage_db(clear=True)
            elif cmd == '0': break

if __name__ == "__main__":
    Saitiki().run()

