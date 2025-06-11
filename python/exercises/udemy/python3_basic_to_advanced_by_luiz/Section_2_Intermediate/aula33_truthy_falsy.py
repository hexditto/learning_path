# Truthy and Falsy values, Imutable and mutable types
# Mutables [] {} set()
# Imutable () "" 0 0.0 None False range (0, 10)
lst = []
dictionary = {}
set_ = set()
tpl = ()
string = ''
integer = 0
floating = 0.0
nothing = None
false = False
rng = range(0)

def falsy(value):
    return 'falsy' if not value else 'truthy'

print(f'TEST', falsy('TEST'))
print(f'{lst=}', falsy(lst))
print(f'{dictionary=}', falsy(dictionary))
print(f'{set_=}', falsy(set_))
print(f'{tpl=}', falsy(tpl))
print(f'{string=}', falsy(string))
print(f'{integer=}', falsy(integer))