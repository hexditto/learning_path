# Exercise - question/answer system

questions = [
    {
        'Question': 'Whats the value of 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'Whats the value of 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'Whats the value of 10/2',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

number_answers = 0

for question in questions:
    print('Question:', question['Question'])
    print()

    options = question['Options']
    for i, option in enumerate(options):
        print(f'{i}) {option}')
    print()

    got_it = False
    choice = input("Choose an option: ")
    choice_int = None
    size_options = len(options)
    if choice.isdigit():
        choice_int = int(choice)
    
    if choice_int is not None:
        if choice_int >= 0 and choice_int < size_options:
            if options[choice_int] == question['Answer']:
                got_it = True
    
    print()
    if got_it:
        number_answers += 1
        print('Congrats!')
    else:
        print("Wrong answer.")
    print() 
    
print('You got it', number_answers)
print('of', len(questions), 'questions.')
