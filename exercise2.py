# ----------FAULTY CALCULATOR----------

a=int(input("Enter first number"))
b=int(input("Enter second number"))
opr=input("Enter operator")

if a==45 and b==3 and opr=="*":
    print("555")
elif a==56 and b==9 and opr=="+":
    print("77")
elif a==56 and b==6 and opr=="/":
    print("4")
elif opr=="+":
    print("sum of two number:",a+b)
elif opr=="-":
    print("subtract of two number:",a-b)
elif opr=="*":
    print("multiplication of two number:",a*b)
elif opr=="/":
    print("division of two number:",a/b)
else:
    print("undefine symbol")
