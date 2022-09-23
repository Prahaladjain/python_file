# user se input lena h tab tk user 100 se upr ka number input na kre .100 se uper ka number input krne ke bad
# congratulation print krna h ydi 100 se kam number input krta h to try again print krna h

while(True):
    inp=int(input("Enter a number:\n"))
    if inp>100:
        print("congrats you have entered a number greater than 100\n")
    else:
        print("Try again")
        continue