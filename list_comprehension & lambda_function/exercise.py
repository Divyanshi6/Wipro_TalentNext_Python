# Q1. Write a list comprehension program to create an output dictionary which contains only the odd numbers
#  that are present in the input list = [1, 2, 3, 4, 5, 6, 7] as keys and their cubes as values.
list = [1, 2, 3, 4, 5, 6, 7]
dict = {x: x**3 for x in list if x % 2 != 0}
print(dict)


# Q2. Make a dictionary of the 26 English alphabets mapping each with the corresponding integer.
alphabet_dict = {chr(i + 97): i + 1 for i in range(26)}
print(alphabet_dict)

# Q3. Cubes every number in the given list: list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubed_list = list(map(lambda x: x**3, list_1))
print(cubed_list)
