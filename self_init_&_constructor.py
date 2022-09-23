"""
class Employee:
    no_of_leaves=8

    def printdetails(self):
        return f"The name is {self.name} salary is {self.salary} and role is {self.role}"

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=25000
harry.role="Instractor"

rohan.name="Rohan"
rohan.salary=10000
rohan.role="student"
print(rohan.printdetails())
print(harry.printdetails())
"""


"""
# ----------USING __init__ / CONSTRUCTOR___________
class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

harry=Employee("Harry",255,"Instructor")
print("my name is :",harry.name)
print("my salary is :",harry.salary)
print("my role is:",harry.role)
"""