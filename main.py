import price_analyzer


def main():
    price_checker = price_analyzer.PriceAnalyzer()
    item_grab = price_checker.load_script()

    print(f'{50*","} Prices Found {50*","}')

    for key,value in item_grab.items():
        price_checker.price_analyze(key,value)

    print(f'\n{50*","} Not in Stock {50*","}')

    for key, value in item_grab.items():
        price_checker.no_stock_item(key,value)



if __name__ == '__main__':
    main()
    print(100*',')

