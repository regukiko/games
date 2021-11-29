import random
def play():
    print("welcome to my game Stones")
    print("The game is as follows: there is a bunch of 100 stones. Two players take turns\n "
          " In one turn, the player must take from a pile at least one, but not more than 9 stones.\n "
         " The one who takes the last stone is the winner")
    hints = False
    while True:
        print("1. 2 Players")
        print("2. Play with computer")
        print("3. Turn on hints")
        print("4. Help")
        print("5. Quit")
        b=int(input())

        if b==1:
            print("write your name 1")
            player1=input()
            print("write your name 2")
            player2=input()
            v= player1
            Stone= 100
            while Stone>0:
                print("Stone:",Stone)
                print("turn",v)
                if hints==True:
                    t= Stone%10
                    if t>0:
                        print("remove",t,"Stones")
                    else:
                        print("we cant help you")

                r=int(input())
                while r<1 and r>9:
                    print("write a number from 1 to 9")
                    r=int(input())
                Stone=Stone-r
                if player1==v:
                    v=player2
                else:
                    v=player1
            if player1 == v:
                v = player2
            else:
                v = player1
            print("winner is ",v)
        elif b==2:
            print("write your name 1")
            player1 = input()
            player2 = "computer"
            v = player1
            Stone = 100
            while Stone > 0:
                print("Stone:", Stone)
                print("turn", v)
                if v=="computer":
                    t = Stone % 10
                    if t > 0:
                        r=t
                    else:
                        r=random.randint(1,9)
                    Stone=Stone-r
                    print("computer removed",r,"Stones")
                    v=player1
                    continue
                if hints == True and v!="computer":
                    t = Stone % 10
                    if t > 0:
                        print("remove", t, "Stones")
                    else:
                        print("we cant help you")

                r = int(input())
                while r < 1 and r > 9:
                    print("write a number from 1 to 9")
                    r = int(input())
                Stone = Stone - r
                if player1 == v:
                    v = player2
                else:
                    v = player1
            if player1 == v:
                v = player2
            else:
                v = player1
            print("winner is ", v)
        elif b==3:
            if hints== True:
                hints= False
                print("Hints are turned off")
            else:
                hints= True
                print("Hints are turned on")