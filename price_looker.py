
class PriceLooker:
    def __init__(self):
        self._item_name = input('What item are you looking for: ')
        self._price_range = input('Price Range (Ex: $10-$100): ').replace('$','').split('-')

