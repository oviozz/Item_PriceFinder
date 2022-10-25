from abc import abstractmethod
import price_looker
from bs4 import BeautifulSoup
import requests

class PriceGrabber(price_looker.PriceLooker):

    def load_script(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

        self.url = 'https://camelcamelcamel.com/search?sq='
        self.content_get = requests.get(f'{self.url}{self._item_name}', headers=header).content
        self.soup = BeautifulSoup(self.content_get, 'lxml')

        self.final_product_list = {}
        for img, price in zip(self.soup.find_all('img', alt=True), self.soup.find_all('tr', attrs={"class": 'watch_row price0'})):
            title = (img['alt'].replace('| Amazon Product Search', '').strip())
            price = price.text.replace('Amazon Price', '').strip().replace('$','')
            self.final_product_list[price] = title

        return self.final_product_list
