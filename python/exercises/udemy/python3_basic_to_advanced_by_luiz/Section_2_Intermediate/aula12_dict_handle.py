# How to handle keys and values in dictionaries

person = {}

key = 'name'
person[key] = 'Luiz Otávio'
person['last_name'] = 'Miranda'

print(person[key])

person[key] = 'Maria'

del person['last_name']
print(person)

if person.get('last_name') is None:
    print('It doesnt exist')
else:
    print(person['last_name'])