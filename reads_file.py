"""
f=open("harry.txt")
content=f.read()
print(content)
f.close()
"""



"""
f=open("harry.txt","rt")
content=f.read(3)
print(content)
content=f.read(5)
print(content)
content=f.read(9)
print(content)
f.close()
"""

"""
f=open("harry.txt","rt")
for line in f:
    print(line,end=" ")

print(f.readline())
f.close()
"""


"""
f=open("harry.txt","rt")
print(f.readlines())
"""






"""
# ----------USING WITH BLOCK TO OPEN A FILE----------
with open("harry.txt") as f:
    a=f.readlines()
    print(a)
"""


"""
# ----------QUESTIONOF THE DAY----------
with open("harry.txt") as f:
    a=f.readlines()
    print(a)
f=open("harry.txt","rt")
print(f.readlines())
f.close()
"""