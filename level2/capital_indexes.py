def capital_indexes(string):
    lis = []
    index = 0

    for letter in string:
        if letter.upper() == letter:
            lis.append(index)
        index += 1

    return lis

print(capital_indexes("HeLlO"))
