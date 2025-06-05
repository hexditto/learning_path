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
# iterate over all options, to get the keys and values
counter = 0
number_questions = 0
for alternative in questions:
    number_questions += 1
    for keys in alternative:
        if keys == 'Question':
            print(f'{keys}: {alternative[keys]}\n')
        if keys == 'Options':
            print(f'{keys}:')
            options_list = alternative[keys]
            for i in range(len(options_list)): # Iterate over the list to display options 
                print(f'{i}) {options_list[i]}')
                if options_list[i] == alternative['Answer']:
                    answer_index = i # Capture the index of the answer for the user input
        if keys == 'Answer':
            test_answer = int(alternative[keys])
            user_answer = int(input("Choose an option: "))
            if user_answer == answer_index:
                counter += 1
                print("You did it!!!\n")
            else:
                print("Wrong answer.\n")

print(f'Congratulations! You got {counter} of {number_questions} questions right!')