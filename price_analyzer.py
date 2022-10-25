import price_grabber

class PriceAnalyzer(price_grabber.PriceGrabber):

    def price_analyze(self, price, title, url):

        self.item_count = 0

        if int(float(price.replace('$','').replace(',',''))) <= int(max(self._price_range)):
            print(f'| Product: {title}\n| Price: {price}\n| Product URL: {url}')
            print(f'{len(url) * "_"}')
            self.item_count += 1


    def item_count_return(self):
        return self.item_count
