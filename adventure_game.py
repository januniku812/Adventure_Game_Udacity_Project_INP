import time 
import random
#Word Banks

wordBankscen1=["You wake up to find yourself in a blazing hot desert and with a sword lying by your side.You stand up and see a snake making its way to you.What do you do?","You are in a boat and all around you see a vast ocean all around you and a sword lays on the other end.A cold realization hits you when you see a pack of sharks coming your way!What do you do?","You find yourself in a dark cave with a fire crackling by your side.You see there is a dagger in your pocket.As you look at your surroundings you see bear coming towards you.What do you do?"]

wordchoiceScen1=["(1)stand still and wait for the snake to leave (2)attack the snake with your sword ","(1)try to swim or (2)attack them with your sword ","(1)try to outrun the bear,(2) Attack it"]

#global variables defined as null until reassigned in their respective functions
attackArea=''
waitTime=''
runTime=''
stabPlace=''
secenario=''
startSecenario=int(random.randint(0,2))
relocate=''

def print_pause(message_to_print):
    time.sleep(2)
    print(message_to_print)
    
def restart(relocate):
    relocate=input("Would you like to play this again(yes or no)?")
    if relocate == "yes":
        startSecenario=int(random.randint(0,2))
        play(stabPlace,startSecenario,secenario,waitTime,attackArea)
    elif relocate == "no":
        print_pause("Ok, hope you enjoyed!Bye!")
    else:
        print_pause("Enter a valid input")
        restart(relocate)
    
def fight(stabPlace,relocate):
    stabPlace = input("where are you going to stab it?Enter either heart,face,or eyes.")
    if stabPlace == "heart":
        if startSecenario == 2 or 1:
            print_pause("Good job you defeated the animal!")
            restart(relocate)
        else:
            ("You missed as it slither out of your reach and kills you out of agression!")
    elif stabPlace == "face":
        if startSecenario == 2 or 1:
            print_pause("Good job you defeated the animal!")
            restart(relocate)
        else:
            ("You missed as it slithers out of your reach and kills you out of agression!")
    elif stabPlace == "eyes":
        print_pause("Good job the animal winces out of pain and retreats!")
        restart(relocate)
    else:
        print_pause("enter a vaild input")
        fight(stabPlace,relocate)
            
       
def swimShark(attackArea,relocate):
    attackArea = input("The shark is gaining speed on you! You have to face it where do you attack it?Its eyes or nose?")
    if attackArea == "eyes":
        print_pause("You were able to successfully punch it in its eyes as it blindly try to attack you and easily passby it!")
        print_pause("You won!")
        restart(relocate)
    elif attackArea == "nose":
        print_pause("You were able to affectively get it distracted but then it comes back with more sharks and finsihes you off!")
        restart(relocate)
    else:
        print_pause("enter a vaild input of either eyes or nose please")
        swimShark(attackArea,relocate)
    
def runBear(relocate):
     print_pause("You run as fast as you can but your legs are burning up")
     print_pause("you turn around to face the bear whom leaps up on you as you realise your mistake of aggrivating it by running")
     print_pause("Game over")
     restart(relocate)
def waitSnake(waitTime):
    waitTime=int(input("How many minutes are you gonna stand still before doing something else(enter a number between 1 and 10)?"))
    try:
        if waitTime > 10 or waitTime < 0:
            print_pause("enter a valid input")
            waitSnake(waitTime)
        else:
            if waitTime > 7:
                print_pause("You were able to successfully outwait the snake and it gets bored and leaves you alone.Good job you won !")
                restart(relocate)
            else:
                print_pause("You weren't able to successfully outwait the animal and the snake sinks its fangs into you and finsihes you off!")
                restart(relocate)
    except ValueError:
        print_pause("enter a valid input")
        waitSnake(waitTime)
def intro():
    print_pause(wordBankscen1[startSecenario]) 
    print_pause(wordchoiceScen1[startSecenario]) 
def flight(startSecenario,waitTime,attackArea,relocate): 
    if startSecenario == 0: 
        waitSnake(waitTime)
    
    elif startSecenario == 1:
        swimShark(attackArea,relocate)
    
    elif startSecenario == 2:
        runBear(relocate)

def layout(): 
    secenario = str(input("which one do you choose(please enter 1 or 2)?"))
    if  secenario == "2":
        fight(stabPlace,relocate)
    elif secenario == "1":
        flight(startSecenario,waitTime,attackArea,relocate)
    elif secenario != "1" or "2":
        print_pause("Please enter a valid input")
        layout()
  
def play(stabPlace,startSecenario,secenario,waitTime,attackArea):
    intro()
    layout() 


play(stabPlace,startSecenario,secenario,waitTime,runTime)
