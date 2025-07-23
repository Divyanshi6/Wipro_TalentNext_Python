#        **************** Tuple ****************
#  Q1. Write a program to remove a given item from the set.
s1 = {10, 20, 30, 40, 50}
item_remove = 30

s1.discard(item_remove) 
print("Updated set:", s1)

# Q2. Write a program to create an intersection of sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
new=set1.intersection(set2)
print("Intersection:", new)

# Q3. Write a program to create a union of sets.
set1 = {10, 20, 30}
set2 = {30, 40, 50}

union = set1.union(set2)
print("Union:", union)

# Q4. Write a program to find the maximum and minimum value in a set.
s2 = {12, 45, 7, 89, 34}

print("Maximum value:", max(s2))
print("Minimum value:", min(s2))
