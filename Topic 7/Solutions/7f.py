diction = {
    'Start' : 'First Word',
    'Hello' : 'Moto',
    47 : 55,
    'Denver' : ['Rockies', 'Nuggets', 'Broncos']
}

key = input('Key: ')
value = input('Value: ')

diction.update({key : value})
print(diction)
