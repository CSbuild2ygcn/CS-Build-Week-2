from MUD import *

def movement(playerAction):
    if playerAction == "n":
        serverResponse = move("n")
        return serverResponse
    if playerAction == "e":
        serverResponse = move("e")
        return serverResponse
    if playerAction == "s":
        serverResponse = move("s")
        return serverResponse
    if playerAction == "w":
        serverResponse = move("w")
        return serverResponse
    else:
        return None

def menuOptions():
    print(f"""
        NSEW to move
        1 - Check inventory
        2 - Pick up treasure
        3 - Drop treasure
        4 - Appraise value of treasure
        5 - Sell treasure
        6 - Equip item
        7 - Unequip item
        8 - Change name
        9 - Pray
        10 - Give to ghost
        11 - Take from ghost
        12 - Get latest proof from Lambda Server
        13 - Submit proof to Lambda Server for evaluation
        14 - Check LambdaCoin Wallet Balance
        15 - Fast Travel
        16 - Examine Item or Player
        """)

def treasure(playerChoice):
    serverResponse = pickUpTreasure(playerChoice)
    print("testing ersponse: ", serverResponse)
    return serverReponse

    

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