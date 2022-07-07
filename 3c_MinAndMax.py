numGrades=int(input('Enter the number of subjects: '))
grades=[]
lowGrade=100
maxGrade=0

for i in range(0,numGrades,1):
    grade=float(input('Please enter grade: '))
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
