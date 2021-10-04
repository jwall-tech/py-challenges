def flatten(*args):
    endTable = []
    for table in args:
        for item in table:
            endTable.append(item)
    return endTable

print(flatten([5,5],[6,7],[12,24,251]))
print(flatten([5,5],[6,7],[12,24,251],[5,5],[6,7],[12,24,251]))
