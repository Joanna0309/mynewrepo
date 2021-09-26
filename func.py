
class Square:
    def __init__(self, side):
        self.side = side

        print('The square has %s m2.'%self.calculate())

    def calculate(self):
        return self.side**2


obj = Square(4)
