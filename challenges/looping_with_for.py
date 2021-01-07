#!/usr/bin/env python3


farms = [
{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
{"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}
]

requested_farm = input("Which farm would you like: NE Farm, W Farm, SE Farm?")


for farm in farms:
    if farm["name"] == requested_farm:
        print(farm["agriculture"])
