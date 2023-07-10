

# professional meteor input list
prof_preds = []

for i in range(5):
    next_pred = input(f'Enter prediction. You have {5 - i} prediction(s) to go: ')
    prof_preds.append(float(next_pred))

# calculate the average
average = sum(prof_preds) / 5

# get the upper and lower bound
upper_bound = average * 1.2
lower_bound = average * 0.8

armchair_preds = input('What is your prediction? ')

while armchair_preds != 'done':

    armchair_preds = float(armchair_preds) # need to convert to float
    if armchair_preds >= lower_bound and armchair_preds <= upper_bound: # check if within bounds
        print(f'Your prediction of {armchair_preds} seems like a valid prediction')
    else:
        print(f'Your prediction of {armchair_preds} is too far off from the professional average of {average}')

    armchair_preds = input('What is your next prediction? ')
    
# exit when done
else:
    print('Have a nice day!')
