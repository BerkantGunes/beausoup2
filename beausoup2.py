# n11 dan datalar cekeriz.
import requests
from bs4 import BeautifulSoup # bu html yapisini Soup yapisina dondurmek icin beautifiul soup metodunu kullaniyoruz!
url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li",{"class":"column"}, limit=1)

print(list)