def swap_case(input_string):
    # what we will finally return
    final_value = ''
    for letter in input_string:
        
        # confirm if upper case
        if letter.isupper():
            final_value += letter.lower()
        else:
            final_value += letter.upper()

    return final_value


test_case_one = swap_case('HeLLo')
print(test_case_one)

test_case_two = swap_case('ALL UPPER')
print(test_case_two)

