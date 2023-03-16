class Rectangle:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def __str__(self):
        return f'Rectangle : {str(self.x)}, {str(self.y)}, {str(self.width)}, {str(self.height)}.'

rec1 = Rectangle(5,10,100,50)

# print(rec1)