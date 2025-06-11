# Dictionary Comprehension and Set Comprehension
product = {
    'name': 'Blue Pen',
    'price': 2.5,
    'category': 'Office',
}

# Using Dict Comprehension
dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
    if key != 'category' # Filtering
}

print(dc)

lst = [
    ('a', 'value a'),
    ('b', 'value b'),
    ('c', 'value c'),
]

dc = {
    key: value
    for key, value in lst
}

# Set Comprehension

s1 = {2 ** i for i in range(10)}
print(s1)