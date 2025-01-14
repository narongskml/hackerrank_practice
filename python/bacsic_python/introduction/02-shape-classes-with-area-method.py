#!/bin/python3

import math



#COPY FROM BELOW, THE HEADERS ARE ALREADY INCLUDED IN CODE EDITOR
class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length

    def area(self):
        return self.breadth*self.length

#    pass

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
#    pass


if __name__ == '__main__':
    # Example usage of the classes (testing)
    
    # Example 1: Rectangle with length 4 and width 5
    rect = Rectangle(4, 5)
    print("{:.2f}".format(rect.area())) 

    # Example 2: Circle with radius 3
    circle = Circle(3)
    print("{:.2f}".format(circle.area()))