from interface import implements, Interface

class priceInterface(Interface):
    def price():
        pass

class hamburger(implements(priceInterface)):
    def price():
        print('2$')

class cola(implements(priceInterface)):
    def price():
        print('1$')

class pizza(implements(priceInterface)):
    def price():
        print('10$')

hamburger.price()

