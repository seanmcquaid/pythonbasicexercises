# 1. Hello, you!
# Prompt the user for his name using the input function. Example:

# name = input('What is your name? ')
# Upon receiving his name, you will say hello to him. Example session:

# $ python hello.py What is your name? Toby Hello, Toby!

# name = raw_input("What is your name? ")

# print "Hello, %s!" % name

# 2. HELLO, YOU!
# Same as the first exercise, but this time print the user's name in ALL CAPS, 
# and also tell them the number of letters in their name. Example session:

# $ python hello2.py WHAT IS YOUR NAME? Toby HELLO, TOBY! YOUR NAME HAS 4 LETTERS IN IT! AWESOME!

# name = raw_input("What is your name? ")

# num = len(name)

# print "HELLO, " + name.upper() + "!" + " YOUR NAME HAS %d LETTERS IN IT! AWESOME" %num

# 3. Madlib
# Prompt the user for the missing words to a Madlib sentence using the input function. 
# You will make up your own Madlib sentence, but here's an example:

# ____(name)____'s favorite subject in school is ____(subject)____.
# With the above given sentence, this is what a user session might look like:

# $ python madlib.py Please fill in the blanks below: ____(name)____'s favorite subject in school is ____(subject)____. 
# What is name? Marty What is subject? math Marty's favorite subject in school is math.

# print "Please fill in the blanks below: _______'s favorite subject in school is _______."

# name = raw_input("What is your name? ")
# subject = raw_input("What is your favorite subject? ")

# print name + "'s favorite subject in school is " + subject + "."


# 4. Day of the Week
# Given the following code that prompts the user for a day number 
# (the int function converts a numeric string to a number):

# day = int(input('Day (0-6)? ')) # Fill in your code here
# The user will enter a number between 0 to 6 inclusive. Given this number, print a day of the week. 
# 0 for Sunday, 1 for Monday, 2 for Tuesday, and so on. Here's an example user session 
# (this assumes you've named the file day_of_week.py):

# $ python day_of_week.py Day (0-6)? 5 Friday $ python day_of_week.py Day (0-6)? 0 Sunday

# user_num = raw_input("Pick a day between 0-6: ")
# gameOn = True
# day = {
#     "0" : "Sunday",
#     "1" : "Monday",
#     "2" : "Tuesday",
#     "3" : "Wednesday",
#     "4" : "Thursday",
#     "5" : "Friday",
#     "6" : "Saturday"
# }

# while (gameOn):
#     if user_num in day:
#         print day[user_num]
#         gameOn = False


# 5. Work or Sleep In?
# Prompt the user for a day of the week just like the previous problem. 
# Except this time print "Go to work" if it's a work day and "Sleep in" if it's a weekend day. 
# Example session:

# $ python work_or_sleep_in.py Day (0-6)? 5 Go to work $ python work_or_sleep_in.py Day (0-6)? 6 Sleep in

# user_num = raw_input("Pick a day between 0-6: ")
# gameOn = True
# day = {
#     "0" : "Sunday",
#     "1" : "Monday",
#     "2" : "Tuesday",
#     "3" : "Wednesday",
#     "4" : "Thursday",
#     "5" : "Friday",
#     "6" : "Saturday"
# }

# while (gameOn):
#     if (user_num == "6" or user_num == "0"):
#         print "Sleep In"
#         gameOn = False
#     else:
#         print "GO TO WORK!"
#         gameOn = False

# 6. Celsius to Fahrenheit
# Prompt the user for a number in degrees Celsius, and convert the value to 
# degrees in Fahrenheit and display it to the user. Example session:

# $ python degree_conversion.py Temperature in C? 28 82.4 F 
# $ python degree_conversion.py Temperature in C? -5 23 F

# Hint: the formula to convert degrees C to degrees F is: F = C x 1.8 + 32.

# celsius = int(raw_input("What's the temperature out in Celsius?: "))
# farenheit = (celsius * 1.8) + 32

# print farenheit

# 7. Tip Calculator
# Prompt the user for two things:

# The total bill amount:
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). 
# The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%
# Example session: $ python tip_calc.py Total bill amount? 100 Level of service? good Tip amount: $20.00 
# Total amount: $120.00 
# $ python tip_calc.py Total bill amount? 48 Level of service? bad 
# Tip amount: $4.80 Total amount: $52.80

# Hints:
# To format a float number as a dollar value, use Python's formatting syntax: "{:.2f}".format(amount)

# total_bill = int(raw_input("How much was your total bill? "))
# level_of_service = raw_input("Level of service? Good, fair or bad? ").lower()
# total_bill_with_tip = 0

# if (level_of_service == "good"):
#     tip_amount = (total_bill * .2)
#     print "Tip amount: " + str(tip_amount)
#     total_bill_with_tip = total_bill + tip_amount
#     print "Total amount with tip: "+ str(total_bill_with_tip)
# elif (level_of_service == "fair"):
#     tip_amount = (total_bill * .15)
#     print "Tip amount: " + str(tip_amount)
#     print "Total amount with tip: "+ str(total_bill_with_tip)
# else:
#     tip_amount = (total_bill * .1)
#     print "Tip amount: " + str(tip_amount)
#     print "Total amount with tip: "+ str(total_bill_with_tip)

# 8. Tip Calculator 2
# Allow the ability to divide the check into a equal parts amount a number of people. 
# The user will enter the number of people to be divided amongst. Example session:

# $ python tip_calc2.py Total bill amount? 100 Level of service? good Split how many ways? 5 
# Tip amount: $20.00 Total amount: $120.00 Amount per person: $24.00


# total_bill = int(raw_input("How much was your total bill? "))
# level_of_service = raw_input("Level of service? Good, fair or bad? ").lower()
# amount_of_people = int(raw_input("How many ways are you splitting the bill? "))
# total_bill_with_tip = 0

# if (level_of_service == "good"):
#     tip_amount = (total_bill * .2)
#     print "Tip amount: " + str(tip_amount)
#     total_bill_with_tip = total_bill + tip_amount
#     print "Total amount with tip: "+ str(total_bill_with_tip)
# elif (level_of_service == "fair"):
#     tip_amount = (total_bill * .15)
#     print "Tip amount: " + str(tip_amount)
#     print "Total amount with tip: "+ str(total_bill_with_tip)
# else:
#     tip_amount = (total_bill * .1)
#     print "Tip amount: " + str(tip_amount)
#     print "Total amount with tip: "+ str(total_bill_with_tip)

# split = (total_bill_with_tip / amount_of_people)

# print "Amount per person: " + str(split) 
# 9. 1 to 10
# Use a while loop to print the numbers from 1 to 10.

# $ python 1_to_10.py 1 2 3 4 5 6 7 8 9 10

# i = 0
# while i < 10:
#     i += 1
#     print i 


# 10. How many coins?
# Write a program that will prompt you for how many coins you want. 
# Initially you have no coins. It will ask you if you want a coin? 
# If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program. Example run:

# $ python coins.py You have 0 coins. 
# Do you want another? yes You have 1 coins. 
# Do you want another? yes You have 2 coins. 
# Do you want another? no Bye

how_many_coins = int(raw_input("How many coins do you want? "))
print "You have 0 coins currently"
coins = 0 

while coins < how_many_coins:
    answer = raw_input("Do you want another? ").lower()
    if (answer == "yes"):
        coins += 1
        print "You have " + str(coins) + " coins."
    else:
        print "BYE!"
        break

