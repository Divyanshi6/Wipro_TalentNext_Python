#        **************** MINI PROJECT ****************

# Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and his or her interesting fact to the screen.
# Next, change a fact about one of the people.
# Also add an additional person and corresponding fact.
# Display the new list of people and facts.
# Run the program multiple times and notice if the order changes.

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Initial Facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

people_facts["Jeff"] = "Is afraid of heights."

people_facts["Jill"] = "Can hula dance."

print("\nUpdated Facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")


# Given the participant’s score sheet for your University Sports Day, you are required to find the runner-up score. You have a list of scores.
# Store them in a list and find the score of the runner-up
# Sample Input:
# [2, 3, 6, 6, 5]
# Sample Output:
# 5

scores = [2, 3, 6, 6, 5]
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
print("Runner-up score:", unique_scores[1])


# You have a record of n students. Each record contains the student's name and their percent marks in Math, Physics, and Chemistry. 
# The marks can be floating-point numbers.
# You are required to save the records in a dictionary data type.
# The student’s name is the key.
# The marks (as a list) are the value.
# The user enters a student’s name. Output the average percentage marks obtained by that student.
# Average = (sum of marks) / (number of subjects)
# Sample Input:
#   "Krishna": [67, 68, 69],
#   "Arjun": [70, 98, 63],
#   "Malika": [52, 56, 60]
# Sample Output:
# Enter a name: Malika
# Average percentage mark: 56

records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}
name = input("Enter a name: ")
if name in records:
    marks = records[name]
    average = sum(marks) / len(marks)
    print("Average percentage mark:", round(average))
else:
    print("Student not found.")


# Given a string of n words, help Alex to find out how many times his name appears in the string.
# Constraint: 1 <= n <= 200
# Sample input: Hi Alex WelcomeAlex Bye Alex.
# Sample output: 3
# Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.
string = "Hi Alex WelcomeAlex Bye Alex."
count = string.count("Alex")
print(count) 
