import requests
from bs4 import BeautifulSoup
import smtplib
import shutil

# Followed this great tutorial 
# https://towardsdatascience.com/a-tutorial-on-scraping-images-from-the-web-using-beautifulsoup-206a7633e948


URL = 'https://apod.nasa.gov/apod/'
headers = {
    "User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
image = soup.findAll('img')
p = soup.findAll('p')
date = str(p[1].getText())
img = image[0]

url_base = URL
url_ext = img.attrs['src']
full_url = url_base + url_ext

r = requests.get(full_url, stream=True)
print("Today: ", date[1:6])

if r.status_code == 200:
    with open("/Users/kirk/Pictures/nasa_apotd/SCRAPED.jpg", 'w+b') as f:
        print("F: ", f)
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)