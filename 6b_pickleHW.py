
import pickle
names=[]
grades=[]
numStudents=int(input('How many students do you have: '))

for j in range(0,numStudents,1):
    name=input('Please enter the student name: ')
    names.append(name)
    prompt='Please enter ' + name + "'s grade: "            #single quote refers to string literal and double quote also represents string literal 
    grade=float(input(prompt))                              # but it allows single quotes and comma to be used in dounle quotes           
    grades.append(grade)

with open('studentsData.pkl','wb') as datax:
    pickle.dump(numStudents,datax)
    pickle.dump(names,datax)
    pickle.dump(grades,datax)

with open('studentsData.pkl','rb') as dataG:
    numStudents=pickle.load(dataG)
    names=pickle.load(dataG)
    grades=pickle.load(dataG)

print(numStudents)
print(names)
print(grades)

while(1==1):
    name=input('Which student do you want to know about: ')
    for i in range(0,numStudents,1):
        if (names[i]==name):
            print(name,"'s grade is", grades[i])
            print(str(name)+"'s grade is "+ str(grades[i]) )                #all the values/setails are in string and are added/catenated to form a sentence

