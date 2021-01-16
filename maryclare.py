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
Rewards="Level up\nnew skills"
def question():#function for question
    print("what will you do\n1.attack\n2.defend\n3.run like the wind")
#functions for options
def one():
    print ("you have  attacked the goblin\nthe goblin loses 10hp\nyou lose 2hp\nthe goblins hp is",goblinstatus["Hp"]-statusbar["attackpower"],"\n you hp is",statusbar["Hp"]-goblinstatus["attackpower"])
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
    print("player transmigrates into riverndale\nwelcome to adventurer",player,"to riverndale")
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
    print("......you start walking toward =s the border in your newbie set\n you have encountered a goblin \n","GOBLIN STATS",goblinstatus)
    print("you have encountered a goblin")
    question()
    queinp=int(input())
    if queinp==2:
        two()
            

else:
    print("you walk towards the borders without a newbies set ,\n you died of hypothermia on the way")

