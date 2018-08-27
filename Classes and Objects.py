#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class circle:
    def __init__(self,r):
        self.radius=r
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        return 2*3.14*self.radius
a=int(input("enter radius "))
area=circle(a)
print("area if circle is",area.getArea())
print("circumference of circle is",area.getCircumference())

#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.

class student:
    def __init__(self,name,r_no):
        self.n=name
        self.r=r_no
    def Display(self):
        print("name=",self.n,"roll no=",self.r)
    def setAge(self,age):
        self.age=age
        print("age=",self.age)
    def setMarks(self,m):
        self.marks=m
        print("marks=",self.marks)
a=student('Rajat Oberoi',1610991682)
a.Display()
a.setAge(20)
a.setMarks(80)

#Q.3- Create a Temprature class and create two methods: 
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class temp:
    def __init__(self):
        print("converting temperature")

    def convertFahrenheit(self,c):
        self.c=c
        print("temp in fahrenheit is",(self.c*9/5)+32)
    def convertCelsius(self,f):
        self.f=f
        print("temp in celsisus is",(self.f-32)*(5/9))
temp1=temp()
temp1.convertFahrenheit(30)
temp1.convertCelsius(99)

#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details.

class MovieDetails:
    def __init__(self,a,y,r):
        self.a=a
        self.y=y
        self.r=r
    def display(self):
        print("artist name",self.a,"year of release",self.y,"rating",self.r)
    def Add(self,n):
        self.n=n
        print("name of movie added ",self.n)
b=MovieDetails('Stark',1999,8.5)
b.display()
b.Add('IRON MAN')

#Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    def animal_attribute(self):
        print("base class animal attribute")

class Tiger(Animal):
    def display(self):
        print("derived class called")

a=Tiger()
a.display()
a.animal_attribute()

#Q6 Output
#Ans is A B
#       A B


#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.

class Shape:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def Area(self):
        print("area method created")

class rectangle(Shape):
 
    def Area(self):
        print("area of rect is = ",self.l*self.b)

class square(Shape):

    def Area(self):
        print("area of square is",self.l*self.l)

a= rectangle(10,20)
a.Area()
c=square(5,9)
c.Area()

