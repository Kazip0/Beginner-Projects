def tally(x,y):          #variables name inside the function need not necessarily have to match the variables name that are assign to it
    z=x+y
    a=23                   #the value of a and b stays inside the scope of the function
    b=45                   #what happens in a function stays in a fucntion
    print('afun is:',a)     
    print('bfun is:',b)
    return z


a=float(input('Enter the first number: '))
b=float(input('Enter the second number: '))

c=tally(a,b)                #passes value of a to x and b to y to create c=a+b
print('a is:',a)            #the value of a and b does not change even after changing values by function tally
print('b is:',b)
print('The final sum is:',c)



