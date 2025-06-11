# Packing and unpacking in dictionaries:
a, b = 1, 2
a, b = b, a
# print(a, b)

person = {
    'name': 'Aline',
    'last_name': 'Souza',
}

data_person = {
    'idade': 16,
    'altura': 1.6,
}

complete_person = {**person, **data_person} #Unpacking in another dictionary

# print(complete_person)
# args and kwargs
# kwargs - keyword arguments
def show_named_arguments(*args, **kwargs):
    print('Non-named arguments:', args)

    for k, v in kwargs.items():
        print(k, v)

# show_named_arguments(1, 2, name = 'Joana', qLq=123)
# show_named_arguments(**complete_person)

config = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
show_named_arguments(**config)