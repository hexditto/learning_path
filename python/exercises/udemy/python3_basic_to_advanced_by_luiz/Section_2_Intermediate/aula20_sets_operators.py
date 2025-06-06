# Handful operators:
# union | union (union) - Unite
# intersection & (intersection) - Items in both
# diference - Items that bellow to the left set
# symmetric difference ^ - Items that dont bellow to both

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # union of the sets
s4 = s1 & s2 # intersection
s5 = s1 - s2 # diffence
s6 = s2 ^ s1 # symmetric difference
print(s3)
print(s4)
print(s5)
print(s6)