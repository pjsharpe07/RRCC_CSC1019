def is_even(number):

    # challenge - handling if not an integer:
    try:
        convert_number = int(number)
    except:
        return f'Sorry, {number} is not a number'

    return number % 2 == 0


fourteen = is_even(14)
eighty_three = is_even(83)
tacos = is_even('tacos')

print(fourteen)
print(eighty_three)
print(tacos)