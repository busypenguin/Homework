shops = {'Перекрёсток': {'молоко': 60, 'хлеб': 30, 'яйца': 150, 'масло': 80, 'кефир': 75}, 'Пятерочка': {'молоко': 65, 'хлеб': 25, 'яйца': 110, 'масло': 90, 'кефир': 55}, 'Дикси': {'молоко': 50, 'хлеб': 40, 'яйца': 120, 'масло': 60, 'кефир': 95}}
input_shop = input('Введите магазин: ')
# input_shop = 'Перекрёсток'
for shop in shops:
    if input_shop == shop:
        products = shops[input_shop]
        for product, price in products.items():
            # input_product = 'молоко'
            input_product = input(f'Вы выбрали магазин {shop}, введите наименование товара, который вы хотите сравнить: ')
            if input_product == product:
                print(f'В магазине {input_shop} продукт {input_product} стоит {price}')