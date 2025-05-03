-#Declaring a variable

#variable_name = value

temperature = 22.0

name = "Drin"

print(type(temperature))
print(type(name))

age = 16

x=5
y=8

result = x + y

print(result)

#update value

age = age +1
print(age)

#combine values

first_name = "Drin"
last_name = "Vllasi"
full_name = first_name + " " + last_name
print(full_name)

#lists

name_of_the_list = ['item1','item2','item3']

#example of a list

shopping_list = ["apples","banannas",'milk',3, 4.5]

print(shopping_list)

#indexing

homework = ["math","biology","psychology","geography","english"]
print(homework[0])
print(homework[4])
print(homework[2])

to_do_list = ["teach 11D","Go shopping","create the app","check devops"]
first_item = to_do_list[0] #this is accessing the first item at the index 0 which is 11D
second_item = to_do_list[1]
third_item = to_do_list[2]

favourite_subject = ["psikologji","sociologji","ed.fizike","frengjisht"]
fourth_subject = favourite_subject[3]
print(fourth_subject)

#adding data to a list we do so by using the append() method

#i want to add strawberries to the shopping list
shopping_list.append("strawberries")

print(shopping_list)


#insert method lets us specify where we want to add or element

shopping_list.insert(2,"lemons")
print(shopping_list)

#remove() method helps us remove items from the list
to_do_list.remove("check devops")
print(to_do_list)

del to_do_list[2]
print(to_do_list)

#updating data, you can change the value of an element by assigning a new value.
to_do_list[0] = "teach 1D"

print(to_do_list)