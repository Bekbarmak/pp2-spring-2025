# exercise 1
class StringHandler:
    def getString(self):
        self.s = input("Enter a string: ")
    
    def printString(self):
        print(self.s.upper())

obj = StringHandler()
obj.getString()
obj.printString()


# exercise 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print("Shape area:", shape.area())  

square = Square(4)
print("Square area:", square.area())  
