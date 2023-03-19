# We can take different type of data types in Lists
# It starts with Index 0
# Indicated by Square Brackets
#[] -Empty List
#List has different Elements
#List1=[1,2.2,"bc"]
#print(len(List1))

#print(type(List1))

#Nested Lists
#List2=[1,2,3,[1,2,3],2] #Starts with 0 index
#print(List2[3][1]) #2Dimensional - similar as Array

#Methods
#1.append - Adds the element at the last in the list
#2.extend - Adds the element as List at the last in the list
#3.remove - Removes the element
#4.insert - Inserts an element at the particular location
#5. index - Gives the index of the element
#6. count - counts the no. of times that element is referred
# Variable.function

List3=[1,2.2,'Kalpana',True]
List3.append(1)
print(type(List3))
List3.extend([1,2,3])
print(List3)
print(len(List3))
List3.insert(1,'python')
print(List3.count(1)) # Output shows extra 1 as True is also considered as 1
#Pop or delete
List3.pop(0)
print(List3)
#reverse
List3.reverse()
print(List3)
#Sort - Ascending/Descending
List4=[1,2.2,3,67,98,0,3,4]
List4.sort()
print(List4)

#If
for i in List4:
 print(i)
#If using List in the List
List5=[1,2.2,[3,67,98],0,3,4]
print(List5[2][0])

List1=[1,2.2,"bc",4]
print(len(List1))

#Check