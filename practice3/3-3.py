def expand_rectangle(x, y):
    origin = x*y
    changed = (x+5)*(y*2)
    print('Width = {}'.format(x+5))
    print('Length = {}'.format(y*2))
    print('Area Ratio = {:.2f}'.format(origin/changed))
