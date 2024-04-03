def determine_length(input_var):
    # the value to return
    num_items = 0

    # we don't really use the 'item' variable here -- do not need it
    for item in input_var:
        num_items += 1
    
    return num_items

print(determine_length(input_var=[]))
print(determine_length(input_var=""))

print(determine_length(input_var=["item_one", "item_two", 3]))
print(determine_length(input_var="How many letters"))
