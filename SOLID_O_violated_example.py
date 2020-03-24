class price():
    def __init__(self, goods):
        self.goods=goods

    def printPrice(self):
        if self.goods=='hamburger':
            print('2$')
        elif self.goods=='coca':
            print('1$')

goods1=price('hamburger')
goods1.printPrice()

