def only_ints(int1,int2):
    if type(int1) == int and type(int2) == int:
        return True
    return False

print(only_ints("hi",5))
print(only_ints(5,5))
print(only_ints("hi","hello"))
