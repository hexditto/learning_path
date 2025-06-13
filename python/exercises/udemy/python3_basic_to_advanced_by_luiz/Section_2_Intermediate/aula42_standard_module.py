# Standard modules in Python (import, from, as e *)
# integer - import name_module
# advantages - you have the namespace of the module
# disadvantages - large names
# import sys

# platform = "Mine"
# print(sys.platform)
# print(platform)

# parts - from name_module import object1, object2
# advantages - short names
# disadvantages - without namespace of the module
# from sys import exit, platform
# 
# print('bla')
# exit()

# alias 1 - import name_module as nickname
# alias 2 - from name_module import object as nickname
# advantages - you can reserve name code
# disadvantages - you can be outdated of the standard of the language
import sys as s
sys = 'something'
print(s.platform)
print(sys)

# bad manners - from name_module import *
# advantages - import everything from a module
# disadvantages - import everything from a module
