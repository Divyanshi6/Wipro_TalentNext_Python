#        **************** Tuple ****************
# Q1. Write a program to print the 4th element from first and 4th element from last in a tuple.
t1 = (5, 10, 15, 20, 25, 30, 35, 40)
print("4th element from start:", t1[3])     
print("4th element from end:", t1[-4])

#Q2. Write a program to check whether an element exists in a tuple or not.
t2= (1, 3, 5, 7, 9)
element = 5
if element in t2:
    print(element, "exists in the tuple")
else:
    print(element, "does not exist in the tuple")

#Q3. Write a program to convert a list into a tuple.
list = [1, 2, 3, 4, 5]
t3 = tuple(list)
print("Converted tuple:", t3)

#Q4. Write a program to find the index of an item in a tuple.
t4 = (10, 20, 30, 40, 50)
item = 30
index = t4.index(item)
print("Index of", item, "is", index)

#Q5. Write a program to replace the last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
list2 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = []
for t in list2:
    new_tuple = t[:-1] + (100,)  
    updated_list.append(new_tuple)
print("Updated list:", updated_list)
