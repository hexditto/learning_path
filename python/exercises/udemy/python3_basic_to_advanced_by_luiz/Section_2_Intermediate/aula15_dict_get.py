# Common dictionaries methods in python
# len - how many keys
# keys - iterable with keys
# values - iterable with values
# items - iterable with keys and values
# setdefault - add value if key exist
# copy - return shallow copy
# get - get a key
# pop - erase an item with a specified key (del)
# popitem - erase last added item
# update - update a dict with another

p1 = {
    'name': 'Luiz Otávio',
    'last_name': 'Miranda',
}

# print(p1['name'])
# print(p1.get('name'))
# name = p1.pop('name')
# print(name)
# print(p1)

# p1.update({
#     'name': 'new value',
#     'idade': 30,
# })

# p1.update(name='new value', idade=30)
tupla = (('name', 'new value'), ('idade', 30))
lista = [['name', 'new value'], ['idade', 30]]
p1.update(lista)
print(p1)