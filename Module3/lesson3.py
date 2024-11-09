#create a set using curly braskets

#my_set = {1,2,3}

#print(my_set)

#creating a set from a list using the set() function
#my_set=([4,5,6])
#print(my_set)

#creating an empty set using the set() function
#my_set = set()
#print(my_set)

my_set = {1,1,2,3,3,4,5,3,2,3}
print(my_set) #set removes all duplicates


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