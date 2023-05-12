import os #color change 
import winsound #needed for beep
import random

#this function is ment to make sounds 
def printSound():
    print("drip")
    print("drip")
    print("drop")
#a randomized loot dropper
def itemDropper():
    num = random.randrange(1, 100)
    if num < 25:
        inventory[0]="potion"
        print("you got a potion")

    elif num < 50:
        inventory[1]="sock"
        print("you got a sock")
    elif num < 75:
        inventory[2]="coin"
        print("you got a coin")

    else: 
        print("no item dropped")

    print("your inventory:", inventory)
# a random room discription
def roomDiscriptions():
    num = random.randrange(1, 100)
    if num < 25:
        print("you see a huge spider craling on the floor")

    elif num < 50:
        print("you get a weard feeling that someone is watching you ")
    elif num < 75:
        print("you see a gost pass through the wall ")
    elif num < 95:
        print("you see a shadow like figure vanish")

    
inventory = [" "," "," "," "," "]
room =1 
while True:
    print(inventory)
    choice = "potatoes"
    print("welcome to the text based game!you have to escape the dungeon")

    while choice != "quit": #game loop-------------------
        if room == 1: 
            os.system('color 1f')
            choice = input("you wake up in a prisson cell that is falling appart due to old age and war, you look to the right and see a hole in the wall that leeds to another room. you can go east to exit your prison cell and go into the court yard. ")
            if choice == "east": 
                room = 2 
            else: 
                print("I don't understand that.")
        
        elif room == 2:
            itemDropper()
            roomDiscriptions()
            os.system('color 2f')#this changes the color of the text 
            choice = input("you walk into the court yard and notice it is completly deserted, you notice a open door. you can go west and go back to your cell or go south.")
            if choice == "west":
                room == 1
            if choice == "south": 
                room = 3
            else: 
                print("I don't undertsand that.")

        elif room == 3:
            os.system('color 3f')
            print("you see a key on the floor")# one of the items needed to win the game 
            choice = input("you're in room 2, you can go south or north")
            if choice == "key" or choice == "get key":# you can only get the key if the player picks it up 
             print("you put the key in the inventory")
             inventory[3]="key"
            choice = input("you walk into the room and it is the guards brake room it looks abandoned like everyone left very quickly, you noticed there is another door to the right. you can go north an go back to the court yard or go east.")
            if choice == "north":
                room = 2
            if choice == "east": 
                room = 4
            else:
                print("I don't understand that. ")

        elif room == 4:
            print(inventory)
            os.system('color 4f')
            choice = input("you open the roor and walk into a hallway and you can see an exit but then the roof caves in bloking the exit but a hole is made in one of the walls.  you can go west to go back to the guards room or south to enter the hole in the wall.")
            if choice == "west":
                room = 3
            if choice == "south": 
                room = 5
            else:
                print("I don't understand that. ")

        elif room == 5:
            print(inventory)#this shows the players inventory 
            itemDropper()
            roomDiscriptions()
            os.system('color 5f')
            choice = input("you enter the hole in the wall and it turns out to be a chapel, the statue of the god they prated to is iluminated by the sun light that is shining through the hole in the roof, the bairly standing the upper half is lying shatered beside it covered in moss and vines, you see a door that leeds out the chapel.  you can go north and go back to the hall way or west through the door.")
            if choice == "north":
                room = 4
            if choice == "west": 
                room = 6
            else:
                print("I don't understand that. ")

        elif room == 6:
            os.system('color 6f')
            choice = input("you open the door and enter the morgue, the moment you enter the room you are overwelmed by the smell of rooting fleash, you see multiple courpses lying in coffens redy to be bured, you see a door to the left.  you can go north to go back to the chapel or south.")
            if choice == "east":
                room = 5
            if choice == "south": 
                room = 7
            else:
                print("I don't understand that. ") 

        elif room == 7:
            itemDropper()
            roomDiscriptions()
            os.system('color 7f')
            choice = input("you enter the execution room, as you walk in you notice the dried blood where the prisoners are beheaded the room has a very dark atmosphere and makes you feel uneasy, but you see another door.  you can go east to go back to the mourge or south to exit the room.")
            if choice == "east":
                room = 6
            if choice == "south": 
                room = 8
            else:
                print("I don't understand that. ")
        elif room == 8:
            os.system('color 8f')
            roomDiscriptions()
            choice = input("you enter the cellblock, you see all the different cells the ones that hold three people two and even one but all are the same very small like a closet with a very small window being the onlt sourse of light in the cells, as you walk down the hall you see a large metal door that is loocked you need a key to open it.  you can go north or west.")
            if choice == "north":
                room = 7
            if choice == "west": 
                room = 9
            else:
                print("I don't understand that. ")
        
        elif room == 9:
            os.system('color 9f')
            print("you see a glowing sword on a table")# the second item neede to win the game
            choice = input("you're in room 2, you can go south or north")
            if choice == "sword" or choice == "grab sword":# only able to pick up sword if the player wants to 
             print("you put the sword in your inventory")
             inventory[4]="sword"
            choice = input("you enter the armoury, it has every kind of wepon you need swards, speers, bows and arows, crossbows, shelds, you notice a very large and old chest that is looked but you can't find a key in the armoury mayby it is in another room, you find another door.  you can go east to go back to the cellblock or go south to exit the armoury.")
            if choice == "east":
                room = 8
            if choice == "south": 
                
                if inventory[3]=="key":# the player needs the key in order to open the door 
                    print("you unlock the door with the key")
                    room = 10
                    inventory[3]=" "
                
                else:
                    print("the door is locked")
            else:
                print("I don't understand that. ")

        elif room == 10:
            choice = input("you are in a yard that lets you exit the prison. you can go north or you can exit the prison by going south.")
            if choice == "north":
                room = 9
            if choice == "south":
                
                if inventory[4]=="sword":# sword opens the last door and you win
                    print("the sword starts to glow and the door starts to slowly open, YOU WIN!!")
                    print("""     /| ________________\nO|===|* >________________>\n     \|""") # a picture of the sword is shown 
                    break
                
                else:
                    print("the door is locked, and you are trapped in the prison")
            else:
                print("I don't understand that. ")







#end of game loop
    print("Thanks for playing. Goodbye")
