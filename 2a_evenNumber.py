num = int(input('Please enter the number to check whether it is odd or even: '))
rem = num%2
if(num>0 and rem==0):
    print(num, ' is an even positive number')
if(num>0 and rem ==1):
    print(num, 'is an odd positive number')
if(num<0 and rem==0):
    print(num, ' is an even negative number')
if(num<0 and rem ==1):
    print(num, 'is an odd negative number')
if(num==0):
    print('The number is zero')
