import colorama
from colorama import Fore, Style, init
init(autoreset=True)
import time

#-------------------------------------------------------------------------------------------------------------#
# Challenge 1: Lounge/Medical Pack

def challenge_lounge(): 
    print(Fore.MAGENTA + "If you drop me, I'm sure to crack. Give me a smile, and I'll always smile back.")
    response = input("What am I? > ")
    if response == "A Mirror" or response == "a mirror" or response == "mirror" or response == "A mirror" or response == "a Mirror" or response == "Mirror":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Medical Pack!")
        searched_lounge()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 2: Dining Room/Water Purification Tablets

def challenge_dining_room(): 
    print(Fore.MAGENTA + "What five-letter word becomes shorter when you add two letters to it?.")
    response = input("What's your answer? > ")
    if response == "Short" or response == "short":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Water Purification Tablets!")
        searched_dining_room()                    
    else:
        print("Your answer is incorrect, please try again")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 3: Kitchen/Food 

def challenge_kitchen_1(): 
        print(Fore.MAGENTA + "The person who makes it has no need for it. The person who purchases it does not use it. The person who does use it does not know he or she is.")
        response = input("What is it? > ")
        if response == "A Coffin" or response == "a coffin" or response == "coffin" or response == "A coffin" or response == "a Coffin" or response == "Coffin":
            print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Food!")
            searched_kitchen()
        else:
            print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 4: Kitchen/Cooking Equipment

def challenge_kitchen_2(): 
    print(Fore.MAGENTA + "What has an eye but cannot see?")
    response = input("What's your answer? > ")
    if response == "A Needle" or response == "a needle" or response == "needle" or response == "A needle" or response == "a Needle" or response == "Needle":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Cooking Equipment!")
        searched_kitchen()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 5: Garden/Water

def challenge_garden(): 
    print(Fore.MAGENTA + "The more you take, the more you leave behind.")
    response = input("What am I? > ")
    if response == "Footprints" or response == "footprints":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Water!")
        searched_garden()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 6: Garage/Matches + Fuel

def challenge_garage_1(): 
    print(Fore.MAGENTA + "What has many keys, but can't open a door?")
    response = input("What's your answer? > ")
    if response == "A Piano" or response == "a piano" or response == "piano" or response == "A piano" or response == "a Piano" or response == "Piano":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Matches & Fuel!")
        searched_garage()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 7: Bedroom/Clothing

def challenge_bedroom(): 
    print(Fore.MAGENTA + "Poor people have it. Rich people need it. If you eat it you die.")
    response = input("What is it? > ")
    if response == "Nothing" or response == "nothing":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Clothing!")
        searched_bedroom()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 8: Bathroom/Radiation Therapy Kit

def challenge_bathroom(): 
    print(Fore.MAGENTA + "What travels around the world, but stays in one spot?")
    response = input("What's your answer? > ")
    if response == "A Stamp" or response == "a stamp" or response == "stamp" or response == "A stamp" or response == "a Stamp" or response == "Stamp":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Radiation Therapy Kit!")
        searched_bathroom()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 9: Outside/Radio

def challenge_outside(): 
    print(Fore.MAGENTA + "I'm a God, a planet and a measurer of heat.")
    response = input("What am I? > ")
    if response == "Mercury" or response == "mercury":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Radio!")
        searched_outside()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 10: Garage/Weaponry

def challenge_garage_2(): 
    print(Fore.MAGENTA + "What is (5 x 62) + (75 x 12)?")
    response = input("What's your answer? > ")
    if response == 1210:
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Weapon!")
        searched_garage()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#

print(Fore.RED + "Welcome to Time Bomb.") 

player_name = input("What's your name? >")
print(Fore.CYAN + "Welcome to the apocalyspe, " + player_name + "! It’s the end of the world... Your time is ticking and you have to make it to your bunker in the garden before you’re obliterated. Collect 10 items along the way to ensure your survival. Happy hunting!") 

input("...are you ready to kick some ass? > ")
print(Fore.CYAN + "You’re lazing around on the sofa, a beer in hand and an apocalyptic survivalist documentary playing. You love this stuff, knowing  it will one day come in handy because the conspiracy theorists are definitely not a bunch of quacks. Suddenly, the TV goes blank and a newscaster appears. “There have been reports of nuclear bombs striking major cities around the world. Your city is next. You have 5 minutes to find a place of safety before…” Static appears on the screen. “Huh, I guess he’s a goner…” You mutter to yourself. “You’ve got this," + player_name + ". Remember your training…”")


def lounge():
    print("You reach under the sofa and grab your list of 'Top 10 Items Needed for Survival'. Gosh, you're so prepared... as you're already in the lounge, would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_lounge'" + Style.RESET_ALL + " for an item?")
    
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    elif response == "search_lounge":
        search_lounge()
    else:
        print("Invalid response")
        lounge()

def searched_lounge():
    print("You have already successfully searched the lounge. Enter" + Fore.BLUE + "'hallway'")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_lounge()

def search_lounge():
    print("Searching lounge...")
    
    print("You've found the " + Fore.MAGENTA + "Medical Pack!")
    
    print(Fore.CYAN + "Uh oh... it seems there's a riddle for you to solve before you can take your item.")
   
    challenge_lounge()
    searched_lounge
lounge()