from logging import exception

try:
    result = 10/10

except:
    print("This doesnt equal to 0, try again")



try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("u cant divide by zero")

fruits = {
    "apple":7,
    "banana":5,
    "orange":3
}

try:
    print(fruits["cherry"])
except KeyError:
    print("That isnt a key on your dictionary")

text = "this is not a nr"

try:
    text_as_int = int(text)
except Exception as e:
    print("An error has occured: " ,e)

try:
    result = 10/2
except ZeroDivisionError:
    print("ZeroDivisionError has occured")
else:
    print("The division was successful, result:",result)

try:
        result = 10 / 2
except ZeroDivisionError:
        print("ZeroDivisionError has occured")
finally:
        print("Finally the block is executed")