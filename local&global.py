"""
l=10
def function(n):
    l=5
    print(l)
    print(n,"I have printed")
function("This is me")
"""


"""
l=10
def function(n):
    m=8
    global l
    l=l+45
    print(l,m)
    print(n,"I have printed")
function("This is me")
"""

"""
def harry():
    x=20
    def rohan():
        global x
        x=88
    print("Before calling rohan()",x)
    rohan()
    print("After calling rohan()",x)
harry()
"""


"""
def harry():
    x=20
    def rohan():
        global x
        x=88
    print("Before calling rohan()",x)
    rohan()
    print("After calling rohan()",x)
harry()
print(x)
"""