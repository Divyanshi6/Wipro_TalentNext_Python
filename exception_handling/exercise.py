# Q1. Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
def safe_division():
    try:
        n1_str = input("Enter the first number: ")
        n2_str = input("Enter the second number: ")

        n1 = float(n1_str)
        n2 = float(n2_str)

        result = n1 / n2
        print(f"The result of division is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

safe_division()

# Q2. Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_with_input():
    try:
        n_str = input("Enter an integer to check if it's prime: ")
        num = int(n_str)

        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

check_prime_with_input()

# Q3.Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
def read_file_in_title_case():
    file_name = input("Enter the name of the file to open: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File Contents (Title Case):")
            print(content.title())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError:
        print(f"Error: Could not read from the file '{file_name}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file_in_title_case()

# Q4.Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
def check_list_index():
    my_list = [10, -5, 20, -15, 30, -25, 40, -35, 50, -45] 

    try:
        index_str = input(f"Enter an index (0 to {len(my_list) - 1}): ")
        index = int(index_str)

        if 0 <= index < len(my_list):
            value = my_list[index]
            if value >= 0:
                print(f"The number at index {index} ({value}) is positive (or zero).")
            else:
                print(f"The number at index {index} ({value}) is negative.")
        else:
            print(f"Error: Index out of range. Please enter an index between 0 and {len(my_list) - 1}.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer for the index.")
    except IndexError: 
        print(f"Error: Index out of range. Please enter an index between 0 and {len(my_list) - 1}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

check_list_index()
