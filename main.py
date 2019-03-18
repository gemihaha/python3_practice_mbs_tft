##print('Hello', 'World')
##print('Hello', 'World', sep='')
##print('Hello', 'World', sep='|')
##print(2*3.14*10)
##print('I\'m', 2019-1992, 'years old')
##print('This is a \nNew line')
##print('No. \tNAME\tGENDER\n1\tJohn\tMale')


##print(format('Hello','>10'))
##print(format('Hello','^10'))
##print(format('Hello','10'))
##print(format('ID','5'),format('NAME','10'),format('GENDER','10'))
##print(format(5/9,'f'))
##print(format(5/9,'.2f'))
##print(format(5/9,'10.2f'))


##print(format(1000000, ','))
##print(format(100000,',.2f'))
##print(format(255,'X'))
##print(format(255,'b'))

##practice 0-1
##print(format(10000000,','),'KRW','=>','USD', format(10000000/1127.83, ',.2f'))


##practice 0-2
##print('I\'m T.\nLet\'s study "python".')

## Practice 1-1
'''
a=10
a=a/2
c=a**3
print(a+c)

b=10.0
d=b*3-10
print(d%4)
'''
## Practice 1-2
##str1 = 'I '
##str2 = 'love '
##str3 = 'you'
##str4 = str1 + str2 + str3
##print(str4)
##str4 = str4[0:6]
##str5 = str4 + ' programming'
##print(str5)



## Practice 1-4
##lst = [1,7,[4,9],'f',('a','b')]
##print(lst)
##lst.append('g')
##print(lst)
##print(lst[4:])
##print(lst[-2:])
##print(list[2][1]) ***


## Practice 1-5
##lst2 = [['A'.lower(),'B'.lower(),'C'.lower(),'D'.lower(),'E'.lower()],['F'.lower(),'G'.lower(),'H'.lower(),'I'.lower(),'J'.lower()],['K'.lower(),'L'.lower(),'M'.lower(),'N'.lower(),'O'.lower()]]
####lst2 = lst2.lower()
##print(lst2[0],'\n',lst2[1],'\n',lst2[2])


## Practice 2-1

##x = int(input("x 입력"))
##y = int(input("y 입력"))
##
##if x > y :
##    print('x가 y보다 큽니다')
##elif x==y :
##    print('x와 y가 같습니다')
##else : 
##    print('x가 y보다 작습니다')


## Practice 2-2
##x = int(input("x를 입력하세요: "))
##y = int(input("y를 입력하세요: "))
##
##if x%y == 0 : 
##        print("zero")
##elif (x%y)%2 == 0 : 
##        print("even")
##else : 
##        print("odd")


## Practice 2-3
##t = [1,3,5,7,'a','b','c']
##if 5 in t :
##    print('5 is in t')
##
##if 'd' in t :  
##    print('d is in t')


## Practice 2-4
##number = 0
##
##while number < 10 :
##    print('10 보다 작습니다')
##    number+=1
##
##print('종료')


## Practice 2-5
##x = int(input("첫번째 숫자를 입력하세요: "))
##y = int(input("두번째 숫자를 입력하세요: "))
##z = int(input("세번째 숫자를 입력하세요: "))
##
##n = 1        
####while n%x !=0 or n%y !=0 or n%z !=0 :
####    n += 1
##
##while True :
##    n+=1
##    if n%x==0 and n%y==0 and n%z==0:
##        break
##
##print('최소공배수는 {} 입니다'.format(n))
##


## Practice 2-7
##integers = [1,2,3,4,5,6,7,8,9,10]
##for i in integers:
##    if(i%2 !=0):
##        print(i)



## Practice 2-8
##
##for i in range(2,10):
##    for j in range(1,10):
##        print(i*j,end =' ')
##    i+=1
##    print('\n')
        

## 자료형 - 예제문제 1

##money_input = int(input("1회당 납입 금액을 입력하세요 : "))
##n = int(input("납입 횟수를 입력하세요: "))
##
##money_result= (money_input*(((1+0.03)**n)-1))/0.03
##
##print('결과는 {:,.2f} 원입니다.'.format(money_result))


## 자료형 - 예제문제 2

##distance = int(input("가야할 거리를 입력하세요: "))
##money = int(input("현재 가진 돈을 입력하세요: "))
##cost = 3000 + 2*distance
##money_result = money - cost
##
##print("택시요금은 {:,.2f} 원이고 남은 돈은 {:,.2f} 원입니다".format(cost,money_result))


## 자료형 - 예제문제 3
##hour = int(input("현재 '시'를 입력하세요.: "))
##to_go = int(input("몇 분 뒤의 시각을 알고 시프신가요: "))
##
##result_h = (hour + to_go//60) % 24  
##result_m = to_go%60
##
##    
##print("{} 분 뒤는 {} 시 {} 분 입니다 ".format(to_go, result_h, result_m))



## 제어문  - 예제문제 2

##score = [70,60,55,75,95,90,80,80,85,100]
##sum = 0
##
##for i in range(len(score)):
##    sum += score[i]
##
##avg= (sum/len(score))
##print(avg)

'''
for j in score:
    sum += j
avg= (sum/len(score))
print(avg)
'''

## 자료형 - 예제문제 4
##
##students = [
##{'번호' : 0, '학번' : '2019-1000' , '이름' : 'Bob' , '중간고사' : 76, '결석횟수': 2},
##{'번호' : 1, '학번' : '2019-1001' , '이름' : 'Chris' , '중간고사' : 76, '결석횟수': 2},
##{'번호' : 2, '학번' : '2019-1002' , '이름' : 'Diana' , '중간고사' : 76, '결석횟수': 2},
##{'번호' : 3, '학번' : '2019-1003' , '이름' : 'Irene' , '중간고사' : 76, '결석횟수': 2}]
##
##
##del students[1]
##
##students[1]['중간고사'] = 90
##students[2]['결석횟수'] = 1
##students[0]['기말고사'] = 85
##students[1]['기말고사'] = 100
##students[2]['기말고사'] = 30
##print(students)


## Practice 3-1

##def calculator(op, int1, int2) :
##    if op == 'add' :
##        return int1 + int2
##
##    elif op == 'sub' :
##        return int1 - int2
##
##    elif op == 'mul' :
##        return int1*int2
##
##    elif op == 'div' :
##        return int1/int2
##
##    else :
##        print('{} is not supported.'.format(op))
##print(calculator('add',1,2))
##print(calculator('sub',1,2))
##print(calculator('mul',1,2))
##print(calculator('div',1,2))


## Practice 3-2
def vowel(words) :
    count = 0
    for i in range(len(words)) :
        if words[i] == 'a' :
            count+=1

        elif words[i] == 'e' :
            count+=1

        elif words[i] == 'i' :
            count+=1

        elif words[i] == 'o' :
            count+=1
                  
        elif words[i] == 'u' :
            count+=1

    print(count)


vowel('apples')
vowel('Hello Mobis')


## Practice 3-3





