import requests
from bs4 import BeautifulSoup
import smtplib
import shutil
import re

# Followed this great tutorial 
# https://towardsdatascience.com/a-tutorial-on-scraping-images-from-the-web-using-beautifulsoup-206a7633e948


URL = "https://apod.nasa.gov/apod/"
headers = {
    "User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
image = soup.findAll('img')
if image == []:
    print("No image today. It's a video.")
else:
    p = soup.findAll('p')
    # date string is located in date variable
    date = str(p[1].getText())
    split_date = date.split()
    img = image[0]
    # list of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    url_ext = img.attrs['src']
    full_url = URL + url_ext

    r = requests.get(full_url, stream=True)
    day = split_date[2]
    year = split_date[0][-2:]


    if r.status_code == 200:
        for number, month in enumerate(months, start=1):
            regex = re.compile(month)
            if regex.search(date):
                with open(f'/Users/kirk/Pictures/nasa_apotd/{number}_{day}_{year}_nasa_pic.jpg', 'w+b') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

 