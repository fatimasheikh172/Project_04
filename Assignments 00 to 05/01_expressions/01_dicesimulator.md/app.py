
"""use variable scope"""
# global variable scope 
# local variable scope

import random

def dice_roll():
    """Stimulates rolling a six-sided die"""
    return random.randint(1 , 6)

def main():
    for i in range(3): # loop to dic in three times

        die1 = dice_roll()
        die2 = dice_roll()
        print(f"Roll {i+1}: Die 1 = {die1}, Die 2 = {die2}")  # Print results

# Required to call the main function
if __name__ == '__main__':
    main()