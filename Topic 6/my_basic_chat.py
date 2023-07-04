''' this will do a few things:
1. say hello
2. add two numbers
3. tell you if a number is even
4. Exit the program
'''

# 1. say hello
def say_hello(input):
    print(f'Hello {input}')

# 2. add two numbers
def add_two(num_one, num_two):
    print(f'Adding {num_one} and {num_two} sums to {num_one + num_two}')

# 3 is_even
def is_even(input):
    if input % 2 == 0:
        print(f'{input} is an even number')
    else:
        print(f'{input} is not an even number')

# fetching and returning user input
def get_user_input():
    return input('Which option would you like? ')

# default display options
def display_menu():
    print('''
    Please select from one of the options. 
    1. Say hello
    2. Add two numbers
    3. See if a number is even
    4. Exit program.
    ''')


def start_chat():
    # always display the menu and fetch user input
    display_menu()
    user_input = get_user_input()

    # basic error handling if not a valid options
    if user_input not in ('1','2','3','4'):
        print(f'Sorry, but {user_input} is not a valid option')
        start_chat()
    # iterate through and call each of our menu options
    # each will restart the chat except for the 'Exit' option
    elif user_input == '1':
        name = input('Who should I say hello to? ')
        say_hello(name)
        start_chat()
    elif user_input == '2':
        num_one = int(input('What is the first number? '))
        num_two = int(input('What is the second number? '))
        add_two(num_one, num_two)
        start_chat()
    elif user_input == '3':
        number = int(input('Which number would you like me to confirm is even or not? '))
        is_even(number)
        start_chat()
    elif user_input == '4':
        print('Have a wonderful day!')


# invoke the function to begin running our chatbot program
start_chat()