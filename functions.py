a=9
b=6
c=sum((a,b))
print(c)


def function():
    print("Hello you are in function")
function()


def function1(a,b):
    print("Hello you are in function1",a+b)
function1(5,9)



def function2(a,b):
    average=(a+b)/2
    # print(average)
    return average
v=function2(2,6)
print(v)


# ----------DOC STRING----------
def function3(a,b):
      """This is a function which will calculate average of two numbers"""
      average=(a+b)/2
      return average
v=function3(5,9)
print(v)
print(function3.__doc__)
