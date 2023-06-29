### checks if input is in the 'acceptable' musical genres

genre_input = input('What genre do you want information about? ')

# fix the casing here - but persist the original input
genre_lower = genre_input.lower()

# these are the genres that we want to confirm exist or not
acceptable_genres = [
    'rock', 
    'pop',
    'classical',
    'jazz',
    'lofi',
    'metal',
    'hip-hop',
    'rap', 
    'blues', 
    'r&b'
]

if genre_lower in acceptable_genres:
    print('Processing data for', genre_input)
else:
    print(f'Sorry, I do not have any information about {genre_input}. Try another genre')