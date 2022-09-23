# What is the output for given program code

# x=89
# def harry():
#     x=20
#     def rohan():
#         global x
#         x=88
#         rohan()
#     print("After calling rohan()",x)
# harry()
# print(x)




x=89
def harry():
    x=20
    def rohan():
        global x
        x=88
        rohan()
    print("After calling rohan()",x)
harry()
print(x)
