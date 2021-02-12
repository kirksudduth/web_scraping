import requests
from bs4 import BeautifulSoup
import smtplib
import shutil


URL = 'https://apod.nasa.gov/apod/astropix.html'
headers = {
    "User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
image = soup.findAll('img')
img = image[0]

url_base = URL
url_ext = img.attrs['src']
full_url = url_base + url_ext

r = requests.get(full_url, stream=True)

if r.status_code == 200:
    with open("Pictures/nasa_apotd/SCRAPED.jpg", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)