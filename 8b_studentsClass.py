class Students:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    
    def gin(self,ng):               # here self is used to access the datas stored in self.first and self.last
                                    
        self.ng = ng                # values are accpeted in form of self.<variable> inside class
        self.grades=[]
        for i in range(0,ng,1):        #as self.ng is already assigned as ng in this method 
                                       # we can freely use ng instead of typing self.ng

            grd=float(input('Please enter '+self.first+' '+self.last+"'s grade "))
            self.grades.append(grd)
        return self.grades

    def printGrades(self):
        print(self.first, self.last+"'s Grades are: ")
        for i in range(0,self.ng,1):
            print(self.grades[i])
        print('')

    def avg(self):
        bucket=0
        for i in range(0,self.ng,1):
            bucket=bucket+self.grades[i]
        avg=bucket/self.ng
        return avg
    
    def highlow(self):
        highGrade=0
        lowGrade=100
        for i in range(0,self.ng,1):
            if self.grades[i]>highGrade:
                highGrade=self.grades[i]
            if self.grades[i]<lowGrade:
                lowGrade=self.grades[i]
        return lowGrade,highGrade

student1=Students('Joe','Evans')
student2=Students('Akise','Aru')

print(student1.first,student1.last)
print(student2.first,student2.last)

student1.gin(4)
student1.printGrades()
avg=student1.avg()

print(student1.first,student1.last,'has an average of',avg)

lowG,highG=student1.highlow()
print(student1.first+' has a high grade of: '+str(highG))
print(student1.first+' has a low grade of: '+str(lowG)+'\n')

student2.gin(4)
student2.printGrades()
avg=student2.avg()

print(student2.first,student2.last,'has an average of',avg)

lowG,highG=student2.highlow()
print(student2.first,'has a high grade of: ',highG)
print(student2.first+' has a low grade of: '+str(lowG))

