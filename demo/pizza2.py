""" write a program which takes a pizza order, and prints out
instructions for the kitchen to follow. """

OPTION_START = {'dough': 33, 'sauces': 49, 'toppings': 65}

def get_ingredients():
    """ this will ultimately retrieve our list of ingredients from
    a database, but in the meantime, it will just return a static
    list of ingredients.  the format should be the same as what
    will come from the DB, so the rest of the program can use its
    output no matter where it comes from. """
    ingredients = {
                   'toppings': [
                                'onions',
                                'pepperoni',
                                'sausage',
                                'spinach',
                                'broccoli',
                                'tomatoes',
                               ],
                   'sauces': [
                              'marinara',
                              'pesto',
                              'spicy',
                             ],
                   'dough': [
                             'gluten free',
                             'normal',
                             'sourdough',
                            ]
                  }
    return ingredients


def print_menu(ingredients):
    """ print out a menu with numbers to make it easy to order, and easy to
    double-check the order makes sense """

    # start with dough, using symbols
    print('Select a dough option (limit 1):')
    for i, option in enumerate(ingredients['dough']):
        symbol = chr(i + OPTION_START['dough']) # this starts with the ! symbol
        print(f'{symbol}: {option}')

    print('Select a sauce option (limit 1):')
    for i, option in enumerate(ingredients['sauces']):
        symbol = chr(i + OPTION_START['sauces']) # this starts with 1
        print(f'{symbol}: {option}')

    print('Select your toppings (no limit):')
    for i, option in enumerate(ingredients['toppings']):
        symbol = chr(i + OPTION_START['toppings']) # this starts with A
        print(f'{symbol}: {option}')

    print('A valid response might look like: !2EFA')


def get_response(ingredients):
    """ prompt the user to input a string representing a pizza.
    double-check that the ingredients make sense (one dough, one sauce,
    zero or more toppings) """
    response = input('Enter your pizza code: ')

    def check_ingredient(ingredient_type, max_i=10, min_i=1):
        # first, check dough
        upper_limit = len(ingredients[ingredient_type])
        code_space = [
                      OPTION_START[ingredient_type],
                      OPTION_START[ingredient_type] + upper_limit
                     ]
        num_items = 0
        for letter in response:
            if ord(letter) >= code_space[0] and ord(letter) <= code_space[1]:
                num_items += 1
        if num_items < min_i or num_items > max_i:
            print(f'Please select *min/max this* {ingredient_type} option')

    check_ingredient('dough', max_i=1)


def print_order():
    pass

def main():
    ingredients = get_ingredients()
    #print_menu(ingredients)
    while True:
        print_menu(ingredients)
        response = get_response(ingredients)
        if response:
            break
    print_order(response)

if __name__ == '__main__':
    main()
