# HANDS ON ASSIGNMENT 
#        **************** Functions ****************
# Q1. Write a function to return the sum of all numbers in a list Sample Input: (8, 2, 3, 0, 7) Expected Output: 20
def sum_list(numbers):
    return sum(numbers)

print(sum_list([8, 2, 3, 0, 7]))

# Q2. Write a function to return the reverse of a string Sample Input: "1234abcd" Expected Output: "dcba4321"
def reverse_string(s):
    return s[::-1]

print(reverse_string("1234abcd"))

# Q3. Write a function to calculate and return the factorial of a non-negative integer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 

# Q4. Write a function that accepts a string and prints the number of uppercase and lowercase letters in it
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")

count_case("Hello World")

# Q5. Write a function to print even numbers from a given list Sample Input: [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Output: [2, 4, 6, 8]
def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Q6. Write a function that takes a number as a parameter and checks if it’s prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11)) 
