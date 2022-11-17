# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class .
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped


class Rectangle:
    # rectangle class
    def __init__(self, l, b):
        #length & bredth is defined
        self.l = l
        self.b = b

    # area

    def Area(self):
        area = self.l*self.b
        print(area)

    def Perimeter(self):
        perimeter = 2*(self.l+self.b)
        print(perimeter)

    def display(self):
        print("length = ", self.l, "bredth =", self.b)
        print("Aread = ", self.Area())
        print("Perimeter = ", self.Perimeter())


class Parallelepiped(Rectangle):

    # parallel .. is a child class of rectangle
    # height as attribute
    def __init__(self, l, b, h):
        Rectangle.__init__(self, l, b)
        self.h = h
    
    def Volume(self):
        print(self.h*self.l*self.b)

myrectangle = Rectangle(10, 20)
myrectangle.display()

para = Parallelepiped(50, 100, 150)
para.Volume()


