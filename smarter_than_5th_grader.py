#!/usr/bin/env python3

#Variables needed
player_name = " "
points = 0
answer = 0

# Allow user to set name
player_name = input("What is your name, child?")

# Welcome Player
print(f"Welcome to Are You Smarter Than a Fifth Grader, {player_name}! I am your host, Jeff Foxworthy. If you don't know who I am, we already know that you are not smarter than a fifth grader. Let's get started with our first question!")

# Question 1
print("If a car is traveling at 40 MPH, how long will it take to go 190 miles?")
print("1.) 4 Hours, 45 Minutes")
print("2.) 3 Hours, 30 Minutes")
print("3.) 4 Hours, 15 Minutes")
print("4.) 3 Hours, 15 Minutes")

# Loop until proper answer is given
while True:
    answer = input("Please enter 1, 2, 3, or 4 for your answer:")

    if answer == "1":
        print("That is correct! Lucky guess, I suppose.")
        points += 1
        break
    elif answer == "2":
        print("No... Just no.")
        break
    elif answer == "3":
        print("You're about thirty minutes early on that one.")
        break
    elif answer == "4":
        print("Please go back to your elementary school and tell your math teacher that they failed.")
        break
    else:
        print("Please enter 1, 2, 3, or 4. If you can't get this, you are not smarter than a three year old.")


# Question 2
print("How many nouns are in the following sentence: 'The rabbit ran to the cafeteria and ate a big salad.'?")
print("1.) Two")
print("2.) Three")
print("3.) Four")
print("4.) Five")

# Loop until proper answer is given
while True:
    answer = input("Please enter 1, 2, 3, or 4 for your answer:")

    if answer == "1":
        print("Close, but still not smarter than a fifth grader.")
        break
    elif answer == "2":
        print("Wow, you can count nouns!")
        points += 1
        break
    elif answer == "3":
        print("Welp, that doesn't seem to be correct here.")
        break
    elif answer == "4":
        print("Did you have to count with your fingers for that incorrect answer?")
        break
    else:
        print("Please enter 1, 2, 3, or 4. This is the second question, and you still haven't figured it out.")


# Question 3
print("What unit of measurement is abbreviated 'oz'?")
print("1.) Ounces")
print("2.) Pounds")
print("3.) Liters")
print("4.) Oblongs")

# Loop until proper answer is given
while True:
    answer = input("Please enter 1, 2, 3, or 4 for your answer:")

    if answer == "1":
        print("Great work on sounding out the word, just to be sure.")
        points += 1
        break
    elif answer == "2":
        print("Bloody hell!... Sorry, I've been hanging out with Gordon too long. Still incorrect though.")
        break
    elif answer == "3":
        print("There isn't even an 'O' in this one...")
        break
    elif answer == "4":
        print("Next question - describe oblongs to me. just kidding, you don't even know about ounces.")
        break
    else:
        print("Please enter 1, 2, 3, or 4. Are we getting dumber by the question?")



# Question 4
print("True or false? The Human shoulder is a ball-and-socket joint?")
print("1.) True")
print("2.) False")

# Loop until proper answer is given
while True:
    answer = input("Please enter 1 or 2 for your answer:")

    if answer == "1":
        print("You paid extra attention during human anatomy, didn't you?")
        points += 1
        break
    elif answer == "2":
        print("Get out.")
        break
    else:
        print("Please enter 1 or 2. I really don't get paid enough for this.")



# Question 5
print("Which one of the following is a mammal?")
print("1.) Seahorse ")
print("2.) Sea Lion")
print("3.) Sea Urchin")

# Loop until proper answer is given
while True:
    answer = input("Please enter 1, 2, or 3 for your answer:")

    if answer == "1":
        print("Have you ever visited the zoo before?")
        break
    elif answer == "2":
        print("You saw lion and knew that had to be it, didn't you?")
        points += 1
        break
    elif answer == "3":
        print("I'll take no for $200.")
        break
    else:
        print("For the love of fifth graders, please enter 1, 2, or 3.")




# Question 6
print("Which continent is least populated?")
print("1.) Asia")
print("2.) Antarctica")
print("3.) Australia")
print("4.) Europe")

# Loop until proper answer is given
while True:
    answer = input("Please enter 1, 2, 3, or 4 for your answer:")

    if answer == "1":
        print("China and India have billions of people in just those two countries alone. No.")
        break
    elif answer == "2":
        print("Good thing you didn't freeze on this one!")
        points += 1
        break
    elif answer == "3":
        print("Nope! Try again! Just kidding, that was your only shot at the question.")
        break
    elif answer == "4":
        print("I really do not like you. No.")
        break
    else:
        print("Please enter 1, 2, 3, or 4. I'll be in the john while we wait for you to understand the rules to this game.")



if points == 6:
    print(f"Well, you made it to the finish line with {points} correct answers, {player_name}. You are just as smart as a fifth grader, but not smarter. Never forget that.")
else:
    print(f"Really {player_name}? Really? Go home. Get out of my face. You are not smarter than a fifth grader.")
