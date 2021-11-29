import random
def stone():
    print("willkommen zur stein pape oder scheere")
    g=0
    h=0
    j=0
    while True:
        print("1.play")
        print("2.reference")
        print("3.about")
        print("4.quit")
        print("5.results")
        n=int(input())
        if  n==1:
            g = int(input("dein zug "))
            a = random.randint(1, 3)
            if a == 1:
                print("der zug von den computer ist stein")
            if a == 2:
                print("der hat scheere gewählt")
            if a == 3:
                print("papier wurde gewählt")
            if a == 1 and g == 2:
                print("computer ist der gewinner")
                h=h+1
            if a == 1 and g == 3:
                print("DU BIST DER GEWINNER")
                g=g+1
            if a == 2 and g == 1:
                print("Du bist der GEWINNER")
                g=g+1
            if a == 2 and g == 3:
                print("computer gewinnt")
                h=h+1
            if a == 3 and g == 1:
                print("computer sind besser als du")
                h=h+1
            if a == 3 and g == 2:
                print("du gewinnst")
                g=g+1
            if a == g:
                print("keiner hat gewonnen")
                j=j+1
        elif n==2:
            print("wenn sie stein sein wollen dann drücken sie 1!")
            print("wenn sie scheere sein wollen drücken sie 2!")
            print("wenn sie pape sein wollen drücken sie 3!")
        elif n==3:
            print("made by alex")
        elif n==4:
            break
        elif n==5:
            print("anzahl an gewinns",g)
            print("anzahl wie oft du verloren hast",h)
            print("anzahl wie oft keiner gewonnen hat",j)
        else:
            print("irgendwas stimmt nicht")



