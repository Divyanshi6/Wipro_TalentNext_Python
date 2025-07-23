#        **************** String ****************
#  Q1. Write a program to count the number of upper and lower case letters in a string.
s1 = "Hello World"
upper = 0
lower = 0
for char in s1:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

#  Q2. Write a program that will check whether a given string is palindrome or not.
s2 = "madam"
if s2 == s2[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#  Q3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string.
s3 = "Wipro"
n = len(s3)
result = s3[:2] * n
print("Output:", result)

# Q4. Given a string, if the first or last character is 'x', return the string without those 'x' characters, else return the string unchanged.
s4 = "xHix"
if s4.startswith('x'):
    s4 = s4[1:]
if s4.endswith('x'):
    s4 = s4[:-1]
print("Output:", s4)

# Q5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
s5 = "Wipro"
n = 3
result = s5[-n:] * n
print("Output:", result)
