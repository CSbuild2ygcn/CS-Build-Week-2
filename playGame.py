from secrets import *
from MUD import *
from playerActions import *
import time

# token = token()
token = "2b31b01022bf6e2fa8e79e93a7f2db494acdfdd6"
print(token)
checkInventory = checkInventory()
initData = init()

# Relevant data for requesting
initRoomNumber = initData["room_id"]
initRoomTitle = initData["title"]
initRoomDescription = initData["description"]
initRoomCoordinates = initData["coordinates"]
initRoomElevation = initData["elevation"]
initRoomTerrain = initData["terrain"]
initRoomPlayers = initData["players"]
initRoomItems = initData["items"]
initRoomExits = initData["exits"]
initRoomCooldown = initData["cooldown"]
initRoomErrors = initData["errors"]
initRoomMessages = initData["messages"]


# roomNumber = movementResponse["room_id"]
# roomTitle = movementResponse["title"]
# roomDescription = movementResponse["description"]
# roomCoordinates = movementResponse["coordinates"]
# roomElevation = movementResponse["elevation"]
# roomTerrain = movementResponse["terrain"]
# roomPlayers = movementResponse["players"]
# roomItems = movementResponse["items"]
# roomExits = movementResponse["exits"]
# roomCooldown = movementResponse["cooldown"]
# roomErrors = movementResponse["errors"]
# roomMessages = movementResponse["messages"]

#
    # movement()

    # Make menu for player choice

    # move
    # fast move
    # pick up treasure
    # drop treasure
    # offer treasure for sale
    # sell treasure
    # Check inventory
    # examine player or item
    # equip item
    #unequip item
    # change name
    # prayu
    # give to ghost
    # take from ghost
    # Mine
    # get last proof
    # check lambda coin balance

def playGame():
    running = True
    print(f"Hello, Player, your token is: {token}, let's go on a mandatory 'adventure'.    Your inventory consists of {checkInventory}.  Press Q to quit at any time")
    # playerOne.lastRoom.name = "the sheer cliff you just scaled"
    print(f"You are in a room called {initRoomTitle}, room number {initRoomNumber}. Room Description: {initRoomDescription}.  Items you can see around you: {initRoomItems}.  The exits are {initRoomExits}")

    while running is True:
        playerAction = input("Enter which direction you want to go or some other choice: ")
        if playerAction == "q":
            print(f"You decide to quit.  Have a nice day")
            running = False
        else:
            if playerAction == "menu":
                menuOptions()
            
            # Check Inventory
            elif playerAction == "1":
                response = checkInventory
                print("test: ", response)
                print(f""" Your 
                Name: {response["name"]},
                Current Weight of all items: {response["encumbrance"]}
                Carrying Capacity: {response["strength"]}
                Speed: {response["speed"]}
                Gold: {response["gold"]}
                Tunic: {response["bodywear"]}
                Shoes: {response["footwear"]}
                Inventory: {response["inventory"]}
                Abilities: {response["abilities"]}
                Status: {response["status"]}
                Have passed MVP: {response["has_mined"]}
                """)
                print("Your cooldown penalty is: ", response["cooldown"])
                time.sleep(response["cooldown"])

            # Pick up treasure
            elif playerAction == "2":
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the treasure you wish to pick up: ")
                    response = pickUpTreasure(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("You picked the item up: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False

            # Drop treasure
            elif playerAction == "3":
                checkInventory
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the treasure you wish to drop: ")
                    response = dropTreasure(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("You dropped the item: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False    
            
            # Appraise value of treasure
            elif playerAction == "4":
                checkInventory
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the treasure you have appraised: ")
                    response = offerTreasureForSale(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("The shopkeeper tells you: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False    
            
            # Sell treasure
            elif playerAction == "5":
                checkInventory
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the treasure you wish to sell: ")
                    response = sellTreasure(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("You sold the treasure: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False   
            
            # Equip Item
            elif playerAction == "6":
                checkInventory
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the treasure you wish to equip: ")
                    response = equipItem(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("You equipped the item: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False  
            
            # Unequip Item
            elif playerAction == "7":
                checkInventory
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the treasure you wish to unequip: ")
                    response = unequipItem(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("You unequipped the item: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False  
            
            # Change Name
            elif playerAction == "8":
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter your new name: ")
                    response = changeName(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("Success! Your new name: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False 
            
            # Pray
            elif playerAction == "9":
                response = pray()
                if len(response["errors"]) > 0:
                    print("You failed becase ", response["errors"])
                    print("Your cooldown penalty is: ", response["cooldown"])
                    time.sleep(response["cooldown"])
                if len(response["messages"]) > 0:
                    print("Success! Your new name: ", response["messages"])
                    print("Your cooldown penalty is: ", response["cooldown"])
                    time.sleep(response["cooldown"])
            
            # Give item to ghost to hold
            elif playerAction == "10":
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the item to give to the ghost: ")
                    response = giveToGhost(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("Success! The ghost took the item: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False 
            
            # Take item from ghost
            elif playerAction == "11":
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the item to give to the ghost: ")
                    response = giveToGhost(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("Success! The ghost took the item: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False 
            
            # Get last proof
            elif playerAction == "12":
                response = lastProof()
                if len(response["errors"]) > 0:
                    print("You failed becase ", response["errors"])
                    print("Your cooldown penalty is: ", response["cooldown"])
                    time.sleep(response["cooldown"])
                if len(response["messages"]) > 0:
                    print("Success! The last proof is: ", response["messages"])
                    print("Your cooldown penalty is: ", response["cooldown"])
                    time.sleep(response["cooldown"])
            
            # Mine Lambda Coin
            elif playerAction == "13":
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the proof you wish to submit: ")
                    response = mine(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("Success! You mined a coin!: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False
            
            # Get Lambda Coin Balance
            elif playerAction == "14":
                response = lambdaCoinBalance()
                if len(response["errors"]) > 0:
                    print("You failed becase ", response["errors"])
                    print("Your cooldown penalty is: ", response["cooldown"])
                    time.sleep(response["cooldown"])
                if len(response["messages"]) > 0:
                    print("Your Lambda Coin Wallet Balance: ", response["messages"])
                    print("Your cooldown penalty is: ", response["cooldown"])
                    time.sleep(response["cooldown"])

            elif playerAction == "15":
                choosing = True
                while choosing is True:
                    if playerAction == "stop":
                        print(f"You return to a normal walking pace")
                        choosing = False
                    playerChoice, nextRoomNumber = input("Enter the direction and room number to go Sonic speed: ").split()
                    movementResponse = fastMove(playerChoice, nextRoomNumber)
                    movementResponse = movement(playerAction)
                    roomNumber = movementResponse["room_id"]
                    roomTitle = movementResponse["title"]
                    roomDescription = movementResponse["description"]
                    roomCoordinates = movementResponse["coordinates"]
                    roomElevation = movementResponse["elevation"]
                    roomTerrain = movementResponse["terrain"]
                    roomPlayers = movementResponse["players"]
                    roomItems = movementResponse["items"]
                    roomExits = movementResponse["exits"]
                    roomCooldown = movementResponse["cooldown"]
                    roomErrors = movementResponse["errors"]
                    roomMessages = movementResponse["messages"]
                    print(f"{roomMessages} You are now in a room called {roomTitle}, room number {roomNumber}. Room Description: {roomDescription}.  Items you can see around you: {roomItems}.  The exits are {roomExits}, your cooldown is {roomCooldown} seconds.  Your error messages are: {roomErrors}")
                    # Force user to wait until cooldown is done
                    time.sleep(roomCooldown)

            # Player movement                
            elif playerAction in ("n", "s", "e", "w"):
                movementResponse = movement(playerAction)
                roomNumber = movementResponse["room_id"]
                roomTitle = movementResponse["title"]
                roomDescription = movementResponse["description"]
                roomCoordinates = movementResponse["coordinates"]
                roomElevation = movementResponse["elevation"]
                roomTerrain = movementResponse["terrain"]
                roomPlayers = movementResponse["players"]
                roomItems = movementResponse["items"]
                roomExits = movementResponse["exits"]
                roomCooldown = movementResponse["cooldown"]
                roomErrors = movementResponse["errors"]
                roomMessages = movementResponse["messages"]
                print(f"{roomMessages} You are now in a room called {roomTitle}, room number {roomNumber}. Room Description: {roomDescription}.  Items you can see around you: {roomItems}.  The exits are {roomExits}, your cooldown is {roomCooldown} seconds.  Your error messages are: {roomErrors}")
                # Force user to wait until cooldown is done
                time.sleep(roomCooldown)
            else:
                print(f"""
                    Wrong input""")
            # if playerAction is "m":
            #     print("menu")
            #     break
            # print("test", movementResponse)

playGame()