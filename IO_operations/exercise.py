 Q1. Write a program to read the entire content from a txt file and display it to the user.
file_name = input("Enter file name: ")
with open(file_name, 'r') as file:
    content = file.read()

print("File Content:\n")
print(content)

# Q2. Write a program to read first n lines from a txt file. Get n as user input.
file_name = input("Enter file name: ")
n = int(input("Enter number of lines to read: "))
with open(file_name, 'r') as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end='')


# Q3. Write a program to accept input from user and append it to a txt file.
file_name = input("Enter file name: ")
user_text = input("Enter text to append: ")
with open(file_name, 'a') as file:
    file.write(user_text + '\n')
print("Text appended successfully!")

# Q4. Write a program to read contents from a txt file line by line and store each line into a list.
file_name = input("Enter file name: ")
lines_list = []
with open(file_name, 'r') as file:
    for line in file:
        lines_list.append(line.strip())
print("Lines stored in list:")
print(lines_list)

# Q5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
file_name = input("Enter file name: ")
with open(file_name, 'r') as file:
    content = file.read()
words = content.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)

# Q6. Write a program to count the frequency of a user entered word in a txt file.
file_name = input("Enter file name: ")
search_word = input("Enter word to count: ")
with open(file_name, 'r') as file:
    content = file.read()
words = content.split()
count = words.count(search_word)
print(f"The word '{search_word}' occurs {count} times in the file.")
