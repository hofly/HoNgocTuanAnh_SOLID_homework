from interface import implements, Interface

class orderInterface(Interface):
    def printOrder(self):
        pass
    
class orderFood(implements(orderInterface)):
    def __init__(self, food):
        self.food=food

    def printOrder(self):
        print(self.food)

class orderDrink(implements(orderInterface)):
    def __init__(self, drink):
        self.drink=drink

    def printOrder(self):
        print(self.drink)

guest1=orderFood(['Hamburger', 'Pizza'])
guest1.printOrder()
guest1=orderDrink('Coca')
guest1.printOrder()
