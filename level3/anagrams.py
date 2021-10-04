def is_anagram(string1,string2):
    i = 0
    for letter in string1:
        i += 1

        if letter in string2:
            string1 = string1[i:]
            string2 = string2[:string2.index(letter)] + string2[string2.index(letter)+1:]
        else:
            return False

    if string1 == "" and string2 == "":
        return True

    return False

print(is_anagram("typhoon","opython"))
print(is_anagram("Bob","Alice"))
print(is_anagram("typhoon","opaython"))
