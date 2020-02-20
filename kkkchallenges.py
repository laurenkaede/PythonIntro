import colorama
from colorama import Fore, Style, init
init(autoreset=True)
import time

#-------------------------------------------------------------------------------------------------------------#
# Challenge 1: Lounge/Medical Pack

def challenge_one(): 
    print(Fore.MAGENTA + "If you drop me, I'm sure to crack. Give me a smile, and I'll always smile back.")
    response = input("What am I? > ")
    if response == "A Mirror" or response == "a mirror" or response == "mirror" or response == "A mirror" or response == "a Mirror" or response == "Mirror":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Medical Pack!")
        searched_lounge()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 2: Dining Room/Water Purification Tablets
def challenge_two(): 
    print(Fore.MAGENTA + "What five-letter word becomes shorter when you add two letters to it?.")
    response = input("What's your answer? > ")
    if response == "Short" or response == "short":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Water Purification Tablets!")
        searched_dining_room()                    
    else:
        print("Your answer is incorrect, please try again")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 3: Kitchen/Food 

def challenge_three(): 
        print(Fore.MAGENTA + "The person who makes it has no need for it. The person who purchases it does not use it. The person who does use it does not know he or she is.")
        response = input("What is it? > ")
        if response == "A Coffin" or response == "a coffin" or response == "coffin" or response == "A coffin" or response == "a Coffin" or response == "Coffin":
            print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Food!")
            searched_kitchen()
        else:
            print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 4: Kitchen/Cooking Equipment

def challenge_four(): 
    print(Fore.MAGENTA + "What has an eye but cannot see?")
    response = input("What's your answer? > ")
    if response == "A Needle" or response == "a needle" or response == "needle" or response == "A needle" or response == "a Needle" or response == "Needle":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Cooking Equipment!")
        searched_kitchen()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 5: Garden/Water

def challenge_five(): 
    print(Fore.MAGENTA + "The more you take, the more you leave behind.")
    response = input("What am I? > ")
    if response == "Footprints" or response == "footprints":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Water!")
        searched_garden()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 6: Garage/Matches + Fuel

def challenge_six(): 
    print(Fore.MAGENTA + "What has many keys, but can't open a door?")
    response = input("What's your answer? > ")
    if response == "A Piano" or response == "a piano" or response == "piano" or response == "A piano" or response == "a Piano" or response == "Piano":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Matches & Fuel!")
        searched_garage()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 7: Bedroom/Clothing

def challenge_seven(): 
    print(Fore.MAGENTA + "Poor people have it. Rich people need it. If you eat it you die.")
    response = input("What is it? > ")
    if response == "Nothing" or response == "nothing":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Clothing!")
        searched_bedroom()
    else:
        print("Your answer is incorrect, please try again.")
            
#-------------------------------------------------------------------------------------------------------------#
# Challenge 8: Bathroom/Radiation Therapy Kit

def challenge_eight(): 
    print(Fore.MAGENTA + "What travels around the world, but stays in one spot?")
    response = input("What's your answer? > ")
    if response == "A Stamp" or response == "a stamp" or response == "stamp" or response == "A stamp" or response == "a Stamp" or response == "Stamp":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Radiation Therapy Kit!")
        searched_bathroom()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 9: Outside/Radio

def challenge_nine(): 
    print(Fore.MAGENTA + "I'm a God, a planet and a measurer of heat.")
    response = input("What am I? > ")
    if response == "Mercury" or response == "mercury":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Radio!")
        searched_outside()
    else:
        print("Your answer is incorrect, please try again.")

#-------------------------------------------------------------------------------------------------------------#
# Challenge 10: Garage/Weaponry

def challenge_ten(): 
    print(Fore.MAGENTA + "What is (5 x 62) + (75 x 12)?")
    response = input("What's your answer? > ")
    if response == 1210:
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Weapon!")
        searched_garage()
    else:
        print("Your answer is incorrect, please try again.")
        
#-------------------------------------------------------------------------------------------------------------#