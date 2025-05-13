# \n (quebra de linha) -> Unix
# \r\n -> CRLF (Windows)
print(12, 34, 1011, sep='-', end='\n##')
print(56, 78, sep='-')
print(9, 10, sep='-')