import requests
import datetime
from bs4 import BeautifulSoup as bs

url = "https://www.coindesk.com/price/dogecoin"
r = requests.get(url)

soup = bs(r.content, 'html.parser')
price = soup.find('div', {'class' : 'price-large'})
today = str(datetime.datetime.now())

url2 = "https://www.coindesk.com/price/ethereum"
r2 = requests.get(url2)
soup2 = bs(r2.content, 'html.parser')
price2 = soup2.find('div', {'class': 'price-large'})

url3 = "https://www.coindesk.com/price/bitcoin"
r3 = requests.get(url3)
soup3 = bs(r3.content, 'html.parser')
price3 = soup3.find('div', {'class': 'price-large'})

url4 = "https://www.coindesk.com/price/cardano"
r4 = requests.get(url4)
soup4 = bs(r4.content, 'html.parser')
price4 = soup4.find('div', {'class': 'price-large'})
print("Dogecoin price at "+ today+" "+price.text )
print("Ethereum price at "+ today+ " "+price2.text)
print("Bitcoin price at "+ today+ " "+price3.text)
print("Cardano price at "+ today+ " "+price4.text)
