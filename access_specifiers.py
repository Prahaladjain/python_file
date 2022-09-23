# public
# protected
# private


class Employee:
    no_of_leaves=8
    var=8              #-->public
    _protec=9          #->protected
    __private=98       #-->private

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The Name is {self.name} salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        print("This is good "+ {string})

emp=Employee("Harry",343,"Programmer")
print(emp.var)
print(emp._protec)
print(emp._Employee__private)
