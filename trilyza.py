
def playerChoice(arr,player):
    symbol=""
    a=b=1
    if player==1:
        symbol="X"
    else:
        symbol="O"
    while a==1:
        choice = [int(x) for x in input("Enter position:").split()]
        while (1>choice[0] or choice[0]>3 or 3<choice[1] or choice[1]<1):
            print ("Invalid Position")
            choice = [int(x) for x in input("Enter position:").split()]
        if arr[choice[0]-1][choice[1]-1] == " ":
            arr[choice[0]-1][choice[1]-1] = symbol
            printArray(arr)
            a=0
        else:
            print("position occupied. Select another position")
            printArray(arr)
    return arr


def defineOutcome(a1):
    if (a1[0][0]==a1[0][1]==a1[0][2] != " "):
        if a1[0][0]=="X":
            print("Player 1 is the Winner!")
            return 1
        elif a1[0][0]=="O":
            print("Player 2 is the Winner!")
            return 1
    elif (a1[0][0]==a1[1][1]==a1[2][2] != " "):
        if a1[0][0]=="X":
            print("Player 1 is the Winner!")
            return 1
        elif a1[0][0]=="O":
            print("Player 2 is the Winner!")
            return 1
    elif (a1[0][2]==a1[1][1]==a1[2][0] != " "):
        if a1[0][2]=="X":
            print("Player 1 is the Winner!")
            return 1
        elif a1[0][2]=="O":
            print("Player 2 is the Winner!")
            return 1
    elif (a1[1][0]==a1[1][1]==a1[1][2] != " "):
        if a1[1][0]=="X":
            print("Player 1 is the Winner!")
            return 1
        elif a1[1][0]=="O":
            print("Player 2 is the Winner!")
            return 1
    elif (a1[2][0]==a1[2][1]==a1[2][2] != " "):
        if a1[2][0]=="X":
            print("Player 1 is the Winner!")
            return 1
        elif a1[2][0]=="O":
            print("Player 2 is the Winner!")
            return 1
    elif (a1[0][0]==a1[1][0]==a1[2][0] != " "):
        if a1[0][0]=="X":
            print("Player 1 is the Winner!")
            return 1
        elif a1[0][0]=="O":
            print("Player 2 is the Winner!")
            return 1
    elif (a1[0][1]==a1[1][1]==a1[2][1] != " "):
        if a1[0][1]=="X":
            print("Player 1 is the Winner!")
            return 1
        elif a1[0][1]=="O":
            print("Player 2 is the Winner!")
            return 1
    elif (a1[2][1]==a1[1][2]==a1[2][2] != " "):
        if a1[2][1]=="X":
            print("Player 1 is the Winner!")
            return 1
        elif a1[2][1]=="O":
            print("Player 2 is the Winner!")
            return 1
    return 0
        



def printArray(arr):
    print(arr[0][0] + '|' + arr[0][1] + '|' + arr[0][2])
    print('-+-+-')
    print(arr[1][0] + '|' + arr[1][1] + '|' + arr[1][2])
    print('-+-+-')
    print(arr[2][0] + '|' + arr[2][1] + '|' + arr[2][2])




repeatcheck=0
while repeatcheck==0:
    myarray = [[" "," "," "],[" "," "," "],[" "," "," "]]
    player = int(input("Who is gonna be first? "))
    printArray(myarray)
    out=count=0
    while (player!=1 and player!=2):
        print ("insert either 1 or 2")
        player = int(input("Who is gonna be first? "))

    while out == 0:
        if player==1:
            print ("player 1 enter your position ")
            myarray=playerChoice(myarray,player)
            count += 1
            out=defineOutcome(myarray)
            if count==9:
                print("It's a Tie!")
                out = 1
            player=2
        else:
            print("player 2 enter your position ")
            myarray=playerChoice(myarray,player)
            count += 1
            out=defineOutcome(myarray)
            if out!=1 and count==9:
                print("It's a Tie!")
                out = 1
            player=1
        if out==1:
            repeat = str(input("Would you like to play again? Press Y/y or N/n: "))
            while (repeat!="Y" and repeat!="y" and repeat!="N" and repeat!="n"):
                print ("Invalid Option")
                repeat = str(input("Would you like to play again? Press Y/y or N/n: "))
                if repeat=="Y" or repeat=="y":
                    repeatcheck = 0
                elif repeat == "N" or repeat =="n":
                    repeatcheck = 1

