class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def Area(self):
        print("Area of Circle is:", 3.14 * self.radius * self.radius)

    def Perimeter(self):
        print("Perimeter of Circle is:",  2 * 3.14 * self.radius)

c1 = Circle(7)
c1.Area()
c1.Perimeter()