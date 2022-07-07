def tally(numnum,myArray):
    total=0
    for i in range(0,numnum,1):
        total=total+myArray[i]
    return total

#num=5
#x=[2,4,6,7,9]
#mySum=tally(num,x)
#print('The sum of the number is:',mySum)
#print("The sum of the datas are "+str(mySum) )

datar=[]
num=int(input('Enter the number of datas in an array: '))
for i in range(0,num,1):
    dat=int(input('Enter the values of the data: '))
    datar.append(dat)

mySum=tally(num,datar)
print('The sum of the number is:',mySum)
