"""
# ----------SINGLE INHERITANCE----------

class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name}.salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("_"))
    @staticmethod
    def printgood(string):
        print("This is good "+string)

class programmer(Employee):
    no_of_holiday=56
    def __init__(self,aname,asalary,arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language=languages

    def printporg(self):
        return f"The programmer's name is {self.name} salary is {self.salary} and role is {self.role}. The language are {self.language}"

harry=Employee("Harry",255,"student" )
karan=Employee("Karan",333,"programmer")
shubham=programmer("Shubham",555,"Programmer",["python"])
karan=programmer("Karan",777,"Programmer",["python","cpp"])
print(karan.name)
print(karan.no_of_holiday)
"""


"""
# ----------MULTIPLE INHERITANCE----------
class Employee:
    no_of_leaves=8
    
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name}.salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("_"))
    @staticmethod
    def printgood(string):
        print("This is good "+string)

class player:
    var=9
    no_of_game=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetails(self):
        return f"The Name is {self.name} and Game is {self.game}"

# class coolprogrammer(Employee,player):
class coolprogrammer(player,Employee):
    language="c++"
    def printlanguage(self):
        print(self.language)

harry=Employee("Harry",255,"student" )
karan=Employee("Karan",333,"programmer")
shubham=player("Shubham",["cricket"])
karan=coolprogrammer("Karan",["cricket"])

det=karan.printdetails()
karan.printlanguage()
print(det)
print(karan.var)
"""


"""
# ----------MULTILEVEL INHERITANCE----------
class Dad:
    basketball=6

class Son(Dad):
    dance=1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance=6
    def isdance(self):
        return f"Jackson Yeah! -- yes I dance very awesomely {self.dance} no of times"

darry=Dad()
larry=Son()
harry=Grandson()

print(harry.isdance())
print(larry.isdance())
"""
