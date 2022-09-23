# guess the number
# n=18
# no of guess 9
# print no of guesses left
# no of guesses he took to finish game over


n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses, "no.of guesses he took to finish.")
        break
    print(9 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1


if (number_of_guesses > 9):
    print("Game Over")
print("Thanks for guess the number")




"""
# ------------EXERCISE 4------------
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
"""