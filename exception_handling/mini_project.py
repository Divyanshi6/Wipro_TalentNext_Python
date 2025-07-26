# Project: 1
# You saved the item names and their price details in a text file, which you purchased from a supermarket.

# You need to calculate:
# How many items did you purchase?
# How many items are free?
# What is the total amount you had to pay?
# What is the discount amount?
# What is the final amount you paid after the discount?

# Requirements:
# Write Python code using exception handling.
# The data is stored in a file like Purchase-1.txt.
# Each line contains an item's details: item price
# Item and price are separated by a space.
# Some lines might be blank or contain Free.
# The last line contains the discount (e.g., Discount 80).

def process_purchase():
    try:
        filename = input("Enter the file name: ").strip()
        with open(filename, 'r') as file:
            lines = file.readlines()

        total_price = 0
        purchased_items = 0
        free_items = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue  
            try:
                item, price = line.split()
                if item.lower() == "discount":
                    discount = int(price)
                elif price.lower() == "free":
                    free_items += 1
                else:
                    total_price += int(price)
                    purchased_items += 1
            except ValueError:
                print(f"Skipping invalid line: '{line}'")
                continue

        final_amount = total_price - discount

        print(f"Number of items purchased: {purchased_items}")
        print(f"Number of free items: {free_items}")
        print(f"Amount to pay: {total_price}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found... Please check the file name.")
    except Exception as e:
        print("error occurred:", e)

process_purchase()
