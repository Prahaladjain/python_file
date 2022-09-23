me="Harry"
a1=3
a="This is %s %s"%(me,a1)
print(a)
a="This is {1} {0}"
print(a)
b=a.format(me,a1)
print(b)



a=f"This is {me} {a1} {4*65}"
print(a)


import math
a=f"This is {me} {a1} {math.cos(65)}"
print(a)