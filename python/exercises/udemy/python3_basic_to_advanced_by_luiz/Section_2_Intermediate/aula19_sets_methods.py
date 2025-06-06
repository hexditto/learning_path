# Handful methods:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4)) # the string will be iterable by the set
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
# Handful operators:
# union | union (union) - Unite
# intersection & (intersection) - Items in both
# diference - Items that bellow to the left set