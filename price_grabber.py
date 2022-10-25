import price_looker
from bs4 import BeautifulSoup
import requests

class PriceGrabber(price_looker.PriceLooker):

    def load_script(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip',
            'DNT': '1',  # Do Not Track Request Header
            'Connection': 'close'
        }

        self.url = 'https://www.amazon.com/s?k='
        self.content_get = requests.get(f'{self.url}{self._item_name}', headers=header).content
        self.soup = BeautifulSoup(self.content_get, 'lxml')


        self.final_product_list = {}

        self.item = self.soup.find_all("div",{"data-component-type" : "s-search-result"})  # items

        for item in self.item:
            tag_finder = item.h2.a

            try:
                url = 'https://www.amazon.com/' + tag_finder.get('href')
                item_title = tag_finder.text.strip()
                price = item.find('span', 'a-price').find('span', 'a-offscreen').text
                item_rating = item.i.text

                self.final_product_list[price] = [item_title, url, item_rating]

            except AttributeError:
                continue


        return {price: title for price, title in sorted(self.final_product_list.items(), key=lambda item: item[1][2], reverse=True)}


