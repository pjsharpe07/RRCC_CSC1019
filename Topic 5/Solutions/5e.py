#### a VERY simple system that will 'cut' veggies until there is none left ####



pounds_left = int(input('How many pounds of vegetables do you want to cut? '))

hours_worked = 0

while pounds_left > 0:
    # make sure there are not too many veggies being sent
    # not needed -- but fun.
    if pounds_left >= 100:
        pounds_left = int(input(f'{pounds_left} is too many vegetables. Try a smaller number?'))
    else:
        print('Beginning to cut some veggies!')
        pounds_left -= 10
        hours_worked += 1
        print(f'Finished with cutting. There are now {pounds_left}lbs remaining\n')
else:
    print(f'Finished slicing all of the veggies in {hours_worked} hours')