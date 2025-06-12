# Yield from in python

def gen1():
    print('START GEN1')
    yield 1
    yield 2
    yield 3
    print('OVER GEN1')


def gen3():
    print('START GEN3')
    yield 10
    yield 20
    yield 30
    print('OVER GEN3')


def gen2(gen=None):
    print('START GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('OVER GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for number in g1:
    print(number)
print()
for number in g2:
    print(number)
print()
for number in g3:
    print(number)
print()