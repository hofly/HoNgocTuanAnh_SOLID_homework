from interface import implements, Interface

IDnumberDict={}
IBnumberDict={}
PITcodeDict={}


class employeeManager():
    def __init__(self, name):
        self.name=name
        
class IDNInterface(Interface):
    def IDN(self, IDnumber):
        pass

class IBNInterface(Interface):
    def IBN(self, IBnumber):
        pass

class PITInterface(Interface):
    def PIT(self, PITcode):
        pass

class full_time_employee(employeeManager,
                         implements(IDNInterface,IBNInterface,PITInterface)):
    def IDN(self, IDnumber):
        IDnumberDict[self.name]=IDnumber
        
    def IBN(self, IBnumber):
        IBnumberDict[self.name]=IBnumber
        
    def PIT(self, PITcode):
        PITcodeDict[self.name]=PITcode

class intern(employeeManager,
             implements(IDNInterface,IBNInterface)):
    def IDN(self, IDnumber):
        IDnumberDict[self.name]=IDnumber
        
    def IBN(self, IBnumber):
        IBnumberDict[self.name]=IBnumber

employee1=full_time_employee('Andy')
employee1.PIT('1250L')
employee1.IDN('123456')
employee1.IBN('789')
print(PITcodeDict)
print(IBnumberDict)
print(IDnumberDict)
