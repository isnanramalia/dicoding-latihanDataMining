# mencoba library beautifulsoup4
# apa itu beautifulsoup? beautifulsoup adalah library python yang digunakan untuk melakukan web scraping, yaitu mengambil data dari website lain. dengan menggunakan beautifulsoup, kita dapat mengambil dan memanipulasi data dari website lain.

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print(soup.title)
