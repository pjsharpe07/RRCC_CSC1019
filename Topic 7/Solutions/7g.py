sample_dictionary = {
    'Rapids' : 33,
    'LAFC' : 45,
    'Cinci' : 58,
    'Philly' : 44,
    'Charlotte' : 20   
}

# one line sort
sorted_values = sorted(sample_dictionary.items(), key=lambda x : x[1])
# [('Charlotte', 20), ('Rapids', 33), ('Philly', 44), ('LAFC', 45), ('Cinci', 58)]

worst_team = sorted_values[0]
best_team = sorted_values[-1]

print(f'{worst_team[0]} has the lowest points with {worst_team[1]}')
print(f'{best_team[0]} has the most points with {best_team[1]}')