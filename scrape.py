import requests
from bs4 import BeautifulSoup
import smtplib
import shutil
import re

# Followed this great tutorial 
# https://towardsdatascience.com/a-tutorial-on-scraping-images-from-the-web-using-beautifulsoup-206a7633e948


URL = 'https://apod.nasa.gov/apod/ap210214.html'
headers = {
    "User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
image = soup.findAll('img')
p = soup.findAll('p')
# date string is located in date variable
date = str(p[1].getText())
img = image[0]
print("Image: ", img)
# list of months
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


url_base = "https://apod.nasa.gov/apod/"
url_ext = img.attrs['src']
full_url = url_base + url_ext
print("Full URL: ", full_url)

r = requests.get(full_url, stream=True)
print("Today: ", date[1:7]+date[7:16]+date[-8:-6])
print("STATUS: ", r.status_code)
day = date[-8:-6]

if r.status_code == 200:
    for number, month in enumerate(months):
        regex = re.compile(month)
        if regex.search(date):
            print("number is: ", number)
            with open(f'/Users/kirk/Pictures/nasa_apotd/{number+1}_{day}_{date[4:6]}_nasa_pic.jpg', 'w+b') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)