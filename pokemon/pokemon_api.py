#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():

    print("Welcome to the game of Pokemon Easy! Here, you don't have to work hard to catch your favorite Pokemon! All you have to do is enter a number, and we'll catch the Pokemon for you!")

    while True:
        continue_playing = ""
        pokeapi = {}

        while True:
            numbers_selected = {}
            choice_input = ""
            
            # Right now this code input is broken and continues to repeat itself after an input is entered. I have tried try: except:.
            # Latest effort was adding a break directly after the input to see if it was my conditionals, but input still repeats.
            choice_input = input("Please enter a number between 1-150:").strip()
            break

            if choice_input in numbers_selected:
                #If time allows, build a feature to print the numbers already selected
                print("Number already used, please select a new number.")
                choice_input = ""
                break
            elif int(choice_input) < 1 or int(choice_input) > 150:
                print("Number must not be less than 1 or greater than 150.")
                break
            else:
                numbers_selected[choice_input] = choice_input
                pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{choice_input}").json()
                break

    print(f"You have chosen {pokeapi['name']} that has appeared in {len(pokeapi['game_indicies'])} games!")
    print(f"If you have never seen a {pokeapi['name']} before, use the following link to see your new Pokemon!")
    print(pokeapi['sprites']['front_default'])
    
    continue_playing = input("Would you like to catch another, or would you like to quit? Enter 'y' for continue or 'n' to quit").strip()

    if continue_playing == "n":
        print("Thank you for playing! See you next time!")
        return
    else:
        print("I knew I could count on you to catch 'em all!")

main()
