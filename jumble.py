import random
def jumble():
    print("Hello guys welcome to my game Word  jumble")
    print("You need to guess the word but the letters are mixed up")
    print("You have 3 lives")
    x=["ice","noodles","physic","hamburger","money","keyboard","games","pokemon","computer","monitor"]
    a=3
    y=0
    random.shuffle(x)
    for b in x:
        c= list (b)
        random.shuffle(c)
        c="".join (c)
        y= y+1
        print("round number",y)
        while True:
            print("now guess the word:",c)
            d=input()
            if b==d:
                print("Right , next round")
                break
            else:
                a=a-1
                print("Wrong, now you have",a,"lives left")
            if a==0:
                print("Game over ")
                break
        if a==0:
            break
    if a>0:
        print("YOU WON")