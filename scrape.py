import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://apod.nasa.gov/apod/astropix.html'
headers = {
    "User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
image = soup.findAll('img')
img = image[0]

print(img.attrs['src'])
