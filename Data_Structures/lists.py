#        **************** LIST ****************

# Q1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
L1 = [10, 20, 30, 40, 50]
print("List:", L1)
print("Accessing elements individually:")
print("First element:", L1[0])
print("Second element:", L1[1])
print("Third element:", L1[2])
print("Fourth element:", L1[3])
print("Fifth element:", L1[4])

# Q2. Write a program to append a new item to the end of the list.
L2 = [1, 2, 3, 4]
L2.append(5)
print("List after appending:", L2)

# Q3. Write a program to reverse the order of the items in the list.
L3 = [1, 2, 3, 4, 5]
L3.reverse()
print("Reversed list:", L3)

# Q4. Write a program to print the number of occurrences of a specified element in a list.
L4 = [1, 2, 3, 2, 4, 2, 5]
count = L4.count(2)
print("Number of occurrences of 2:", count)

# Q5. Write a program to append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print("Combined list with list1 at front:", list2)

# Q6. Write a program to insert a new item before the second element in an existing list.
L6 = [10, 30, 40]
L6.insert(1, 20)  
print("List after insertion:", L6)

# Q7. Write a program to remove the item from a specified index in a list.
L7 = [10, 20, 30, 40, 50]
idx_remove = 2
removed = L7.pop(idx_remove)
print("Removed item:", removed)
print("List after removal:", L7)

# Q8. Write a program to remove the first occurrence of a specified element from a list.
L8 = [10, 20, 30, 20, 40]
L8.remove(20)  
print("List after removing first occurrence of 20:", L8)
