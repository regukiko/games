
import random
menu1 = "1. play with friends"
menu2 = "2. play with a bot"
menu3 = "3. help"
menu4 = "4. change language"
menu5 = "5. leave"
help1 = "to make a move input the number of the cell from 1 to 9 "
help2 = "to win you must either put 3 circles or crosses in a row"
play1 = "1.PLayer write your nickname"
play2 = "2.Player write your nickname"
play3="Player: "
play4="wins"
play5="nobody wins"
play6="error write it again"
play7="computer"
def menu():
    global menu1,menu2,menu3,menu4,menu5,help1,help2,play1,play2
    print(menu1)
    print(menu2)
    print(menu3)
    print(menu4)
    print(menu5)
def help():
    global menu1,menu2,menu3,menu4,menu5,help1,help2,play1,play2
    print(help1)
    print(help2)
    print("_1_|_2_|_3_")
    print("_4_|_5_|_6_")
    print("_7_|_8_|_9_")
def show(b):
    print(f"_{b[0]}_|_{b[1]}_|_{b[2]}_")
    print(f"_{b[3]}_|_{b[4]}_|_{b[5]}_")
    print(f"_{b[6]}_|_{b[7]}_|_{b[8]}_")
def play():
    global menu1,menu2,menu3,menu4,menu5,help1,help2,play1,play2
    b=[" "," "," "," "," "," "," "," "," "]
    print(play1)
    player1=input()
    print(play2)
    player2=input()
    show(b)
    if random.randint(0,1)==0:
        players=[player1,player2]
    else:
        players=[player1,player2]
    print("X",players[0])
    print("O",players[1])
    move=0
    xo=["X","0"]
    while True:
        print(play3,players[move])
        a=check(b)
        b[a]=xo[move]
        show (b)
        a=winner(b)
        if a=="w":
            print(players[move],play4)
            break
        elif a=="d":
            print(play5)
            break
        if move==0:
            move=1
        else:
            move=0
def check(b):
    global menu1,menu2,menu3,menu4,menu5,help1,help2,play1,play2
    a=int(input())-1
    while  a<0 or a>8 or  b[a]!=" ":
        print(play6)
        a = int(input()) - 1
    return a
def play_bot():
    global menu1,menu2,menu3,menu4,menu5,help1,help2,play1,play2
    b=[" "," "," "," "," "," "," "," "," "]
    print(play1)
    player1=input()
    print(play2)
    player2=play7
    show(b)
    if random.randint(0,1)==0:
        players=[player1,player2]
    else:
        players=[player1,player2]
    print("X",players[0])
    print("O",players[1])
    move=0
    xo=["X","0"]
    while True:
        print(play3,players[move])
        if players[move]!=play7:
            a=check(b)
        else:
            a=bot(b,xo[move])
        b[a]=xo[move]
        show (b)
        a=winner(b)
        if a=="w":
            print(players[move],play4)
            break
        elif a=="d":
            print(play5)
            break
        if move==0:
            move=1
        else:
            move=0
def language(p):
    global menu1,menu2,menu3,menu4,menu5,help1,help2,play1,play2,play3,play4,play5,play6,play7
    if p==1:
        menu1="1. play with friends"
        menu2="2. play with a bot"
        menu3="3. help"
        menu4="4. change language"
        menu5="5. leave"
        help1="to make a move input the number of the cell from 1 to 9 "
        help2="to win you must either put 3 circles or crosses in a row"
        play1="1.PLayer write your nickname"
        play2="2.Player write your nickname"
        play3="Player: "
        play4="wins"
        play5="nobody wins"
        play6="error write it again"
        play7="computer"
    elif p==2:
        menu1="1. mit freunden spielen"
        menu2="2. mit einem Bot spielen"
        menu3="3. hilfe"
        menu4="4.sprache wechseln"
        menu5="5. verlassen"
        help1=" wählen sie eine zahl von 1 bis 9 "
        help2=" um zu gewinnen musst du entweder in eine zaile"
        play1="1. Spieler schreiben sie ihren spiel namen"
        play2="2. Spieler schreiben sie ihren spiel namen"
        play3="Spieler: "
        play4="gewinnt"
        play5="keiner gewinnt"
        play6="fehler schreiben sie es nochmal"
        play7="computer"
def bot(b,xo):
    for i in range(9):
        if b[i]==" ":
            b[i]=xo
            if winner(b)=="w":
                b[i]=" "
                return i
            b[i]=" "
    if xo=="X":
        ox="O"
    else:
        ox="X"
    for i in range(9):
        if b[i] == " ":
            b[i] = ox
            if winner(b) == "w":
                 b[i] = " "
                 return i
            b[i] = " "
    if b[5]==" ":
        return 5
    a=[1,3,5,7,0,2,6,8]
    for i in a :
        if b[i] == " ":
            return i
def game():
    while True:
       menu()
       a=input()
       if a=="1":
          play()
       if a=="2":
           play_bot()
       if a=="3":
           help()
       if a=="4":
           p=int(input("1-english,2-deutsch"))
           language(p)
       if a=="5":
           break
def winner(b):
    if b[0]==b[1]==b[2]!=" " or b[3]==b[4]==b[5]!=" " or b[6]==b[7]==b[8]!=" " or b[0]==b[3]==b[6]!=" " or b[1]==b[4]==b[7]!=" " or b[2]==b[5]==b[8]!=" " or b[0]==b[4]==b[8]!=" " or b[2]==b[4]==b[6]!=" ":
        return"w"
    if b[0]!=" " and b[1]!=" " and b[2]!=" " and b[3]!=" " and b[4]!=" " and b[5]!=" " and b[6]!=" " and b[7]!=" "and b[8]!=" ":
        return "d"
    return "n"