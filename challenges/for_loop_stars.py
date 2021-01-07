# Write a script that constructs the following pattern using a for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# BONUS- Come up with as many other methods to create this output as you can!



#!/usr/bin/env python3

# create a tracker for amount of stars to add
count = 1

# create a storage for the stars
result = []

# create a function that adds to count until input number is reached
def counting_up(top_num):
    # while count is less than top_num
    while count < top_num:
        # create a new holder array
        holder = []
        # loop to add number of stars equal to count
        for x in count:
            # add star to holder
            holder.append("*")
        # add holder to result
        result.append(holder)
        # increment count
        count += 1



# create a function that removes from count until count equals one
