from MUD import *

def movement():
    if playerAction == "n":
        move("n")
    if playerAction == "e":
        move("e")
    if playerAction == "s":
        move("s")
    if playerAction == "w":
        move("w")

#  if order == 'n':
#         if playaaaa.current_room.n_to is None: 
#             print("No, no, no you can not go that way!") 
#         else:
#            playaaaa.current_room = playaaaa.current_room.n_to
#     elif order == 'e':
#         if playaaaa.current_room.e_to is None: 
#             print("No, no, no you can not go that way!") 
#         else:
#            playaaaa.current_room = playaaaa.current_room.e_to
#     elif order == 's':
#         if playaaaa.current_room.s_to is None: 
#             print("No, no, no you can not go that way!") 
#         else:
#            playaaaa.current_room = playaaaa.current_room.s_to
#     elif order == 'w':
#         if playaaaa.current_room.w_to is None: 
#             print("No, no, no you can not go that way!") 
#         else:
#            playaaaa.current_room = playaaaa.current_room.w_to
#     elif order == 'q':
#         print('You are a loser, good byeee!')
#         exit()


# def movement():
#     if playerOne.currentRoom == room['outside'] and playGame.action == "north":
#         playerOne.updateRoom(room['foyer'])
#         playerOne.updatePreviousRoom(room['outside'])
#     elif playerOne.currentRoom == room['foyer'] and playGame.action == "south":
#         playerOne.updateRoom(room['outside'])
#         playerOne.updatePreviousRoom(room['foyer'])
#     elif playerOne.currentRoom == room['foyer'] and playGame.action == "north":
#         playerOne.updateRoom(room['overlook'])
#         playerOne.updatePreviousRoom(room['foyer'])
#     elif playerOne.currentRoom == room['overlook'] and playGame.action == "south":
#         playerOne.updateRoom(room['foyer'])
#         playerOne.updatePreviousRoom(room['overlook'])
#     elif playerOne.currentRoom == room['foyer'] and playGame.action == "east":
#         playerOne.updateRoom(room['narrow'])
#         playerOne.updatePreviousRoom(room['foyer'])
#     elif playerOne.currentRoom == room['narrow'] and playGame.action == "west":
#         playerOne.updateRoom(room['foyer'])
#         playerOne.updatePreviousRoom(room['narrow'])
#     elif playerOne.currentRoom == room['narrow'] and playGame.action == "north":
#         playerOne.updateRoom(room['treasure'])
#         playerOne.updatePreviousRoom(room['narrow'])
#     elif playerOne.currentRoom == room['treasure'] and playGame.action == "south":
#         playerOne.updateRoom(room['narrow'])
#         playerOne.updatePreviousRoom(room['treasure'])
#     else:
#         print("Invalid Input")