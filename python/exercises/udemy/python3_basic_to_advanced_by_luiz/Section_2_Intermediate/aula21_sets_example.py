# Example of use of sets

letters = set()
while True:
    letter = input('Type: ')
    letters.add(letter.lower())

    if 'l' or 'L' in letter:
        print('Congrats')
        break
    print(letters)