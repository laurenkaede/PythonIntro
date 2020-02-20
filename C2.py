def challenge_dining_room():
    welcome = ['An important survival skill is knowing how to light a fire.',
               'Fire provides warmth, light, protection from predators and a psychological boost.',
               'Which of the following items could be used to start a fire in a survival situation?'
               ]

    for line in welcome:
        print(line, sep='\n')

    quiz_options = [
        "1. Flint and Steel",
        "2. Bow and Drill",
        "3. Ammunition",
        "4. All of these"
    ]

    for answers in quiz_options:   
        print(answers)
    answer = input()

    if answer == "4" or answer == "4.":
        print("Congratulations, you have unlocked the " + Fore.MAGENTA + "Batteries!")
        searched_dining_room() 
    else:
        print("Your answer is incorrect, please try again")
        challenge_dining_room()

challenge_dining_room()
