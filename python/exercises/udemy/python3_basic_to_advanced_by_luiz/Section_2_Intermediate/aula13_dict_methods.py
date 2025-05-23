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

person = {
    'name': 'Luiz Otávio',
    'last_name': 'Miranda',
    'idade': 900,
}

person.setdefault('idade', None)
print(person['idade'])
# print(len(person))
# print(list(person.keys()))
# print(list(person.values()))
# print(list(person.items()))
  
# for keys in person:
#     print(keys)
# 
# for keys, values in person.items():
#     print(keys, values)