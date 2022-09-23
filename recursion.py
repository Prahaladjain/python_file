"""
# ----------ITERATIVE METHOD----------
def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
number=int(input("Enter a number"))
print("Factorial using Iterative method",factorial_iterative(number))
"""



"""
# ----------RECURSIVE METHOD----------
def factorial_recursive(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
number=int(input("Enter a number"))
print("Factorial using recursive method",factorial_recursive(number))
"""