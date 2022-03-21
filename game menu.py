import random
import jumble
import gallow
import stone
import number
import stones_100
import hero_adventure
while True:
    print("1.Word jumble")
    print("2.Gallow")
    print("3.Stone Paper..")
    print("4.Guess the number")
    print("5.Stones")
    print("6.Hero Adventure")
    print("7.Leave")
    a=input()
    if a=="1":
        jumble.jumble()
    elif a=="2":
        gallow.gallow()
    elif a=="3":
        stone.stone()
    elif a=="4":
        number.number()
    elif a=="5":
        language=input("english-deutsch")
        stones_100.play(language)
    elif a=="6":
        hero_adventure.game()
    elif a=="7":
        break
