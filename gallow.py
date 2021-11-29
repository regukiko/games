import random
def gallow():
    print("welcome to my own game named gallows")
    print("you need to write a letter and guess the word")
    print("you can only do 11 mistakes")
    a=0
    x=["ice","noodles","physic","hamburger","money","keyboard","games","pokemon","computer","monitor"]
    random.shuffle(x)
    y=0
    for b in x:
        c="_"*len (b)
        y= y+1
        print("round number",y)
        while True:
            print(c)
            print("write a letter ")
            d=(input())
            if d in b:
                for e in range (len(b)):
                    if b [e] == d:
                        c=c[:e]+d+c[e+1:]
            else:
                a=a+1
                if a == 1:
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                elif a == 2:
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("______")
                elif a == 3:
                    print("____________")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("______")
                elif a == 4:
                    print("____________")
                    print("| /")
                    print("|/")
                    print("|")
                    print("|")
                    print("|")
                    print("______")
                elif a == 5:
                    print("____________")
                    print("| /        |")
                    print("|/")
                    print("|")
                    print("|")
                    print("|")
                    print("______")
                elif a == 6:
                    print("____________")
                    print("| /        |")
                    print("|/         o")
                    print("|")
                    print("|")
                    print("|")
                    print("______")
                elif a == 7:
                    print("____________")
                    print("| /        |")
                    print("|/         o")
                    print("|          O")
                    print("|")
                    print("|")
                    print("______")
                elif a == 8:
                    print("____________")
                    print("| /        |")
                    print("|/         o")
                    print("|        /( )")
                    print("|")
                    print("|")
                    print("______")
                elif a == 9:
                    print("____________")
                    print("| /        |")
                    print("|/         o")
                    print("|        /( )\\")
                    print("|")
                    print("|")
                    print("______")
                elif a == 10:
                    print("____________")
                    print("| /        |")
                    print("|/         o")
                    print("|        /( )\\")
                    print("|         /")
                    print("|")
                    print("______")
                elif a == 11:
                    print("____________")
                    print("| /        |")
                    print("|/         o")
                    print("|        /( )\\")
                    print("|         / \\")
                    print("|")
                    print("______")
            if a==11:
               print("You lose")
               break
            if c.count("_")==0:
                print("You won now your in next round")
                break
        if a ==11:
            break