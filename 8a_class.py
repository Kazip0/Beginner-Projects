class Rectangle:
    def __init__(self,c,l,w):       #function inside of a class is called a method and it is as same as function
                                    #use of __init__ function, parameters are passed not to class but to __init__ parameters
                                    #self is the name of object i.e. rect1 and rect2 when it calls the class
                                    #rect1 is an object of closs Rectangle
        
        self.color=c                #runs rect1 at first then rect2
        self.length=l
        self.width=w


        #EXTRA EXTRA EXTRA
        print('Width is:',w)        #as w is already declared in this method 
                                    # we can freely use w instead of typing self.w 



    def area(self):                        #when in using self all the values passed 
        self.area=self.length*self.width   #are in the form of self.<variable>
        return self.area

    def per(self):
        self.perimeter=2*(self.length+self.width)
        return self.perimeter

    def dig(self):
        self.diagonal=( (self.length)**2 + (self.width)**2 )**(1/2)
        return self.diagonal
    

rect1=Rectangle('red',2,1)     
rect2=Rectangle('blue',4,2)
print(rect1.color)
print(rect2.color)
print('rect1 lenght is:',rect1.length)
print('rect2 length is:',rect2.length)
print('')

print('rect1 width is:',rect1.width)
print('rect2 width is:',rect2.width)                #color, width and length are variables inside __init__ sunction
                                                    #and that's why () are not used to call them
print('')

print('Area of rect1 is:',rect1.area())             #area is the function/method so brackets is used () to call it
print('Area of rect2 is:',rect2.area())

print('')

print('Perimeter of rect1:',rect1.per())            #per is a function so () brackets are used
print('Perimeter of rect2:',rect2.per())

print('')

print('Diagonal of rect1 is',round(rect1.dig(), 1) )
print('Diagonal of rect2 is',round(rect2.dig(), 1) )
