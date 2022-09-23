"""
i=0
while(i<45):
    print(i)
    i=i+1
"""


"""
# ----------BREAK ----------
i=0
while(True):
    print(i+1,end=" " )
    if(i==44):
        break
    i=i+1
"""


"""
# ---------CONTINUE---------
i=0
while(1):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end=" ")
    if(i==44):
        break
    i=i+1
"""




# ----------EXERICISE4----------
print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()