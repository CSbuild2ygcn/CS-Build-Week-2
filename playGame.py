from secrets import *
from MUD import *
from playerActions import *

token = token()
print(token)
checkInventory = checkInventory()
initData = init()
# Relevant data for requesting
roomNumber = initData["room_id"]
roomTitle = initData["title"]
roomDescription = initData["description"]
roomCoordinates = initData["coordinates"]
roomElevation = initData["elevation"]
roomTerrain = initData["terrain"]
roomPlayers = initData["players"]
roomItems = initData["items"]
roomExits = initData["exits"]
roomCooldown = initData["cooldown"]
roomErrors = initData["errors"]
roomMessages = initData["messages"]

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
    print(f"Hello, Player, your token is: {token}, let's go on a mandatory 'adventure'.    Your inventory consists of {checkInventory}.  You are in room {roomNumber} Press Q to quit at any time")
    # playerOne.lastRoom.name = "the sheer cliff you just scaled"
    while running:
        print(f"You are in a room called {roomTitle}, room number {roomNumber}. You look and see {roomDescription}.  Items you can see: {roomItems} on the floor.  The exits are {roomExits}")
        playerAction = input("Enter which direction you want to go or some other choice: ")
        if playerAction == "q":
            print(f"You decide to quit.  Have a nice day")
            running = False
        else:
            print("Hello world")

playGame()