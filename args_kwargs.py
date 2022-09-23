"""
def funargs(*args):
    print(type(args))
    print(args[0])

har=["Harry","Rohan","Skillf","Hammad","Shivam"]
funargs(*har)
"""



"""
def funargs(normal,*args):
    print(normal)
    for item in args:
        print(item)
har=["Harry","Rohan","Skillf","Hammad","Shivam","The prgrammer"]
normal="i am a normal Argument and the student are:"
funargs(normal,*har)
"""



"""
def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce some of our heroes")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
har=["Harry","Rohan","Skillf","Hammad","Shivam","The prgrammer"]
normal="i am a normal Argument and the student are:"
kw={"Rohan":"moniter","Harry":"fitness instructor","The programmer":"cordinator","Shivam":"cook"}
funargs(normal,*har,**kw)

"""