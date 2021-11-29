def number():
    print("wilkommen zu meinem Spiel")
    while True:
        print("1. Spiel starten ")
        print("2. Regeln")
        print("3. Spiel verlassen")
        w=int(input())
        if w==1:
            l = 0
            r = 100
            while True:
                a = l + (r - l) // 2
                print("its deine zahl  ?", a)
                b = int(input())
                if b == 1:
                    r = a
                if b == 2:
                    l = a
                if b == 3:
                    print("DER Copmuter hat DIE ZAHL erraten")
                    break
        if w==2:

            print("wahlen sie eine zahl von 1 bis 99")
            print("der computer wird am ende deine gewalte zahl heraus finden")
            print("wenn deine zahl kleiner als die von computer drücken sie 1")
            print("wenn die zahl von dir größer als die von computer ist drücken sie bitte 2")
            print("wenn computer die zahl erraten hat drücken sie 3")
        if w==3:
            break