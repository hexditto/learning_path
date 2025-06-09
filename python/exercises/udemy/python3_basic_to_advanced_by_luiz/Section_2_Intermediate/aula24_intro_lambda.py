"""
Lambda Function in Python
- Anonymous function that has only one line
- Everything must be converted in one expression
"""

# array = [4, 32, 1, 34, 5, 6, 6, 21]
# array.sort()
# print(array)

array = [
    {'name': 'Luiz', 'last_name': 'Miranda'},
    {'name': 'Maria', 'last_name': 'Oliveria'},
    {'name': 'Daniel', 'last_name': 'Silva'},
    {'name': 'Eduardo', 'last_name': 'Moreira'},
    {'name': 'Aline', 'last_name': 'Souza'}
]

def show(array):
    for item in array:
        print(item)
    print()


l1 = sorted(array, key=lambda item: item['name'])
l2 = sorted(array, key=lambda item: item['last_name'])

show(l1)
show(l2)