class A:
    def __init__(self, n='Rahul'):
        self.name = n


class B(A):
    def __init__(self, roll, name):
        self.roll = roll
        # self.name = name
        A.__init__(self,name)

ss = A('Nani')
object = B(23,'Ferr')

print(object.name)
print(ss.name)
# print(ss.roll)
print(object.roll)
