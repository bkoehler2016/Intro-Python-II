from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('Our-Mountain_v003_Looping.wav')
mixer.music.play(-1)
mixer.music.set_volume(0.2)

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

#
# Main
# Add Items
room['outside'].items.append(Item('Sword', 'used to slice up enemies'))
room['foyer'].items.append(Item('Bow', 'used to shoot enemies from afar'))
room['treasure'].items.append(Item('Gold Coin', 'some loot left behind'))

# print('outside south:', room['outside'].n_to) # NOTE Valid
# print('outside south:', room['outside'].s_to) # NOTE Will give error

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
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
print(player.room)

lastRoom = player.room

#Game Loop
while 1:
    command = input()
    if command.find(' ') != -1:
        player.modifyItem(command)
    else:
        player.changeRoom(command)
        if lastRoom != player.room:
            print(player.room)
        lastRoom = player.room 