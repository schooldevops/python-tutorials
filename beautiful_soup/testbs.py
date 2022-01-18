import requests as req 
from bs4 import BeautifulSoup
import csv

page = req.get('https://www.costco.co.kr/my-account/orders')
# print(page.encoding)
page.encoding = 'utf-8'

print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all("li", {"class": "order-history__list-item"})
print(data)

