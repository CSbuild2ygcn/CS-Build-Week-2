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

    while running:
        
        playerAction = input("Enter which direction you want to go or some other choice: ")
        if playerAction == "q":
            print(f"You decide to quit.  Have a nice day")
            running = False
        else:
            if playerAction == "menu":
                print(f"""
                    move
                    fast move
                    pick up treasure
                    drop treasure
                    offer treasure for sale
                    sell treasure
                    Check inventory
                    examine player or item
                    equip item
                    unequip item
                    change name
                    pray
                    give to ghost
                    take from ghost
                    Mine
                    get last proof
                    check lambda coin balance""")
                
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
                time.sleep(roomCooldown)
            else:
                print(f"""
                    Wrong input""")
            # if playerAction is "m":
            #     print("menu")
            #     break
            # print("test", movementResponse)

playGame()