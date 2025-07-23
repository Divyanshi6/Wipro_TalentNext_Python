#        **************** MINI PROJECT ****************
# Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
# Constraint: All the colors will be completely in either lower case or upper case.
# Sample input 1: green-red-yellow-black-white
# Sample output 1: black-green-red-white-yellow
# Sample input 2: PINK-BLUE-TAN-PURPLE
# Sample output 2: BLUE-PINK-PURPLE-TAN
def sort_colors(color_string):
    colors = color_string.split('-')
    sorted_colors = sorted(colors)
    return '-'.join(sorted_colors)

print(sort_colors("green-red-yellow-black-white"))   
print(sort_colors("PINK-BLUE-TAN-PURPLE"))           

# Create a Python module with the following functions:
# \| Function Name              | Task                                                                 |
# > \|----------------------------|----------------------------------------------------------------------|
# > \| ispalindrome(name)         | Given the user name as input, this function should tell us whether the name is a palindrome or not. |
# > \| count\_the\_vowels(name)     | Given the user name as input, this function should tell us how many vowels are present in it. |
# > \| frequency\_of\_letters(name) | Given the user name as input, this function should tell us how many times each letter appears in the name. |
# Note: name will be completely in either lower case or upper case.
# Import the module in another python script and test the functions by passing appropriate inputs.
# Sample input 1: bob
# Sample output 1:
# Yes it is a palindrome.
# No of vowels: 1
# Frequency of letters: b-2, o-1
# Sample input 2: marcel bentok tanaka
# Sample output 2:
# No it is not a palindrome.
# No of vowels: 7
# Frequency of letters: m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1, k-2

# mymodule.py
def is_palindrome(name):
    name_without_spaces = name.replace(" ", "")
    reversed_name = name_without_spaces[::-1]
    if name_without_spaces == reversed_name:
        return True
    else:
        return False

def count_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in name:
        if letter in vowels:
            count += 1
    return count

def letter_frequency(name):
    freq = {}
    for letter in name:
        if letter != " ": 
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
    return freq
