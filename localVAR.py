# Python program to demonstrate private members
# of the parent class


class C(object):
    def __init__(self):
        self.c = 21
        # d is private instance variable
        self.__d = 42
        print('Inside C.__init__',self.__d)

class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)


obj1 = C()
object1 = D()


# produces an error as d is private instance variable
print('dir(obj1)',dir(obj1))
print('Mangled "__d"',obj1._C__d)
print('e',object1.e)