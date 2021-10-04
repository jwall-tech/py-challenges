def mid(string):
    stringLength = len(string)

    if stringLength % 2 > 0:
        return string[int(stringLength/2)]
    else:
        return " "

print(mid("abcde"))
print(mid("aaaa"))
