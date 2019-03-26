n1 = int(input('첫번째 숫자를 입력하세요: '))
n2 = int(input('두번째 숫자를 입력하세요: '))
n3 = int(input('세번째 숫자를 입력하세요: '))

number = 1

while number % n1 != 0 or number % n2 != 0 or number % n3 != 0:
    number += 1
print('최소공배수는 {}입니다.'.format(number))
