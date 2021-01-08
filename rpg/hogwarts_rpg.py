#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
Hogwarts RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

    'Main Hall': {
        'north': 'Entrance Hall',
        'east': 'Lessons Hallway',
        'west': 'Moving Staircases',
        'upstairs': 'Main Hall Balcony',
        'item': 'wand'
    },
    'Lessons Hallway': {
        'north': 'Charms Hallway',
        'south': 'Divination Courtyard',
        'west': 'Main Hall',
        'southwest': 'Potions Class'
    },
    # For now, the directions of the rooms don't change, but it would be cool to find a way to make it so the stairs
    # move like in the books to change which rooms they go to.
    'Moving Staircases': {
        'east': 'Main Hall',
        'west': 'House Hallway',
        'south': 'Headmaster\'s Office'
    },
    'Entrance Hall': {
        # Continue building
        'south': 'Main Hall'
    },
    'Main Hall Balcany': {
        # Continue building
        'downstairs': 'Main Hall'

    },
    'Charms Hallway': {
        # Continue building
        'south': 'Lessons Hallway'
    },
    'Divination Courtyard': {
        # Continue building
        'north': 'Lessons Hallway'
    },
    'Potions Class': {
        # Continue building
        'northeast': 'Lessons Hallway'
    },
    'House Hallway': {
        'downstairs': 'Slytherin CR',
        'north': 'Ravenclaw Tower',
        'east': 'Moving Staircases',
        'south': 'Hufflepuff CR',
        'west': 'Gryffindor CR',
    },
    'Headmaster\'s Office': {
        # Continue building
    },
    'Slytherin CR': {
        # Continue building
        'upstairs': 'House Hallway'
    },
    'Ravenclaw Tower': {
        'south': 'House Hallway',
        'upstairs': 'Ravenclaw CR'
    },
    'Hufflepuff CR': {
        # Continue building
        'north': 'House Hallway'
    },
    'Gryffindor CR': {
        # Continue building
        'east': 'House Hallway'
    },
    'Ravenclaw CR': {
        'north': 'Ravenclaw Dorm',
        'downstairs': 'Ravenclaw Tower'
    },
    'Ravenclaw Dorm': {
        'south': 'Ravenclaw CR'
    }

}

# start the player in the Hall
currentRoom = 'Main Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # Check if player is attempting to enter dorm room - if so, prompt with riddle
        if currentRoom.split(" ")[1] == "CR" and rooms[currentRoom][move[1]].split(" ")[1] == "Dorm":
            # For now, for simplicity, every room will have the same riddle, but in future can have random
            # riddles or specific ones to each house
            print("""
In order to enter the house dorm, you must first answer this riddle. 
Answer correctly and you may enter. 
Answer incorrectly and face the consequences.
            """)
            print('''
            I'm often very stern,
            I wear my hair up in a bun,
            I'm really very fair,
            I find Quidditch very fun.
            Who am I?
Enter "A" for Albus Dumbledore - 
"B" for Harry Potter - 
"C" for Hermione Granger - 
"D" for Minerva McGonagall
            ''')
            answer = input(">").strip().upper()

            if answer == "D":
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print("""
You have been caught by Professor Minerva McGonagall for trying to sneak into another houses dorm!
She takes you directly to the Headmaster's Office!
                """)
                currentRoom = "Headmaster\'s Office"
        # check that they are allowed wherever they want to go
        elif move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

