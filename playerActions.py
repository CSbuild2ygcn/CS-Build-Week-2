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
        17 - Examine room you're currently in
        18 - Confirm name change
        """)