#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def downstairs_hallway():
    print("downstairs_hallway. Enter 'garage', 'outside', 'upstairs_hallway', 'dining_room' or 'kitchen'.")
    response = input("What do you do? ")
    if response == "garage":
        garage()
    elif response == "outside":
        outside()
    elif response == "upstairs_hallway":
        upstairs_hallway()
    elif response == "dining_room":
        dining_room()
    elif response == "kitchen":
        kitchen()
    else:
        print("Invalid response")
        downstairs_hallway()

def search_downstairs_hallway():
    print("Search downstairs_hallway")
    downstairs_hallway()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def garage():
    print("garage. Enter 'garden', 'downstairs_hallway' or 'outside'")
    response = input("What do you do? ")
    if response == "garden":
        garden()
    elif response == "downstairs_hallway":
        downstairs_hallway()
    elif response == "outside":
        outside()
    else:
        print("Invalid response")
        garage()

def search_garage():
    print("Search garage")
    garage()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    

def kitchen():
    print("kitchen. Enter 'downstairs_hallway' or 'dining_room'")
    response = input("What do you do?")
    if response == "downstairs_hallway":
        downstairs_hallway()
    elif response == "dining_room":
        dining_room()
    else:
        print("Invalid response")
        kitchen()

def search_kitchen():
    print("Search kitchen")
    kitchen()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  

def dining_room():
    print("dining_room. Enter 'downstairs_hallway' or 'kitchen'")
    response = input("What do you do?")
    if response == "downstairs_hallway":
        downstairs_hallway()
    elif response == "kitchen":
        kitchen()
    else:
        print("Invalid response")
        dining_room()

def search_dining_room():
    print("Search dining_room")
    dining_room()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def garden():
    print("garden. Enter 'outside', 'downstairs_hallway' or 'bunker'")
    response = input("What do you do?")
    if response == "outside":
        outside()
    elif response == "downstairs_hallway":
        downstairs_hallway()
    elif response == "bunker":
        bunker()
    else:
        print("Invalid response")
        garden()

def search_garden():
    print("Search garden")
    garden()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def outside():
    print("outside. Enter 'garage', 'downstairs_hallway' or 'garden'")
    response = input("What do you do?")
    if response == "garage":
        garage()
    elif response == "downstairs_hallway":
        downstairs_hallway()
    elif response == "garden":
        garden()
    else:
        print("Invalid response")
        outside()

def search_outside():
    print("Search outside")
    outside()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def upstairs_hallway():
    print("upstairs_hallway. Enter 'bedroom' or 'bathroom' or 'downstairs_hallway'?")
    response = input("What do you do? ")
    if response == "bathroom":
        bathroom()
    elif response == "bedroom":
        bedroom()
    elif response == "downstairs_hallway":
        downstairs_hallway()
    else:
        print("Invalid response")
        upstairs_hallway()

def search_upstairs_hallway():
    print("Search upstairs_hallway")
    upstairs_hallway()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def bedroom():
    print("bedroom. Enter 'upstairs_hallway'")
    response = input("What do you do? ")
    if response == "upstairs_hallway":
        upstairs_hallway()
    else:
        print("Invalid response")
        bedroom()

def search_bedroom():
    print("Search bedroom")
    bedroom()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def bathroom():
    print("bathroom. Enter 'upstairs_hallway'")
    response = input("What do you do? ")
    if response == "upstairs_hallway":
        upstairs_hallway()
    else:
        print("Invalid response")
        bathroom()

def search_bathroom():
    print("Search bathroom")
    bathroom()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def lounge():
    print("lounge. Enter 'downstairs_hallway'")
    response = input("What do you do?")
    if response == "downstairs_hallway":
        downstairs_hallway()
    else:
        print("Invalid response")
        lounge()

def search_lounge():
    print("Search lounge")
    lounge()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#