PITcodeDict={}

class employeeManager():
    def __init__(self, name):
        self.name=name
        
    def PIT(self, PITcode):
        PITcodeDict[self.name]=PITcode

class part_time_employee(employeeManager):
    pass

class full_time_employee(employeeManager):
    pass

class intern(employeeManager):
    pass

employee1=full_time_employee('Andy')
employee1.PIT('1250L')
print(PITcodeDict)

