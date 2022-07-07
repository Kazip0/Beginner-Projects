
numGrades=int(input('How many subjects/grades do you have? '))
grades=[]
sum=0

for i in range(0,numGrades,1):
    grade=float(input('Please enter your grade '))
    grades.append(grade)

print('')
print('All your grades are: ')
for i in range(0,numGrades,1):
    print(grades[i])

print('')
for i in range(0,numGrades,1):
    sum = sum + grades[i]
avg = sum/numGrades
print('Sum of all the grades is',sum)
print('The average of the sum is',avg)

print('')