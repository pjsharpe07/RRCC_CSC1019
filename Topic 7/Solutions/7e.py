input_numbers = [int(x) for x in input('What numbers do you want? ').split(', ') ]
# testing: 55, 45, 150, 75, 31, 44, 144, 36, 60

divis_letter = int(input('What number are you checking for? '))
# testing: 12

final_numbers = [x + 100 for x in input_numbers if x % divis_letter == 0 ]
print(final_numbers)