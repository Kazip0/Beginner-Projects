def tally(nums):             #defines a function
    x=[]                     #array for storing the required the number of marks
    for i in range(0,nums,1):
        myNum=float(input('Enter your number: '))
        x.append(myNum)
    return x

num=int(input('How many subjects were studied: '))          #since num is passed to function where a for loop
y=tally(num)                                                # is present therefore loops can only done using integers and not floating numbers

print('The marks are as follows: ') 
print(y)
