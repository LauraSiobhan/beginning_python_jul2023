""" write a program which takes a pizza order, and prints out
instructions for the kitchen to follow. """

# this global variable contains the unicode codes for the start of the symbols
# that will be used for choosing the different categories of ingredient
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
    """ print out a menu with numbers """

    for i, option in enumerate(ingredients):
        print(f'{i+1}: {option}')


def get_response(ingredients):
    response = int(input('What is your choice? '))
    max_num = len(ingredients)
    if response > 0 and response <= max_num:
        return response

def print_order(response, ingredients):
    print('Dear kitchen, please make the following pizza:')
    for item in ingredients:
        ingredient_num = response[item] - 1
        print(f'{item}: {ingredients[item][ingredient_num]}')

def main():
    ingredients = get_ingredients()
    #print_menu(ingredients)
    kitchen_response = {}
    for item in ingredients:
        while True:
            print(f'Select your {item}')
            print_menu(ingredients[item])
            response = get_response(ingredients[item])
            if response:
                break
        kitchen_response[item] = response
    print_order(kitchen_response, ingredients)

if __name__ == '__main__':
    main()
