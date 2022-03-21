import random
def menu():
    print("1.Play")
    print("2.Help")
    print("3.Quit")
def help():
    print("To move your character use a or d")
    print("E=enemy")
    print("to show hero´s characteristics press h")
    print("G=gold")
    print("H=hero")
    print("B=bandages")
def play():
    print("write the name of your hero")
    a=input()
    level=0
    hero={"name":a,"position":0,"health":100,"power":50,"intelligent":200,"gold":0,"accuracy":70,"dexterity":90}
    board=[
        [".", ".", "B", ".", ".", "G", "E"],
        [".","B","G","E",".","G",".",".","E"],
        [".","G",".",".",".","E"],
        [".","E",".","G",".","B","E"],
        [".","G,","E",".",".","B",".",".","E","E"]
    ]
    enemies=[ {"name": "pirate", "health": 100 , "power": 55, "intelligent": 50,"accuracy":100,"dexterity":50},
              {"name": "jack", "health": 75, "power": 65, "intelligent": 100, "accuracy": 95, "dexterity": 25},
              {"name": "moscol", "health": 200, "power": 30, "intelligent": 25, "accuracy": 50, "dexterity": 15},
              {"name": "ash", "health": 125, "power": 55, "intelligent": 50, "accuracy": 100, "dexterity": 50},
              {"name": "senar", "health": 135, "power": 60, "intelligent": 150, "accuracy": 100, "dexterity": 98},
              {"name": "ploner", "health": 60, "power": 70, "intelligent": 10, "accuracy": 85, "dexterity": 75},
              {"name": "xploypher", "health": 200, "power": 50, "intelligent": 55, "accuracy": 65, "dexterity": 75},
              {"name": "patrick", "health": 75, "power": 30, "intelligent": 245, "accuracy": 75, "dexterity": 100},
              {"name": "mohler", "health": 200, "power": 45, "intelligent": 55, "accuracy": 100, "dexterity": 25},
              {"name": "repart", "health": 145, "power": 65, "intelligent": 165, "accuracy": 50, "dexterity": 25},
    ]
    show_hero(hero)
    d=board[level][:]
    d[hero["position"]] = "H"
    while True:
        print(*d)
        print("make a turn")
        f=input()
        if f.upper()=="A":
            if hero["position"]>0:
                d[hero["position"]]="."
                hero["position"]-=1
        if f.upper()=="D":
            d[hero["position"]] = "."
            hero["position"] +=1
        if d[hero["position"]]=="G":
            print("You found the Gold")
            hero["gold"]+=1
        if f.upper()=="H":
            show_hero(hero)
        if d[hero["position"]]=="E":
            enemy  = enemies.pop(random.randint(0,len(enemies)-1))
            hero, enemy=fight_with_enemy(hero,enemy)
            if enemy["health"]<=0:
                print("you have killed the enemy")
            elif hero["health"]<=0:
                print("the enemy has killed you")
                break
        if d[hero["position"]]=="B":
            print("You found a Bandage")
            c=min(100-hero["health"],25)
            hero["health"]+=c
            print("You got ",c,"hp")
            print("You have now ",hero["health"],"hp")
        d[hero["position"]] = "H"
        if hero["position"]==len(d)-1:
            level+=1
            hero["health"]=100
            print("Now you are in level", level+1)
            hero["position"]=0
            d = board[level][:]
            d[hero["position"]] = "H"
def fight_with_enemy(hero,enemy):
    print("You found the enemy")
    while True:
        show_hero(enemy)
        print("If you want to attack press e")
        print("if you want to combine attack and intelligent press ef")
        print("if you want to leave the fight press l")
        gold=0
        if hero["intelligent"]> enemy["intelligent"]:
            p=hero["intelligent"]-enemy["intelligent"]
            l=random.randint(1,p//15)
            gold=max(1,10//l)
            print("You can pay",gold,"gold to escape")
        g = input()
        if g.upper() == "E":
            chance=hero["accuracy"]*2-enemy["dexterity"]
            damage=hero["power"]*random.randint(0,chance)//100
            enemy["health"]-=damage
            print("you hitted the enemy",damage)
        if g.upper() == "EF":
            chance=hero["intelligent"]- enemy["intelligent"]
            damage=hero["power"]*random.randint(0,max(chance,0))//100
            enemy["health"]-=damage
            print("you hitted the enemy",damage)
        if g.upper() == "L":
            if hero["gold"]>=gold and hero["intelligent"]> enemy["intelligent"]:
                hero["gold"]-=gold
                print("you left the fight")
                break
            else:
                print("you dont have enough gold to escape")
        chance = enemy["accuracy"]*2- hero["dexterity"]
        damage = enemy["power"] * random.randint(chance//10 , chance) // 100
        hero["health"] -= damage
        print("the enemy hitted you", damage)
        if hero["health"]<0 or enemy["health"]<0:
            break
    return hero,enemy
def game():
    while True:
        menu()
        print("choose a item")
        b=input()
        if b=="1":
            play()
        if b=="2":
            help()
        if b=="3":
            break
def show_hero(hero):
    for key,value in hero.items():
        print(key,value)