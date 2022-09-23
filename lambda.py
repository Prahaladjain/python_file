"""
minus =lambda x,y:x-y
x=int(input("Enter first number"))
y=int(input("Enter second number"))

print("Both number are subtraction is",minus(x,y))
"""



"""
a=[[1,4],[5,3],[7,9],[6,2],[9,5]]
a.sort(key = lambda x:x[0])
print(a)
"""


"""
# ---------USING FUNCTION----------
def minus(x,y):
    print(x-y)
minus(9,5)




def a_sort(a):
    return a[0]
a=[[1,4],[5,3],[7,9],[6,2],[9,5]]
a.sort(key=a_sort)
print(a)
"""


"""
numbers=["3","34","64"]
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
numbers[2]=numbers[2]+1
print(numbers[2])
"""


"""
# ----------MAP----------
items=[1,2,3,4,5]
a=list(map((lambda x:x**3),items))
print(a)
"""


"""
# ----------FILTER----------
a=[1,2,3,4,5,6]
b=[2,5,0,3,7]
c=list(filter(lambda x: x in a,b))
print(c)
"""



"""
# ----------REDUCE----------
from functools import reduce
a=reduce((lambda x, y:x*y),[1,2,3,4,5])
print(a)
"""