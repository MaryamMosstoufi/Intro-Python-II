from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Declare items in each room
room["outside"].items.append(Item("item1 Name", "item1 Description"))
room["foyer"].items.append(Item("item2 Name", "item2 Description"))
room["overlook"].items.append(Item("item3 Name", "item3 Description"))
room["narrow"].items.append(Item("item4 Name", "item4 Description"))
room["treasure"].items.append(Item("item5 Name", "item5 Description"))
room["foyer"].items.append(Item("item6 Name", "item6 Description"))
room["narrow"].items.append(Item("item7 Name", "item7 Description"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def room_game():
    print("Welcome To Room Game!")
    current = room['outside']
    player = Player(current)
    playing = True

    while playing:
        print(f"- Your Current Location: {current.name}")
        print(f"- {current.description}")
        if len(current.items) > 0:
            print(f"This room has {len(current.items)} items:")
            current.room_items()
        else:
            print("There are no items in this room.")
        if len(player.holding) > 0:
            player.player_holding()
        else:
            print("You are currently not holding any items.")
        print("----------------------------------------------")
        key = input("What Next? ")

        if key == "n":
            try:
                current = current.n_to
                print(current.name)
            except:
                print("Oops You Hit The Wall. Try Again!")

        elif key == "e":
            try:
                current = current.e_to
                print(current.name)
            except:
                print("Oops You Hit The Wall. Try Again!")

        elif key == "s":
            try:
                current = current.s_to
                print(current.name)
            except:
                print("Oops You Hit The Wall. Try Again!")
        elif key == "w":
            try:
                current = current.w_to
                print(current.name)
            except:
                print("Oops You Hit The Wall. Try Again!")

        elif key == "q":
            print("Thank you for playing!")
            playing = False

        elif key == 'p':
            if len(current.items) == 0:
                print("There are no items to be picked up in this room")
            else:
                for i in current.items:
                    print(
                        f"{i.name} - {i.description}")
                itemkey = input(
                    "Please type the name of the item that you want to pick up: ")
                for i in current.items:
                    try:
                        if itemkey == i.name:
                            player.pick_item(i)
                            current.remove_item(i)
                            print(
                                f"you have picked up {i.name}")

                    except:
                        print('Please enter a valid item name.')

        elif key == 'd':
            if len(player.holding) == 0:
                print("You are not holding any items to drop")
            else:
                for i in player.holding:
                    print(
                        f"{i.name} - {i.description}")
                itemkey = input(
                    "Please type the name of the item that you want to drop off: ")
                for i in player.holding:
                    try:
                        if itemkey == i.name:
                            player.drop_item(i)
                            current.add_item(i)
                            print(
                                f"you have dropped off {i.name}")
                    except:
                        print('Please enter a valid item name.')
        else:
            print('''Please enter a valid command
            N: North
            E: East
            S: South
            W: West
            P: Pick Up Item
            D: Drop Off Item
            Q: Quit
            ''')


room_game()
