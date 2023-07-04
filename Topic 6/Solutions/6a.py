####### reversing a string #######



def reverse_string(string_name):
    return string_name[::-1]

my_name_reversed = reverse_string('Preston')
print(my_name_reversed)


### challenge with lower or not

def reverse_string_lower(string_name, lower):
    if lower:
        return string_name[::-1].lower()
    else:
        return string_name[::-1]

my_name_reversed = reverse_string_lower('PRESTON', True)
print(my_name_reversed)

my_name_reversed = reverse_string_lower('Preston', False)
print(my_name_reversed)
