#create a set using curly braskets

#my_set = {1,2,3}

#print(my_set)

#creating a set from a list using the set() function
#my_set=([4,5,6])
#print(my_set)

#creating an empty set using the set() function
#my_set = set()
#print(my_set)

#my_set = {1,1,2,3,3,4,5,3,2,3}
#print(my_set) #set removes all duplicates


#################

set1 = {1,2,3}
set2 = {3,4,5}

#union between set1 and set2 using the union() method

union_method = set1.union(set2)
print(union_method)

#compute union between set1 and set2 using the | operator

union_operator = set1 | set2

print("Union of set1 and set2 using method: ",union_method)
print("Union of set1 and set2 using operator: ",union_operator)

#compute intersection between set1 and set2 using the intersection() method

intersection_method = set1.intersection(set2)

#computing intersection between set1 and set2 using & operator

intersection_operator = set1 & set2

print("Intersection of set1 and set2 using the intersection method: ",intersection_method)
print("Intersection of set1 and set2 using the intersection operator: ",intersection_operator)

#computing the elements that are unique to set1 using the difference method

difference_method = set1.difference(set2)

#computing the elements that are unique to set1 using the - operator

difference_operator = set1 - set2

print("Difference of set1 and set2 using the difference method: ",difference_method)
print("Difference of set1 and set2 using the difference operator: ",difference_operator)

#computing the elements that are in set1 and in set2 but not their intersection
symmetric_difference_method = set1.symmetric_difference(set2)

#computing the elements that are in set1 and in set2 but not in their intersection using the ^ operator
symmetric_difference_operator = set1 ^ set2

print("Symmetric difference of set1 and set2 using the symmetric difference method: ",symmetric_difference_method)
print("Symmetric difference of set1 and set2 using the symmetric difference operator: ",symmetric_difference_operator)


#SET METHODS

#Create a set

my_set = {1,2,3}

#add number 7 at the end of the set

my_set.add(7)

#remove number 3 from my set

my_set.remove(3) #remove method

#removing 8 from the set without throwing an error if 8 is now on the set

my_set.discard(8)
print(my_set)

#removingall the numbers from the set
my_set.clear()

print(my_set)


#remove duplications from a list

#create a list that contains duplications

my_list = [1,2,2,2,3,4,4,4,5,6]

#convert this list to a set to remove duplications
unique_set = set(my_list)

print(unique_set)

#conver this set to a list
unique_list = list(unique_set)
print(unique_list)


#checking for common elements

blertas_interests = {"music","movies","travel"}
drilonis_interests = {"movies","games","skiing"}

common_interests = blertas_interests.intersection(drilonis_interests)
print(common_interests)

#IN operator

colors = {"red","purple","yellow","blue"}
color = "blue"

print(color in colors)

