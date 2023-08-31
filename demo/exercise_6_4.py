pizza1 = {'size': 'medium',
          'toppings': ['onions', 'mushrooms', 'sausage']}
pizza2 = {
          'size': 'large',
          'toppings': ['pepperoni', 'pepperoni', 'pepperoni']
         }
pizza3 = {
          'size': 'small',
          'toppings': [
                       'peppers',
                       'avocado',
                       'tomatoes'
                      ]
         }

orders = [pizza1, pizza2, pizza3]

for order in orders:
    size = order['size']
    toppings = ', '.join(order['toppings'])
    print(f'Make a {size} pizza with the following toppings: {toppings}')

