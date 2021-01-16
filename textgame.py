#this is a text based game
#once the game starts you are expected to input your username 
#you will be asked to makee choices during this game
import time
goblin=0
hp=100
hp2=30
attackpower =10
attackpower2 = 2
health2 ="+2 per hour"
health = "+2 per minute"
Rewards="Level up ,new skills"
def question():#function for question
    print("what will you do\n1.attack\n2.defend\n3.run like the wind")
#functions for options
def one():
    goblinstatus["Hp"]=goblinstatus["Hp"]-statusbar["attack power"]
    statusbar["Hp"]=statusbar["Hp"]-goblinstatus["attack power"]
    print ("you have  attacked the goblin\nthe goblin loses 10hp\nyou lose 2hp\nthe goblins hp is",goblinstatus["Hp"],"\n you hp is",statusbar["Hp"])
def two():
    print("you defended the goblins attack")
def three():
    print("you could not run fast enough \nthe goblins ganged up on you")
    #status bar
statusbar={"Hp":hp, 
       "attack power":attackpower,
       "Health" : health,
       "Title" : "transmigrated trash",
       "Skils" : "Warrior strength",
       "Tasks" : "Kill the demon lord",
       "Rewards" : Rewards }

#goblin status bar
goblinstatus={"Hp":hp2, 
       "attack power":attackpower2,
       "Health" : health2,
       "Title" : "regular goblin",
       "Skils" : "gob gob" }
def intro():
    player=input("enter you username: ")#code to enter username
    print("player transmigrates into riverndale\nwelcome  adventurer",player,"to riverndale")
def introstory():
    print("We summoned you here to ask for you help\nThe demon lord has resurrected\nand his underlings have been terrorising the citizens of riverndale ")
intro()
time.sleep(1)
introstory()
time.sleep(1)
quest = input("take the quest (y/n)>> ")
if quest.lower() == "y":
    print("because you are a transmigrated human,you can see status bar and check your stats")
    query = input("type statusbar>>")
    if query.lower()=="statusbar":
        print(statusbar)
else:
    intro()
def queststory():
    print("Town lord:the goblins are at the borders of riverndale,dear adventurer save us\n"
"Town lord:please accept our gift ")
time.sleep(1)
queststory()
newbieset=input("the city lord offers you your newbies set ....\n will you accept yes/no>>  ")
if newbieset.lower() == "yes":
    print("......you start walking towards the border in your newbie set\n you have encountered a goblin \n","GOBLIN STATS",goblinstatus)
    print("you have encountered a goblin")
    question()
    queinp=int(input())
    if queinp==1:
        one()
        print(statusbar)
        time.sleep(1)
        print(goblinstatus)
        question()
        que1=int(input("<<<"))
        if que1==1:
            one()
            print(statusbar)
            time.sleep(1)
            print(goblinstatus)
            question()
            que2=int(input("<<<"))
            if que2==1:
                one()
                print(statusbar)
                time.sleep(1)
                print(goblinstatus)
                print("you have killed the goblin,\nLEVEL UP,\n Quest reward\n......New skill,\nWARRIOR STRENGTH")
            elif que2==2:
                two()
                print("the shield is not strong enough\nthe shield has only one more tries")
                question()
                que_2=int(input("<<<"))
                if que_2==1:
                    one()
                    print(statusbar)
                    time.sleep(1)
                    print(goblinstatus)
                    print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                elif que_2==2:
                    two()
                    print("the shield is not strong enough\nthe shield has no more tries")
                    question()
                    que__2=int(input("<<<"))
                    if que__2==1:
                        one()
                        print(statusbar)
                        time.sleep(1)
                        print(goblinstatus)
                        print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                    elif que__2==2:
                        print("the shield couldnt hold up\n you died \n task failed")
                    elif que__2==3:
                        print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")
                elif que_2==3:
                    print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")
            elif que2==3:
                three()        
        elif que1==2:
            two()
            print("the shield is not strong enough\nthe shield has only one more tries")
            question()
            que_1=int(input("<<<"))
            if que_1==1:
                one()
                print(statusbar)
                time.sleep(1)
                print(goblinstatus)
                question()
                que11=input(int("<<<"))
                if que11==1:
                    one()
                    print(statusbar)
                    time.sleep(1)
                    print(goblinstatus)
                    print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                elif que11==2:
                    two()
                    print("the shield is not strong enough\nthe shield has no more tries")
                    question()
                    que12=input(int("<<<"))
                    if que12==1:
                        one()
                        print(statusbar)
                        time.sleep(1)
                        print(goblinstatus)
                        print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                    elif que12==2:
                        print("the shield couldnt hold up\n you died \n task failed")
                    elif que12==3:
                        print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")        
                elif que11==3:
                    print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")   
            elif que_1==2:
                two()
                print("the shield is not strong enough\nthe shield has no more tries")
                question()
                que__1=input(int("<<<"))
                if que__1==1:
                    one()
                    print(statusbar)
                    time.sleep(1)
                    print(goblinstatus)
                    que_11=input(int("<<<"))
                    if que_11==1:
                        one()
                        print(statusbar)
                        time.sleep(1)
                        print(goblinstatus)
                        print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                    elif que_11==2:
                        print("the shield couldnt hold up\n you died \n task failed")
                    elif que_11==3:
                        print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")        
                elif que__1==2:
                    print("the shield couldnt hold up\n you died \n task failed")
                elif que__1==3:
                    three()
            elif que_1==3:
                three()               
        elif que1==3:
            three()
    elif queinp==2:
        two()
        print("the shield is not strong enough\nthe shield has only one more try")
        question()
        queinp_2=int(input("<<<"))
        if queinp_2==1:
            one()
            print(statusbar)
            time.sleep(1)
            print(goblinstatus)
            question()
            queinp11=int(input("<<<"))
            if queinp11==1:
                one()
                print(statusbar)
                time.sleep(1)
                print(goblinstatus)
                question()
                queinp_11=int(input("<<<"))
                if queinp_11==1:
                    one()
                    print(statusbar)
                    time.sleep(1)
                    print(goblinstatus)
                    print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                elif queinp_11==2:
                    two()
                    print("the shield is not strong enough\nthe shield has only no more tries")
                    question()
                    queinp12 =int(input("<<<"))
                    if queinp12==1:
                        one()
                        print(statusbar)
                        time.sleep(1)
                        print(goblinstatus)
                        print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                    elif queinp12==2:
                        two()
                        print("the shield couldnt hold up\n you died \n task failed")
                    elif queinp12==3:
                        print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")
                elif queinp_11==3:
                    print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")
            elif queinp11==2:
                two()
                print("the shield is not strong enough\nthe shield has no more tries")
                question()
                queinp13=int(input("<<<"))
                if queinp13==1:
                    one()
                    print(statusbar)
                    time.sleep(1)
                    print(goblinstatus)
                    question()
                    queinp_13=int(input("<<<"))
                    if queinp_13==1:
                        one()
                        print(statusbar)
                        time.sleep(1)
                        print(goblinstatus)
                        print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                    elif queinp_13==2:
                        two()
                        print("the shield couldnt hold up\n you died \n task failed")
                    elif queinp_13==3:
                        print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")
                elif queinp13==2:
                    two()
                    print("the shield couldnt hold up\n you died \n task failed")
                elif queinp13==3:
                    three()        
            elif queinp11==3:
                three()
        elif queinp_2==2:
            two()
            print("the shield is not strong enough\nthe shield has no more tries")
            question()
            queinp14=int(input("<<<"))
            if queinp14==1:
                one()
                print(statusbar)
                time.sleep(1)
                print(goblinstatus)
                question()
                queinp_14=int(input("<<<"))
                if queinp_14==1:
                    one()
                    print(statusbar)
                    time.sleep(1)
                    print(goblinstatus)
                    question()
                    queinp__14=int(input("<<<"))
                    if queinp__14==1:
                        one()
                        print(statusbar)
                        time.sleep(1)
                        print(goblinstatus)
                        print("you have killed the goblin,\nLEVEL UP,\n Task reward\n......New skill,\nWARRIOR STRENGTH")
                    elif queinp__14==2:
                        two()
                        print("the shield couldnt hold up\n you died \n task failed")
                    elif queinp__14==3:
                        print("you managed to escape,\nbut the goblin went to alert the other goblins so you died")
                elif queinp_14==2:
                    two()
                    print("the shield couldnt hold up\n you died \n task failed")
                elif queinp_14==3:
                    three()
            elif queinp14==2:
                two()
                print("the shield couldnt hold up\n you died \n task failed")
            elif queinp14==3:
                three()    
    elif queinp==3:
        three()    
        
            

else:
    print("you walk towards the borders without a newbies set ,\n you died of hypothermia on the way")
