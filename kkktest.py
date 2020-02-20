import colorama
from colorama import Fore, Style, init
init(autoreset=True)
#import time

#-------------------------------------------------------------------------------------------------------------#

room_clear = {
    "bathroom": "false",
    "bedroom": "false",
    "outside": "false",
    "dining_room": "false",
    "kitchen": "false",
    "garden": "false",
    "garage": "false",
    "lounge": "false"
    }

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
# Challenge 2: Dining Room/Batteries

def challenge_dining_room(): 
    print(Fore.MAGENTA + "What five-letter word becomes shorter when you add two letters to it?.")
    response = input("What's your answer? > ")
    if response == "Short" or response == "short":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Batteries!")
        searched_dining_room()                    
    else:
        print("Your answer is incorrect, please try again")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 3: Kitchen/Food/Cooking Equipment

def challenge_kitchen(): 
    print(Fore.MAGENTA + "The person who makes it has no need for it. The person who purchases it does not use it. The person who does use it does not know he or she is.")
    response = input("What is it? > ")
    if response == "A Coffin" or response == "a coffin" or response == "coffin" or response == "A coffin" or response == "a Coffin" or response == "Coffin":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Food" + Style.RESET_ALL + " and " + Fore.MAGENTA + "Cooking Equipment!")
        searched_kitchen()
    else:
        print("Your answer is incorrect, please try again.")
        
#-------------------------------------------------------------------------------------------------------------#
# Challenge 4: Garden/Water

def challenge_garden():
    print(Fore.MAGENTA + "The more you take, the more you leave behind.")
    response = input("What am I? > ")
    if response == "Footprints" or response == "footprints":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Water!")
        searched_garden()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 5: Garage/Matches + Fuel/Weapon # Problem with challenge #

def challenge_garage(): 
    print(Fore.MAGENTA + "What is (5 x 62) + (75 x 12)?")
    response = input("What's your answer? > ")
    if response == "1210":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Matches & Fuel" + Style.RESET_ALL + " and " + Fore.MAGENTA + "Weapon!")
        searched_garage()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 6: Bedroom/Clothing

def challenge_bedroom(): 
    print(Fore.MAGENTA + "Poor people have it. Rich people need it. If you eat it you die.")
    response = input("What is it? > ")
    if response == "Nothing" or response == "nothing":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Clothing!")
        searched_bedroom()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 7: Bathroom/Radiation Therapy Kit

def challenge_bathroom(): 
    print(Fore.MAGENTA + "What travels around the world, but stays in one spot?")
    response = input("What's your answer? > ")
    if response == "A Stamp" or response == "a stamp" or response == "stamp" or response == "A stamp" or response == "a Stamp" or response == "Stamp":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Radiation Therapy Kit!")
        searched_bathroom()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 8: Outside/Radio

def challenge_outside(): 
    print(Fore.MAGENTA + "I'm a God, a planet and a measurer of heat.")
    response = input("What am I? > ")
    if response == "Mercury" or response == "mercury":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Radio!")
        searched_outside()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#

print(Fore.RED + "Welcome to Time Bomb.") 

player_name = input("What's your name? >")
print(Fore.CYAN + "Welcome to the apocalyspe, " + player_name + "! It’s the end of the world... Your time is ticking and you have to make it to your bunker in the garden before you’re obliterated. Collect 10 items along the way to ensure your survival. Happy hunting!") 

input("...are you ready to kick some ass? > ")
print(Fore.CYAN + "You’re lazing around on the sofa, a beer in hand and an apocalyptic survivalist documentary playing. You love this stuff, knowing  it will one day come in handy because the conspiracy theorists are definitely not a bunch of quacks. Suddenly, the TV goes blank and a newscaster appears. “There have been reports of nuclear bombs striking major cities around the world. Your city is next. You have 5 minutes to find a place of safety before…” Static appears on the screen. “Huh, I guess he’s a goner…” You mutter to yourself. “You’ve got this," + player_name + ". Remember your training…”")
print("You reach under the sofa and grab your list of 'Top 10 Items Needed for Survival'. Gosh, you're so prepared...")

#-------------------------------------------------------------------------------------------------------------#
# Location - Bunker

def bunker():
    print("You have entered the bunker. Would you like to return to the " + Fore.BLUE + "'garden'" + Style.RESET_ALL + " or " + Fore.BLUE + "'check items'" + Style.RESET_ALL + " needed for survival?")
    response = input("What do you do? > ")
    if response == "garden":
        garden()
    if response == "'check items'":
        print("-show list of items collected (or still needed)-")
        searched_garden()
    else:
        print("Invalid response")
        bunker()

#-------------------------------------------------------------------------------------------------------------#
# Location - Bathroom

def bathroom():
    print("You have entered the bathroom. Would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_bathroom'" + Style.RESET_ALL + " for an item?")
    x = room_clear.get("bathroom")
    response = input("What do you do? > ")
    if response == "search_bathroom" and x == "false":
        search_bathroom()
    if response == "search_bathroom" and x == "true":
        print("You have already searched this room.")
        searched_bathroom()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        bathroom()

def searched_bathroom():
    print("Enter " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "search_bathroom")
    x = room_clear.get("bathroom")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "search_bathroom" and x == "true":
        print("This room has already been searched.")
    else:
        print("Invalid response")
        searched_bathroom()

def search_bathroom():
    print("Searching bathroom...")
    print("You've found the " + Fore.MAGENTA + "Radiation Therapy Kit!")
    print(Fore.CYAN + "Uh oh... it seems there's a riddle for you to solve before you can take your item.")
    room_clear.update({"bathroom": "true"})
    challenge_bathroom()
    searched_bathroom()

#-------------------------------------------------------------------------------------------------------------#
# Location - Bedroom

def bedroom():
    print("You have entered the bedroom. Would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_bedroom'" + Style.RESET_ALL + " for an item?")
    x = room_clear.get("bedroom")
    response = input("What do you do? > ")
    if response == "search_bedroom" and x == "false":
        search_bedroom()
    if response == "search_bedroom" and x == "true":
        print("You have already searched this room.")
        searched_bedroom()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        bedroom()

def searched_bedroom():
    print("Enter " + Fore.BLUE + "hallway" + Style.RESET_ALL + " or " + Fore.BLUE + "search_bedroom")
    x = room_clear.get("bedroom")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "search_bedroom" and x == "true":
        print("This room has already been searched.")
        searched_bedroom()
    else:
        print("Invalid response")
        searched_bedroom()

def search_bedroom():
    print("Searching bedroom...")
    print("You've found the " + Fore.MAGENTA + "Clothing!")
    print(Fore.CYAN + "Uh oh... it seems there's a riddle for you to solve before you can take your item.")
    room_clear.update({"bedroom": "true"})
    challenge_bedroom()
    searched_bedroom()

#-------------------------------------------------------------------------------------------------------------#
# Location - Outside

def outside():
    print("You have entered the outside. Would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_outside'" + Style.RESET_ALL + " for an item?")
    x = room_clear.get("outside")
    response = input("What do you do? > ")
    if response == "search_outside" and x == "false":
        search_outside()
    if response == "search_outside" and x == "true":
        print("You have already searched outside.")
        searched_outside()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        outside()

def searched_outside():
    print("Enter " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "search_outside")
    x = room_clear.get("outside")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "search_outside" and x == "true":
        print("This room has already been searched.")
    else:
        print("Invalid response")
        searched_outside()

def search_outside():
    print("Searching outside...")
    print("You've found the " + Fore.MAGENTA + "Radio!")
    print(Fore.CYAN + "Uh oh... it seems there's a riddle for you to solve before you can take your item.")
    room_clear.update({"outside": "true"})
    challenge_outside()
    searched_outside()

#-------------------------------------------------------------------------------------------------------------#
# Location - Garden

def garden():
    print("You have entered the garden. Would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_garden'" + Style.RESET_ALL + " for an item?")
    x = room_clear.get("garden")
    response = input("What do you do? > ")
    if response == "search_garden" and x == "false":
        search_garden()
    if response == "search_garden" and x == "true":
        print("You have already searched garden.")
        searched_garden()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        garden()

def searched_garden():
    print("Enter " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "search_garden")
    x = room_clear.get("garden")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "search_garden" and x == "true":
        print("This room has already been searched.")
    else:
        print("Invalid response")
        searched_garden()
        
def search_garden():
    print("Searching garden...")
    print("You've found the " + Fore.MAGENTA + "Water!")
    print(Fore.CYAN + "Uh oh... it seems there's a riddle for you to solve before you can take your item.")
    room_clear.update({"garden": "true"})
    challenge_garden()
    searched_garden()

#-------------------------------------------------------------------------------------------------------------#
# Location - Dining Room

def dining_room():
    print("You have entered the Dining Room. Would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_dining_room'" + Style.RESET_ALL + " for an item?")
    x = room_clear.get("dining_room")
    response = input("What do you do? > ")
    if response == "search_dining-room" and x == "false":
        search_dining_room()
    if response == "search_dining_room" and x == "true":
        print("You have already searched outside.")
        searched_dining_room()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        dining_room()

def searched_dining_room():
    print("Enter " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "search_dining_room")
    x = room_clear.get("dining_room")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "search_dining_room" and x == "true":
        print("This place has already been searched.")
        searched_dining_room()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        searched_dining_room()

def search_dining_room():
    print("Searching dining_room...")
    print("You've found the " + Fore.MAGENTA + "Batteries!")
    print(Fore.CYAN + "Uh oh... it seems there's a riddle for you to solve before you can take your item.")
    room_clear.update({"dining_room": "true"})
    challenge_dining_room()
    searched_dining_room()

#-------------------------------------------------------------------------------------------------------------#
# Location - Kitchen

def kitchen():
    print("You have entered the kitchen. Would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_kitchen'" + Style.RESET_ALL + " for an item?")
    x = room_clear.get("kitchen")
    response = input("What do you do? > ")
    if response == "search_kitchen" and x == "false":
        search_kitchen()
    if response == "search_kitchen" and x == "true":
        print("You have already searched this room.")
        searched_kitchen()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        kitchen()

def searched_kitchen():
    print("Enter " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "search_kitchen")
    x = room_clear.get("kitchen")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "search_kitchen" and x == "true":
        print("This room has already been searched.")
        searched_kitchen()
    else:
        print("Invalid response")
        searched_kitchen()

def search_kitchen():
    print("Searching kitchen...")
    print("You've found the " + Fore.MAGENTA + "Food and Cooking Equipment!")
    print(Fore.CYAN + "Uh oh... it seems there's a riddle for you to solve before you can take your item.")
    room_clear.update({"kitchen": "true"})
    challenge_kitchen()
    searched_kitchen()

#-------------------------------------------------------------------------------------------------------------#
# Location - Garage

def garage():
    print("You have entered the garage. Would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_garage'" + Style.RESET_ALL + " for an item?")
    x = room_clear.get("garage")
    response = input("What do you do? > ")
    if response == "search_garage" and x == "false":
        search_garage()
    if response == "search_garage" and x == "true":
        print("You have already searched this room.")
        searched_garage()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        garage()

def searched_garage():
    print("Enter " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "search_garage")
    x = room_clear.get("garage")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "search_garage" and x == "true":
        print("This room has already been searched.")
    else:
        print("Invalid response")
        searched_garage()

def search_garage():
    print("Searching garage...")
    print("You've found the " + Fore.MAGENTA + "Matches/Fuel and Weapon!")
    print(Fore.CYAN + "Uh oh... it seems your items are locked in a safe! Complete the maths challenge to reveal the code.")
    room_clear.update({"garage": "true"})
    challenge_garage()
    searched_garage()

#-------------------------------------------------------------------------------------------------------------#
# Location - Hallway

hallway_rooms = [
    "1. Garage",
    "2. Outside",
    "3. Bathroom",
    "4. Bedroom",
    "5. Dining Room",
    "6. Garden",
    "7. Lounge",
    "8. Kitchen"
]
def room_list_hallway():
    for rooms in hallway_rooms:   
        print(rooms)

def hallway():
    room_list_hallway()
    response = input("What do you do? > ")
    if response == "1" or response == "1.":
        garage()
    elif response == "2" or response == "2.":
        outside()
    elif response == "5" or response == "5.":
        dining_room()
    elif response == "8" or response == "8.":
        kitchen()
    elif response == "3" or response == "3.":
        bathroom()
    elif response == "4" or response == "4.":
        bedroom()
    elif response == "7" or response == "7.":
        lounge()
    elif response == "6" or response == "6.":
        garden()
    else:
        print("Invalid response")
        hallway()

#-------------------------------------------------------------------------------------------------------------#
# Location - Lounge

lounge_rooms = [
    "1. Hallway",
    "2. Search the Lounge"
]
def room_list_lounge():
    for rooms in hallway_rooms:   
        print(rooms)

def lounge():
    room_list_hallway()
    print("You have entered the lounge, would you like to enter: " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_lounge'" + Style.RESET_ALL + " for an item?")
    x = room_clear.get("lounge")
    response = input("What do you do? > ")
    if response == "search_lounge" and x == "false":
        search_lounge()
    if response == "search_lounge" and x == "true":
        print("You have already searched this room.")
        searched_lounge()
    elif response == "hallway":
        hallway()
    else:
        print("Invalid response")
        lounge()
lounge()
def searched_lounge():
    print("Enter " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "search_lounge")
    x = room_clear.get("lounge")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "search_lounge" and x == "true":
        print("This room has already been searched.")
    else:
        print("Invalid response")
        searched_lounge()

def search_lounge():
    print("Searching lounge...")
    print("You've found the " + Fore.MAGENTA + "Medical Pack!")
    print(Fore.CYAN + "Uh oh... it seems there's a riddle for you to solve before you can take your item.")
   
    room_clear.update({"lounge": "true"})
    challenge_lounge()
    searched_lounge
lounge()

#-------------------------------------------------------------------------------------------------------------#