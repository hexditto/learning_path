# dir, hasattr and getattr in Python
string = 'Luiz'
method = 'upper'

if hasattr(string, method):
    print('It has upper')
    print(getattr(string, method)())
else:
    print('There isn\'t a method', method)