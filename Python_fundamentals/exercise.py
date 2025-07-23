# HANDS ON ASSIGNMENT

#Q1. Write a program to check if a given number is Positive, Negative or Zero.
n = float(input("Enter a number: "))

if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")

# Q2. Write a program to check if a given number is odd or even.
n= int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1%10 == n2%10:
    print("True")
else:
    print("False")

# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1, 11):
    print(i, end="\t")

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

# Q6. Write a program to check if a given number is prime or not.
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime Number")
            break
    else:
        print("Prime")

# Q7. Write a program to print prime numbers between 10 and 99.
for num in range(10, 100):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# Q8. Write a program to print the sum of all the digits of a given number.
n = int(input("Enter a number: "))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print("Sum of all digits:", total)

# Q9. Write a program to reverse a given number and print.
n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n%10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed number:", reverse)

# Q10. Write a program to find if the given number is palindrom or not.
n = int(input("Enter a number: "))
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
