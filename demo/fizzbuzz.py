# print out 1 2 fizz 4 buzz, etc.

number = 1

while True:
    if number % 3 == 0:
        print('Fizz', end='')
    if number % 5 == 0:
        print('Buzz', end='')
        continue
    print(number)
    print('\n')
    number += 1
