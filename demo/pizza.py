def make_pizza(size, ingredients, extras=None):
    """
    Print out instructions to the kitchen for making a pizza as ordered
    """
    print('Please make the following pizza:')

    dough_ounces = {'small': 6, 'medium': 8, 'large': 12}
    print(f'This is a {size} pizza: use {dough_ounces[size]} oz of dough')

    print('With the following ingredients:')
    for thing in ingredients:
        print(f'* {thing}')

    if extras:
        print('And add the following extras:')
        for thing in extras:
            print(f'* {thing}')

make_pizza('small', ['pepperoni', 'cheese', 'broccoli'])

make_pizza('small', [
                     'meatballs',
                     'pesto',
                     'spinach'
                    ],
                    extras = [
                                 'pineapple',
                                 'tomatoes'
                                ]
           )
