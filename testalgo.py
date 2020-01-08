# TO DO:
# 1) Change tracking of traversal from own_graph to writing to a text file, so it persists between sessions and we can pass it around to the team
# 2) Add ability to read cooldown from server response, and set a timer for next move based on what's returned
# 3) Add functions from MUD.py to navigate island.  Can change len(roomGraph) to 500, since we know how large the island is
# 4)  if we find shrine, maybe pray at shrine while exploring to get powers right away, and then in rare case we can dash, dash?
import json
import subprocess
import time
# from secrets import token
from MUD import *
# from MUD.py import { move, fastMove, pray, fly, dash checkstatus }




# upon reaching shrine, pray to get powers
    # check to make sure we have powers
        # if we do, dash if possible
            # else fly
        # if not, normal move



traversalPath = []
backpath = []
own_graph = {}


# # after request, store into exits here
def getExits():
    exits = []
    if self.n_to is not None:
        exits.append("n")
    if self.s_to is not None:
        exits.append("s")
    if self.w_to is not None:
        exits.append("w")
    if self.e_to is not None:
        exits.append("e")
    return exits

# keep track of cooldown from response
def runRequest(request, argsforRequest):
    response = request(argsforRequest)
    time.sleep(response['cooldown'])

# # don't have tot touch
def get_opp(direction):
    if direction == 'n':
        return 's'
    if direction == 'e':
        return 'w'
    if direction == 's':
        return 'n'
    if direction == 'w':
        return 'e'

def log_path(direction, prev_room, prev_exits):
    # if room already in own graph, assign exit just used, leave everything else alone
    if player.currentRoom.id in own_graph:
        for x in player.currentRoom.getExits():
            if get_opp(direction) == x: 
                own_graph[player.currentRoom.id][x] = prev_room
​
    # otherwise, create room, assign exit just used, fill other exits with '?'
    else:
        own_graph[player.currentRoom.id] = {}
        for x in player.currentRoom.getExits():
            if get_opp(direction) == x: 
                own_graph[player.currentRoom.id][x] = prev_room
            else:
                own_graph[player.currentRoom.id][x] = '?'
​
    # assign exit just used to previous room
    for x in prev_exits:
        if x == direction:
            own_graph[prev_room][x] = player.currentRoom.id

def get_unexplored(unexplored):
    # if any exits in current room == '?', add to unexplored list
    for x in player.currentRoom.getExits():
        if own_graph[player.currentRoom.id][x] == '?':
            unexplored.append(x)
​
def travel(direction):
    player.travel(direction)
    traversalPath.append(direction)

def dft():
    
    # while len(own_graph) < 500:  
        # open, read, save, close
    with open('data.txt') as f:
        our_data = json.load(f)
    f.closed

        prev_room = player.currentRoom.id
        prev_exits = player.currentRoom.getExits()
        loop through current room exits, if exit == '?', then add to unexplored list
        unexplored = []
        get_unexplored(unexplored)
        ​
        # choose random direction from unexplored
        if len(unexplored) > 0:
            direction = random.choice(unexplored)
            travel(direction)
            backpath.append(get_opp(direction))  
        else: 
            # if dead-end reached
            while len(unexplored) == 0:
                direction = backpath.pop()
                travel(direction)
                get_unexplored(unexplored)
​
        #### after traveling, log
        # #open dump close
        log_path(direction, prev_room, prev_exits)
        # own graph maybe?
    info = runRequest(move, 's')
    with open('data.txt', 'w') as f:
        our_data = json.dump(info, filter)
    f.closed
​

dft()