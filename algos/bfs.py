import json
# import queue

from util import Queue
# # pseudocode
# BFS(graph, startVert):
#   for v of graph.vertexes:
#     v.color = white

#   startVert.color = gray
#   queue.enqueue(startVert)

#   while !queue.isEmpty():
#     u = queue[0]  // Peek at head of queue, but do not dequeue!

#     for v of u.neighbors:
#       if v.color == white:
#         v.color = gray
#         queue.enqueue(v)
    
#     queue.dequeue()
#     u.color = black



def bfs(start_room, end_room):
    # route = []
    local_graph = {}
    with open('small_graph.txt') as f:
        local_graph = json.load(f)
    f.closed        
    # print ("local_graph: ", local_graph)
    q = Queue()
    q.enqueue([start_room])
    visited = set()

    print("q.queue = ", q.queue)

    while len(q.queue) > 0:
        u = q.queue[0]
        print("u: ", u)
        path = q.dequeue()
        print("path: ", path)

        room = str(path[-1])
        # room = str(path[0])

        print("room: ", room)

        if room not in visited:

            if room == end_room:
                return path

            visited.add(room)
            # route.append(room)


            print("local_graph[room]: ", local_graph[room])
            # for x in local_graph[room]:
            for x in (local_graph[room]):
                # local_graph[room][x]

                # print("local_graph[room][x]", local_graph[room][x])
                # print("v", v)
                new_path = path.copy()
                new_path.append(local_graph[room][x])
                q.enqueue(new_path)
        
        # print("visited: ", visited)





print(bfs(0, 55))