from s1691 import Rectangle

class R1(Rectangle):
    # def __init__(self,a,b,w=5,h=5):
    #     self.a = a
    #     self.b = b
    #     self.w = w
    #     self.h = h
    #     Rectangle.__init__(self,a,b,h,w)

    def get_area(self):
        return self.width * self.height

rect = R1(5,6,7,8)

print(rect)
print(rect.get_area())