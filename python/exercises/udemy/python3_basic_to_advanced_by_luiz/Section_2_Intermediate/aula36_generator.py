# Generator expression
import sys

lst = [n for n in range(100000)] # Too many values aloccated in the memory without being used
generator = (n for n in range(100000)) # Usually used to avoid memory allocation

# Bytes difference
print(sys.getsizeof(lst))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

print(generator)

# for n in generator:
#   print(n)