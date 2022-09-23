import random
k="y"
while k!='n':
    print("welcome to snake water gun game")
    game_dict={"s":['water','gun'],"w":['snake','gun'],"g":['water','snake']}
    y="choose your player press 1 for player1 and press 2 for player2 :"
    print("choose your player press 1 for player1 and press 2 for player2")
    choose_player=[" ","player1","player2"]
    cp=int(input())
    count=0
    print("selected",choose_player[cp],"\n", end=" ")
    in_dic={"s":"sanke","g":"gun","w":"water"}
    print("select your input as alphabet: s=snake,w=water,g=gun")
    for i in range(10):
        game_input=input("select\n")
        print("you've selected ",in_dic[game_input])
        if game_input== "s":
            ran=random.choice(game_dict["s"])
            print(ran)
            if ran=="water":
                print("you have won")
                count+=1
            else:
                print("you lost and computer win")
            print("Total Attempts are 10","Left",(8+1)-i)

        elif game_input=="w":
            ran = random.choice(game_dict["w"])
            print(ran)
            if ran == "gun":
                print("you have won")
                count += 1
            else:
                print("you lost and computer win")
            print("Total Attempts are 10", "Left", (8 + 1) - i)
        elif game_input=="g":
            ran = random.choice(game_dict["g"])
            print(ran)
            if ran == "snake":
                print("you have won")
                count += 1
            else:
                print("you lost and computer win")
            print("Total Attempts are 10", "Left", (8 + 1) - i)
    print("you won",count,"computer won",(10-count))
    k=input("would you like to play one more time? y/n \n")
print("Thanks for playing snake water and gun")