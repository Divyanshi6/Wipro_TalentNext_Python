#        **************** Dictionary ****************
# Q1. Write a program to add a key and value to a dictionary.
#     Sample Dictionary: {0: 10, 1: 20}
#     Expected Result: {0: 10, 1: 20, 2: 30}
d1 = {0: 10, 1: 20}
d1[2] = 30
print("Updated Dictionary:", d1)

# Q2. Write a program to concatenate the following dictionaries to create a new one.
    #   Sample Dictionary:
    #   dic1 = {1: 10, 2: 20}  
    #   dic2 = {3: 30, 4: 40}  
    #   dic3 = {5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new = {}
new.update(dic1)
new.update(dic2)
new.update(dic3)
print("Concatenated Dictionary:", new)

# Q3. Write a program to check if a given key already exists in a dictionary.
d2 = {1: 'a', 2: 'b', 3: 'c'}
key = 2
if key in d2:
    print(f"Key {key} exists in the dictionary.")
else:
    print(f"Key {key} does not exist in the dictionary.")

# Q4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone, and both keys and values.
d3 = {'a': 100, 'b': 200, 'c': 300}
print("Keys:")
for key in d3:
    print(key)

print("\nValues:")
for value in d3.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in d3.items():
    print(key, ":", value)

# Q5. Write a program to prepare a dictionary where the keys are s2 between 1 and 15 (both included) and the values are square of the keys.
d4 = {}
for i in range(1, 16):
    d4[i] = i * i
print("Square Dictionary (1–15):", d4)

# Q6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
d5 = {'a': 100, 'b': 200, 'c': 300}
total = sum(d5.values())
print("Sum of all values:", total)
