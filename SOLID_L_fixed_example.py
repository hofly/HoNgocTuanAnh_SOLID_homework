from interface import implements, Interface

PITcodeDict={}

class employeeManager():
    def __init__(self, name):
        self.name=name
        
class PITInterface(Interface):
    def PIT(self, PITcode):
        pass

class part_time_employee(employeeManager,implements(PITInterface)):
    def PIT(self, PITcode):
        PITcodeDict[self.name]=PITcode


class full_time_employee(employeeManager,implements(PITInterface)):
    def PIT(self, PITcode):
        PITcodeDict[self.name]=PITcode

class intern(employeeManager):
    pass

employee1=full_time_employee('Andy')
employee1.PIT('1250L')
print(PITcodeDict)

