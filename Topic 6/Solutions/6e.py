def update_list(lst, idx, value):
    
    # if the index is not in the list
    try:
        og_value = lst[idx]
    except:
        accepted_idx = [str(x) for x in range(len(lst))]
        print(f'Sorry, {idx} is not in the list')
        print(f'Acceptable indexes are {", ".join(accepted_idx)}')
        return None
    
    # now update the list for everything else
    lst[idx] = value
    return lst


my_list = [
    'Suzie',
    'gato',
    22,
    1000.02
]

# failed_example = update_list(my_list, 100, 'This should fail anyway')

# update_one = update_list(my_list, 0, 'Rebecca')
# print(update_one)

update_two = update_list(my_list, 2, my_list[2] * 2)
print(update_two)