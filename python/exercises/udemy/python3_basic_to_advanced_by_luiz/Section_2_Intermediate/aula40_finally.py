# Try, except, else and finally

try:
    print('Open File')
    # 8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Divided by zero.')
except IndexError as error:
    print('Index Error')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Did\'t get error.')
finally: # Always gonna be used
    print('Close File')