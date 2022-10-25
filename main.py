import price_analyzer

def main():
    price_checker = price_analyzer.PriceAnalyzer()
    item_grab = price_checker.load_script()

    print(f'{50*"="} Prices Found For Less than ${price_checker.item_range()[0]} {50*"="}\n')


    for key,value in item_grab.items():
        price_checker.price_analyze(key, value[0], value[1], value[2])

    if price_checker.item_count_return() == 0:
        print(f'{60 * " "}NO ITEM FOUND')

if __name__ == '__main__':
    main()
    print(f'\n{133*"="}')

