from rectangle import Rectangle
from rectangle import Square
from rectangle import Circle


rect1 = Rectangle(3,4)
rect2 = Rectangle(12,15)

print(rect1.get_area())
print(rect2.get_area())

sq1 = Square(15)
sq2 = Square(22)

print(sq1.get_area_square(),sq2.get_area_square(),"\n")

figures = [rect1,rect2,sq1,sq2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

circ1 = Circle(6)
circ2 = Circle(11)

print(circ1.get_circle_area(),circ2.get_circle_area())