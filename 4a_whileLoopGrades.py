
numGrades=int(input('Enter the no. of subjects: '))
grades=[]
j=0
while(j<numGrades):
    grd=float(input('Input the grades received: '))
    grades.append(grd)
    j=j+1

j=0
print('All the grades are:')
while(j<numGrades):
    print(grades[j])
    j=j+1
