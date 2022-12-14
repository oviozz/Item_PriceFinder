import price_grabber

class PriceAnalyzer(price_grabber.PriceGrabber):

    item_count = 0

    def price_analyze(self, price, title, url, rating, item_count=None):

        if int(float(price.replace('$','').replace(',',''))) <= int(max(self._price_range)):
            print(f'| Product: {title}\n| Price: {price}\n| Product URL: {url}\n| Product Rating: {rating}')
            print(f'{len(url) * "_"}')
            self.item_count += 1


    def item_count_return(self):
        return self.item_count
