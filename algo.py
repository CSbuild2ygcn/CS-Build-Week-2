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
cooldown = 15

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
def run_request(request, main_arg=None, prev_request_cooldown=15, fast_room_id=None, dash_room_ids=None):
    time.sleep(prev_request_cooldown)
    if request == "fastMove":
        response = request(main_arg, fast_room_id)
    elif request == "dash":
        response = request(main_arg, len(dash_room_ids.split(",")), dash_room_ids)
    elif request == "move" or "fly":
        response = request(main_arg)
    else:
        response = request()
    
    cooldown = response["cooldown"]
    return response

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

    # otherwise, create room, assign exit just used, fill other exits with '?'
    else:
        own_graph[player.currentRoom.id] = {}
        for x in player.currentRoom.getExits():
            if get_opp(direction) == x: 
                own_graph[player.currentRoom.id][x] = prev_room
            else:
                own_graph[player.currentRoom.id][x] = '?'

    # assign exit just used to previous room
    for x in prev_exits:
        if x == direction:
            own_graph[prev_room][x] = player.currentRoom.id

def get_unexplored(unexplored):
    # if any exits in current room == '?', add to unexplored list
    for x in player.currentRoom.getExits():
        if own_graph[player.currentRoom.id][x] == '?':
            unexplored.append(x)

def travel(direction):
    player.travel(direction)
    traversalPath.append(direction)

def dft():
    
    # while len(own_graph) < 500:  
        # open, read, save, close
    with open('data.txt') as f:
        our_data = json.load(f)
    f.closed
    own_graph = our_data
    
    # add info into own_graph
    info = run_request(move, 's', cooldown)
    print("info", info)

    with open('data.txt', 'w') as f:
        our_data = json.dump(own_graph, f)
    f.closed

dft()