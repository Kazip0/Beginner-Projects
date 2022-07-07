import pickle                                   #importing library to save and read data files with pickle
fruits=['apple','oranges','banana']
x=7
y=3.14
nuts=['pecan','almond']
grades=[99,100,56,77,85]

dataSet=[fruits,x,y,nuts,grades]                # combination of arrays and variables

with open('myData.pkl','wb') as f:              # writes/saves data in binary
    pickle.dump(fruits,f)                                           
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(nuts,f)
    pickle.dump(grades,f)
    pickle.dump(3,f)
    

    pickle.dump(dataSet,f)

with open('myData.pkl','rb') as f2:            #loads/reads data in binary
    a=pickle.load(f2)                          # all the datas are loaded in serial just as it was saved
    b=pickle.load(f2)
    c=pickle.load(f2)
    d=pickle.load(f2)
    e=pickle.load(f2)
    f=pickle.load(f2)

    bigKahuna=pickle.load(f2)

print(a)                                       #prints the required data on terminal
print(b)
print(c)
print(d)
print(e)
print(f)

print(bigKahuna)

for dt in bigKahuna:                    #prints every element of the list, bigKahuna
    print(dt)