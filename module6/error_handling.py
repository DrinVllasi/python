try:
    result = 10/10

except:
    print("This doesnt equal to 0, try again")

fruits = {
    "apple":7,
    "banana":5,
    "orange":3
}

try:
    print(fruits["cherry"])
except KeyError:
    print("That isnt a key on your dictionary")