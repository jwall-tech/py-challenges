def double_letters(string):
    lastLetter = ""

    for letter in string:
        if letter == lastLetter:
            return True
        lastLetter = letter
    return False

print(double_letters("nono"))
print(double_letters("aabb"))
