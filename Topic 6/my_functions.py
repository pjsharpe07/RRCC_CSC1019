def my_test_function(string):
    return f'The name of my string is {string}'

print('All functions imported. You should see this when importing the script.')

if __name__ == "__main__":
    print('This is for debugging purposes.')
    print('You will not see this when importing like you do before')
    my_value = my_test_function('TESTING MAIN FUNCTIONALITY')
    print(my_value)