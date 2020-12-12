import requests
import threading
from bs4 import BeautifulSoup
#F64 ProductPrice watcher

# This script is free and not indended to harmful website
# Personal use only, set interval check as large as possible otherwise the server kick you out for flooding
# I am not responsible for damage caused by improper use


def spacer():
    print('-'*10)


print('F64 ProductPrice Watcher')
spacer()
print('Introdu URL produs: ')
URL = input()
print('Interval verificare pret (secunde): ')
timer = input()
print('Pret dorit achizitie: ')
priceTo = input()


def checkPrice():
    print('\n'*2)
    print('Urmaresc-> '+URL)
    spacer()
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = []
    title = ''
    results = soup.find(
        'div', {'class': 'vtex-flex-layout-0-x-flexRow--productMain'})
    product_price = results.find_all(
        'span', class_='fstudio-pricing-integration-1-x-currencyContainer--productPagePrices')
    product_title = results.find_all(
        'span', class_='vtex-store-components-3-x-productBrand--productPageProductName')

    for product_price in product_price:
        price.append(product_price.text)
    print('Afisez pret')
    spacer()
    for product_title in product_title:
        title = product_title
    print('Pret precedent: ' + price[0])
    print('Pret curent: ' + price[1])
    if(price[1] <= priceTo):
        print('Este timpul ideal pentru achizitie! -> ' + priceTo)
    threading.Timer(float(timer), checkPrice).start()


checkPrice()
