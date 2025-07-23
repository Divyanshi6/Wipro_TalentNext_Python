              # *********** MINI PROJECT ***********
# PS1. create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. 
# if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination

distance = float(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor-cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# PS2. Let's assume you are planning to use your python skills to build an App for Mobile.
# You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. 
# you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
# Write a python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How much days can I operate one server with $918?

cost_per_hour = 0.51
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
print("Cost to operate one server per day: $", round(cost_per_day, 2))
print("Cost to operate one server per week: $", round(cost_per_week, 2))
print("Cost to operate one server per month: $", round(cost_per_month, 2))
budget = 918
days_possible = budget / cost_per_day
print("With $918, you can operate the server for", int(days_possible), "days")
