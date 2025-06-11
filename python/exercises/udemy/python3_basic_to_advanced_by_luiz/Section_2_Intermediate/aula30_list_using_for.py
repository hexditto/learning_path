# List comprehension using more than one 'for' statement

# List without comprehension
lst = []
for x in range(3):
    for y in range(3):
        lst.append((x, y))

# Using list comprehension
lst = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lst)