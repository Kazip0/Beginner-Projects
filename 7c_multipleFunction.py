def tally(x,y):          #variables name inside the function need not necessarily have to match the variables name that are assign to it
    sum=x+y
    prod=x*y
    diff=x-y
    div=x/y
    
    return sum,prod,diff,div


a=float(input('Enter the first number: '))
b=float(input('Enter the second number: '))

w,x,y,z=tally(a,b)          
print('The final sum is:',w)
print('The final product is:',x)
print('The final difference is:',y)
print('The final division result is:',z)
print(f'The final division result is: {z}')
print(f"The final division result is: {z}")


