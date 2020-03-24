class order():
    def __init__(self, food, drink):
        self.food=food
        self.drink=drink
        
    def printOrder(self):
        print(self.food)
        print(self.drink)

guest1=order(['Hamburger', 'Pizza'], 'Coca')
guest1.printOrder()
