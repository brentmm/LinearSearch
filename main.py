from random import randint

#generates list if 10 random numbers
def test():
    a = []
    for i in range(0, 10):
        a.append(randint(0, 10))
    return a


#searches for userInput
def linearSearch(c):
    userInput = int(input("Pick an Integer: "))  #user Chooses a number to search for
    n = len(c)
    for i in range(0, n):
        if c[i] == userInput:  #checks if list index value = userInput
            indexNum = i  #storing what index userInput is
            found = True  #if number is found
            break
        else:
            indexNum = False  #stores false if userInput is not found
            found = False  #if userInput is not found

    return userInput, indexNum, found

b = test()
print(b)
d = linearSearch(b)

print()
print("List: " + str(b))
print()

if d[2] == True:
    print("Found " + str(d[0]) + " at index " + str(d[1]) + ".")
else:
    print(str(d[0]) + " not found.")
