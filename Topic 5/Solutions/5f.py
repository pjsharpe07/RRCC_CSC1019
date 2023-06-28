### get the number of games with > 15 points ###

over_fifteen = 0

for i in range(10):
    points_scored = int(input(f'How many points were scored in the game {i + 1}? '))
    
    if points_scored >= 15:
        over_fifteen += 1
        print(f'Another fifteen pointer. Total games > 15 is now: {over_fifteen}')
    # for readability in output
    print()
# break and output total
else:
    print(f'Total Games over 15: {over_fifteen}')