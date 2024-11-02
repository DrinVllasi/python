fruits = ["apple","banana","cherry"]

print("fruits")

#create a tuple
words = ("spam","eggs","sausages")
print(words[1])

#creating a tuple with information about a person

person = ('drin',16,"student")

name,age,proffesion = person

print(name, "'s","proffesion is" , proffesion," and he is",age," years old")

#creating dictionary

my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

contact_info = {
    "blerta": "444-33334105",
    "drini": "22396-45512"
}

#create a variable called kreative's phone and use [] we can specify which key we want to access

print(contact_info)

kreative_phone = contact_info["blerta"]

print(kreative_phone)
print(contact_info)

contact_info["drini"] = "0294-48575"

print(contact_info)

#we want to add another friend to contact_info

contact_info["eros"] = "9374-117348"

print(contact_info)

#delete a contact info

del contact_info["blerta"]
print(contact_info)

#print only the keys of the dictionary

keys = contact_info.keys()

print(keys)

#print values
values = contact_info.values()
print(values)

#print items
items = contact_info.items()
print(items)