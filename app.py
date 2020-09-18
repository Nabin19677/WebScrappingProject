from bs4 import BeautifulSoup
import requests
import re
import json

link = "https://www.sastodeal.com/sd-fast/food-essentials/sd-value-pack.html"


result = requests.get(link, headers={
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
})
print(result.status_code)
# print(result.content)

soup = BeautifulSoup(result.text, "lxml")

soup.prettify()
div = soup.find('div', {"id": "amasty-shopby-product-list"})
lis = div.find_all('li')

products = []

for li in lis:
    product = li.find('a', class_="product-item-link")
    price = li.find_all('span', class_="price")
    if(product):
        products.append({
            "name": product.string.replace("\n", ""),
            "price": price[0].string,
            "discountPrice": price[1].string if len(price) > 1 else None
        })


print(products)

with open('sastodealwebdata.json', 'w') as file:
    json.dump(products, file, indent=4)
