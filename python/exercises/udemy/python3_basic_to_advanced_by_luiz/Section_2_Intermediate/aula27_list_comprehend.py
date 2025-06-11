# List comprehension in Python
# List comprehension is a quick way to create lists from iterables
# print(list(range(10)))

# Doing without list comprehension
array: list[int] = []
for number in range(10):
    array.append(number)
# print(array)

# With list comprehension
array2: list[int] = [number * 2 for number in range(10)]
print(array2)