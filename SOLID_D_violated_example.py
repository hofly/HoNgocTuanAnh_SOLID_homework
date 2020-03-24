from SOLID_employeeDatabase import PITcodeDict

class employeeInfo():
    def __init__(self, name):
        self.name=name

    def printInfo(self):
        print(PITcodeDict[self.name])

employee1=employeeInfo('Andy')
employee1.printInfo()

