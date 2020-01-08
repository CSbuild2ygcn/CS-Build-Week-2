import json
import time
z = {
    1: {
        "name": "bob",
        "age": 52,
        "kids": ["susan", "charles"],
        "car": {
            "make": "toyota",
            "model": "camry"
        }
    }
}
x = {
    0: {
        "room_id": 0,
        "title": "",
        "description": "",
        "coordinates": (),
        "elevation": 0,
        "terrain": "",
        "items": [],
        "exits": {
            'n': '?', 's': '?', 'e': '?', 'w': '?'
        }

    }
}

start = time.time()
with open('data.txt', 'w') as f:
    json.dump(x, f)
    # json.dump(z, f)
f.closed
end = time.time()
# print(f"dump time2: {end - start}")

# with open('data.txt', 'w') as f:
#     json.dump(z, f)
#     # json.dump(z, f)
# f.closed
# end = time.time()

start2 = time.time()
with open('data.txt') as f:
    json.dump(z, f)

    y = json.load(f)
    # a = json.load(f)
    # y = f.read()
    print(y, a)
    # print(a)
f.closed
end2 = time.time()
# print(f"load time: {end2 - start2}")
