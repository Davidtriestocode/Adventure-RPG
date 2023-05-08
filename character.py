import pygame
import random
import numpy as np

# place the character on a random location on the grid
char_row, char_col = np.random.randint(10), np.random.randint(10)

def level_up(char_attributes):
    # check if the character has enough experience points to level up
    if char_attributes["Experience Points"] >= 100:
        # level up the character
        char_attributes["Experience Points"] -= 100
        char_attributes["Level"] += 1
        
        # increase the character's attributes based on their current level
        char_attributes["Strength"] += 5
        char_attributes["Agility"] += 5
        char_attributes["Endurance"] += 5
        char_attributes["Intelligence"] += 5
        char_attributes["Magic"] += 5
        char_attributes["Attack"] += 5
        char_attributes["Defence"] += 5
        char_attributes["Health Points"] += 10
        char_attributes["Stamina Points"] += 10
        char_attributes["Mana Points"] += 10
        
        print(f"Congratulations! You have reached level {char_attributes['Level']}.")

# create a character with random attributes
char_attributes =  {
        "Strength": 10,
        "Agility": 10,
        "Endurance": 10,
        "Intelligence": 10,
        "Magic": 10,
        "Attack": 10,
        "Defence": 10,
        "Health Points": 10,
        "Stamina Points": 10,
        "Mana Points": 10
        }


   
