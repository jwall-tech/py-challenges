def online_count(table):
    online = 0
    for key in table:
        item = table[key]
        if item.lower() == "online":
            print(key + " is online")
            online += 1

    print("total online: "+str(online))
    return online

t1 = {
    "Billy" : "Online",
    "Moritz" : "Online",
    "James": "Offline",
    }

t2 = {
    "Ded" : "Offline",
    "Alive" : "Online",
    }

online_count(t1)
print("----------")
online_count(t2)
