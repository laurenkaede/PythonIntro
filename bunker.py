# Location - Bunker

def bunker():
    print("You have entered the bunker. Would you like to return to the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'close hatch'")
    response = input("What do you do? > ")
    if response == "hallway":
        hallway()
    if response == "close hatch":
        print("WARNING: once the hatch is closed, you will be here for a while")
        checksum()
    else:
        print("Invalid response")
        bunker()
        





# Location - Garden

def garden():
    print("You have entered the garden. Would you like to enter the " + Fore.BLUE + "'hallway'" + Style.RESET_ALL + " or " + Fore.BLUE + "'search_garden'" + Style.RESET_ALL + " for an item?")
    response = input("What do you do? > ")
    if response == "search_garden" and x == "false":
        search_garden()
    if response == "search_garden" and x == "true":
        print("You have already searched garden.")
        searched_garden()
    elif response == "search_garden":
        search_garden()
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
 