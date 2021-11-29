import random
import jumble
import gallow
import stone
import number
import stones_100
while True:
    print("1.Word jumble")
    print("2.Gallow")
    print("3.Stone Paper..")
    print("4.Guess the number")
    print("5.Stones")
    print("6.Leave")
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
        stones_100.play()
    elif a=="6":
        break