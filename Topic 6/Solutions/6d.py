def hide_numbers(num, hidden_character):
    input_num = str(num)
    hidden_characters = ''
    first_digits = input_num[:-4]
    last_four = input_num[-4:]


    for letter in first_digits: # we want up to the last four digits
        hidden_characters += hidden_character


    return hidden_characters + last_four


first_example = hide_numbers(8675309, 'x')
second_example = hide_numbers(8753314581, '*')

print(first_example)
print(second_example)