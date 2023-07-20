baseball_teams = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}


############### initial setup ###########

# print(baseball_teams)
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 
# 'Minnesota': 'Twins', 'Milwaukee': 'Brewers',
#  'Seattle': 'Mariners'}

##### accessing kv pairs ###########

# print(baseball_teams['Colorado']) # Rockies
# print(baseball_teams['Seattle']) # Mariners
# print(baseball_teams['Kansas City']) # error

############## adding kv pairs ########

# baseball_teams['Kansas City'] = 'Royals'
# print(baseball_teams)
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 
#  'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 
#  'Seattle': 'Mariners', 'Kansas City': 'Royals'}

############## modify existing kv pair ########

# baseball_teams['Minnesota'] = 'New Twin Name'
# print(baseball_teams)
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 
# 'Minnesota': 'New Twin Name', 'Milwaukee': 'Brewers', 
# 'Seattle': 'Mariners', 'Kansas City': 'Royals'}

############# removing kv pair ########
# del baseball_teams['Milwaukee']
# print(baseball_teams)
#  {'Colorado': 'Rockies', 'Boston': 'Red Sox', 
# 'Minnesota': 'Twins', 'Seattle': 'Mariners'}


######### only integers ##########

# some_fake_values = {
#     0 : 1,
#     7 : 4,
#     6 : 8
# }

# print(some_fake_values[7]) # 4

### mixing up the types ###

# testing = {42: 'aaa', 
#            2.78: 'bbb', 
#            True: 123,
#            'my_list' : ['abc', 123, 456]
#            }

# print(testing[42]) # aaa
# print(testing[True]) # 123
# print(testing['my_list']) # ['abc', 123, 456]

######## you can get the len of dictionaries too
baseball_teams = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}
# print(len(baseball_teams)) # 5
# # now add an element
# baseball_teams['Kansas City'] = 'Royals'
# print(len(baseball_teams)) # 6

# # modify an element
# baseball_teams['Colorado'] = 'Nuggets'
# print(len(baseball_teams)) # 6

##### viewing some of the list values in action #############

# baseball_teams = {
#     'Colorado' : 'Rockies',
#     'Boston'   : 'Red Sox',
#     'Minnesota': 'Twins',
#     'Milwaukee': 'Brewers',
#     'Seattle'  : 'Mariners'
# }

# co_team = baseball_teams.get('Colorado')
# print(co_team) # Rockies

# kc_team = baseball_teams.get('Kansas City')
# print(kc_team) # none

# # wipe them all out
# baseball_teams.clear()
# print(baseball_teams) # {}


########## dynamically fetching values #############

baseball_teams = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}

# everything = baseball_teams.items()
# print(everything)
# dict_items([('Colorado', 'Rockies'), ('Boston', 'Red Sox'), ('Minnesota', 'Twins'), ('Milwaukee', 'Brewers'), ('Seattle', 'Mariners')])

# for item in everything:
#     print(item)
#     print(item[0]) # this is the key
#     print(item[1]) # this is the value

print(baseball_teams.keys())
# dict_keys(['Colorado', 'Boston', 'Minnesota', 'Milwaukee', 'Seattle'])
for key in baseball_teams.keys():
    print(key)

print(baseball_teams.values())
# dict_values(['Rockies', 'Red Sox', 'Twins', 'Brewers', 'Mariners'])
for value in baseball_teams.keys():
    print(value)
