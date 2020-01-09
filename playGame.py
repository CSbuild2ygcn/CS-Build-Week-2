from secrets import *
from MUD import *
from playerActions import *
import time
from mining import *

# token = token()
#token = "ABC123"
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

def playGame():
    running = True
    print(f"Hello, Player, your token is: {token}, let's go on a mandatory 'adventure'.    Your inventory consists of {checkInventory}.  Press Q to quit at any time")
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
            
            # Change Name
            elif playerAction == "18":
                choosing = True
                while choosing is True:
                    playerChoice = input("Confirm your new name: ")
                    response = confirmName(playerChoice)
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
                    print("You failed because ", response["errors"])
                    print("Your cooldown penalty is: ", response["cooldown"])
                    time.sleep(response["cooldown"])
                if len(response["messages"]) > 0:
                    print("Success! Your prayer has been answered: ", response["messages"])
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
                    lastNum = lastProof()
                    difficulty = lastNum["difficulty"]
                    oldProof = lastNum["proof"]
                    coolD = lastNum["cooldown"]
                    print("Difficulty being sent in is: ", difficulty)
                    print("last proof is: ", oldProof)
                    time.sleep(coolD)
                    newProof = proof_of_work(oldProof, difficulty)
                    print("Proof to be sent in: ", newProof)
                    print("Type of proof being sent in: ", type(newProof))
                    response = mine(newProof)
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

            # Fast travel - for moving, NOT picking anything up, praying, or anything else
            # Drop out of Sonic speed before moving about the cabin
            elif playerAction == "15":
                print("To exit the realm of Sonic and return to normal walking speed, type 'stop' to BOTH input requests")
                print("Fast Travel requires two arguments - 1) NSWE, and 2) Room Number where you'r traveling to")
                choosing = True
                while choosing is True:
                    playerAction = input("Enter the direction: ")
                    if playerAction == "stop":
                        print(f"You return to a normal walking pace")
                        choosing = False
                    nextRoomNumber = input("Enter the room number: ")
                    if nextRoomNumber == "stop":
                        print(f"You return to a normal walking pace")
                        choosing = False
                    else:
                        movementResponse = fastMove(playerAction, nextRoomNumber)
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
                        print(f"""
                        {roomMessages} You are now in a room called {roomTitle}, room number {roomNumber}. Room Description: {roomDescription}.  Items you can see around you: {roomItems}.  The exits are {roomExits}, your cooldown is {roomCooldown} seconds.  Your error messages are: {roomErrors}""")
                        # Force user to wait until cooldown is done
                        time.sleep(roomCooldown)
            
            # Examine Item
            # Doesn't work for Player bc "User 1234" is 2 strings
            elif playerAction == "16":
                choosing = True
                while choosing is True:
                    playerChoice = input("Enter the name of the player or item you wish to examine: ")
                    response = examine(playerChoice)
                    if len(response["errors"]) > 0:
                        print("You failed becase ", response["errors"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    if len(response["messages"]) > 0:
                        print("Here's what Lion-O's Sight Beyond Sight reveals: ", response["messages"])
                        print("Your cooldown penalty is: ", response["cooldown"])
                        time.sleep(response["cooldown"])
                    choosing = False

            # Examine current room
            elif playerAction == "17":
                print(initData)

            # Fly
            elif playerAction == "19":
                choosing = True
                while choosing is True:
                    playerAction = input("Enter the direction: ")
                    if playerAction == "stop":
                        print(f"You return to a normal walking pace")
                        choosing = False
                    else:
                        movementResponse = fly(playerAction)
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
                        print(f"""
                        {roomMessages} You are now in a room called {roomTitle}, room number {roomNumber}. Room Description: {roomDescription}.  Items you can see around you: {roomItems}.  The exits are {roomExits}, your cooldown is {roomCooldown} seconds.  Your error messages are: {roomErrors}""")
                        # Force user to wait until cooldown is done
                        time.sleep(roomCooldown)

            # Dash
            elif playerAction == "20":
                choosing = True
                while choosing is True:
                    playerAction = input("Enter the direction: ")
                    if playerAction == "stop":
                        print(f"You return to a normal walking pace")
                        choosing = False
                    num_rooms = input("Enter the number of rooms to dash: ")
                    if num_rooms == "stop":
                        print(f"You return to a normal walking pace")
                        choosing = False

                    else:
                        next_room_ids = []
                        for x in range(0, int(num_rooms)):
                            x_room_id = input("Enter room id: ")
                            if x_room_id == "stop":
                                print(f"You return to a normal walking pace")
                                choosing = False
                            next_room_ids.append(x_room_id)
                        next_room_ids = ",".join(next_room_ids)
                        movementResponse = dash(playerAction, num_rooms, next_room_ids)
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
                        print(f"""
                        {roomMessages} You are now in a room called {roomTitle}, room number {roomNumber}. Room Description: {roomDescription}.  Items you can see around you: {roomItems}.  The exits are {roomExits}, your cooldown is {roomCooldown} seconds.  Your error messages are: {roomErrors}""")
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
                print(f"""
                {roomMessages} You are now in a room called {roomTitle}, room number {roomNumber}. Room Description: {roomDescription}.  Items you can see around you: {roomItems}.  The exits are {roomExits}, your cooldown is {roomCooldown} seconds.  Your error messages are: {roomErrors}""")
                # Force user to wait until cooldown is done
                time.sleep(roomCooldown)
            else:
                print(f"""
                    Wrong input""")

playGame()