def calculator(operator, integer1, integer2):
    if operator == 'add':
        print(integer1 + integer2)
    elif operator == 'sub':
        print(integer1 - integer2)
    elif operator == 'mul':
        print(integer1 * integer2)
    elif operator == 'div':
        print(integer1 / integer2)
    else:
        print('{} is not supported.'.format(operator))
