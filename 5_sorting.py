numGrades=int(input('Enter the number of subjects: '))
grades=[]
lowGrade=100
maxGrade=0

for i in range(0,numGrades,1):
    grade=float(input('Please enter the grade: '))
    grades.append(grade)


print('')
for i in range(0,numGrades,1):
    if(grades[i]<lowGrade):
        lowGrade=grades[i]        
print('The lowest Grade is: ', lowGrade)

for i in range(0,numGrades,1):
    if(grades[i]>maxGrade):
        maxGrade=grades[i]
print('The Maximum Grade is: ', maxGrade)


for i in range(0,numGrades-1,1):
    for i in range(0,numGrades-1,1):
        if grades[i]<grades[i+1]:
            swp=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=swp

print('The sorted grades in desending order is:')
for i in range(0,numGrades,1):
    print(grades[i])


for i in range(0,numGrades-1,1):
    for i in range(0,numGrades-1,1):
        if grades[i]>grades[i+1]:
            msp=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=msp

print('The sorted grades in ascending order is:')
for i in range(0,numGrades,1):
    print(grades[i])
