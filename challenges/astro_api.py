#!/usr/bin/env python3


# imports always go at the top of your code
import requests

def main():
    ## create r, which is our request object
    r = requests.get('http://api.open-notify.org/astros.json').json()
    
    print("People in space:", r["number"])

    for astro in r["people"]:
       # print(astro.get("name"))  # the .get() method returns NONE if key not found
        print(astro.get('name'), "on the", astro.get('craft'))

main()

