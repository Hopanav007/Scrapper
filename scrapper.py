import requests
from bs4 import BeautifulSoup

class Cryptoscrapper:
    url = "https://coinmarketcap.com"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, features="lxml")

    table = soup.find("table", attrs={"class" : ["h7vnx2-2", "czTsgW", "cmc-table"]})
    global tr_info
    tr_info = table.tbody.find_all("tr")

    def CryptInfo(cryptoN):
        cryptoN = input("Enter the currency name: ")
        for i in range(50):
            for a in tr_info[i].find_all("td"):
                if tr_info[i].find_all("td") == cryptoN.lower():
                    print(a.text)

info = Cryptoscrapper()

info.CryptInfo()