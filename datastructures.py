##Empty list creation 
my_list=[]

#Adding of elemnts using append method
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

##Insertion of element by use of index 
print("Before insertion:",my_list)
my_list[2]= 15

print("After insertion:", my_list)

#Extending list
my_list.extend([50])
my_list.extend([60])
my_list.extend([70])

print(my_list)

#Removal of last element from the list 
my_list.pop()

print(my_list)

#sort list in ascending order 
my_list.sort()

print(my_list)

try:
    index_of_30 = my_list.index(30)
    print(f"Index of 30: {index_of_30}")
except ValueError:
    print("Value 30 is not in the list.")
