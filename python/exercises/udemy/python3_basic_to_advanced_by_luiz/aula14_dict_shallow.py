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
import copy # Has deepcopy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2] # shallow copy doesnt enter the list
}

# d2 = d1 # Doesn't create a copy, its a pointer to d1 instead
d2 = d1.deepcopy() # From module
d2 = d1.copy() # Now this is a shallow copy. Only copies immutable values

d2['c1'] = 1000
d2['l1'][1] = 99999 # Alters both
print(d1)
print(d2)