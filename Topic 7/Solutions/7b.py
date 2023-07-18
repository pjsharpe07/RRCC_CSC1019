input_names = input('What names do you want checked? ').split()
input_letter = input('What letter are you checking? ')


for name in input_names:
    if name[0].lower() == input_letter.lower():
        print(name)