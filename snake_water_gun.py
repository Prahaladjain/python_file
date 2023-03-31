import random

options = ["snake", "water", "gun"]
user_score = 0
computer_score = 0

print("*******You have total five chances************")
print("***********Let's play the game***************")

for i in range(5):
    randomWord = random.choice(options)
    print("Choose any one from snake, water and gun")
    user_input = str(input())

    print("The computer choice is:-    "+randomWord)

    if randomWord == "water":
        if user_input == "snake":
            user_score += 1
        elif user_input == "gun":
            computer_score += 1
        else:
            print("equal point distribute")

    elif randomWord == "snake":
        if user_input == "water":
            computer_score += 1
        elif user_input == "gun":
            user_score += 1
        else:
            print("equal point distribute")

    else:
        if user_input == "snake":
            computer_score += 1
        elif user_input == "water":
            user_score += 1
        else:
            print("equal point distribute")

    print("User score :- " + str(user_score))
    print("computer score :- " + str(computer_score))

if user_score > computer_score:
    print("Congratulations! You won the game")
else:
    print("Sorry! You lost the game") # corrected the message