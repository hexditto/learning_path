# isinstance - to know if the object is a certain type
lst = ['a', 1, 1.1, True, [0, 1, 2], (1, 2),
       {0, 1}, {'name': 'Luiz'}]


for item in lst:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, str))
    
    elif isinstance(item, (int, float)):
        print('NUMBER')
        print(item, item * 2)
    else:
        print('Another')
        print(item)