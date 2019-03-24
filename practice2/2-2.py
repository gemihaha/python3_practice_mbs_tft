x = int(input('x를 입력하세요: '))
y = int(input('y를 입력하세요: '))

if x%y == 0:
    print('zero')
elif (x%y)%2 == 0:
    print('even')
else:
    print('odd')
