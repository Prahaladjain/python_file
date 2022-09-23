class Employee:
    no_of_leaves=8
    pass
harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=25000
harry.role="Instractor"

rohan.name="Rohan"
rohan.salary=10000
rohan.role="student"

print(rohan.no_of_leaves)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves=9
print(rohan.__dict__)
print(harry.__dict__)




