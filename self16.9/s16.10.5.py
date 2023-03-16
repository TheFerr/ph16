class NonPositiveDigitException(ValueError):
    pass
    def __init__(self):
        print('Sq edge less or equal 0')

class SquareException:
    def __init__(self,edge):
        self.edge = edge
        if self.edge <= 0:
            raise NonPositiveDigitException
        else:
            print(self.edge**2)

SquareException(2)
