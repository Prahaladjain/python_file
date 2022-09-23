"""
class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

harry=Employee("Harry",255,"student")

harry.change_leaves(34)
print(harry.name)
print(harry.no_of_leaves)
"""



"""
# ----------CLASS METHOD AND ALTERNATIVE CONSTRUCTOR----------

class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        params=string.split("_")
        print(params)
        return cls(params[0],params[1],params[2])
        return cls(*string.split("_"))


harry=Employee("Harry",255,"student")
rohan=Employee("Rohan",333,"programmer")
karan=Employee.from_dash("Karan_400_Instructor")
"""





"""
# ----------STATIC METHOD----------

class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        params=string.split("_")
        print(params)
        return cls(params[0],params[1],params[2])
        return cls(*string.split("_"))
    @staticmethod
    def printgood(string):
        print("This is good "+string)

harry=Employee("Harry",255,"student")
rohan=Employee("Rohan",333,"programmer")

Employee.printgood("Prahalad")
"""