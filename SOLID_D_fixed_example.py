from interface import implements, Interface
from SOLID_employeeDatabase import IDnumberDict, IBnumberDict, PITcodeDict

class infoInterface(Interface):
    def printInfo(name):
        pass

class printIDN(implements(infoInterface)):
    def printInfo(name):
        print(IDnumberDict[name])

class printIBN(implements(infoInterface)):
    def printInfo(name):
        print(IBnumberDict[name])

class printPITcode(implements(infoInterface)):
    def printInfo(name):
        print(PITcodeDict[name])
        
class employeeInfo():
    def __init__(self, name):
        self.name=name

    def printInfo(self, infoClass):
        infoClass.printInfo(self.name)
        
employee1=employeeInfo('Andy')
employee1.printInfo(printIDN)
employee1.printInfo(printIBN)
employee1.printInfo(printPITcode)

