import pygame
import random
import numpy as np
from character import char_col, char_row

# place the monster on a random location on the grid that is different from the player's location
while True:
    monster_row, monster_col = np.random.randint(10), np.random.randint(10)
    if monster_row != char_row or monster_col != char_col:
        break

# create a monster with random attributes
monster_attributes = {"Strength": np.random.randint(1, 101),
                      "Agility": np.random.randint(1, 101),
                      "Endurance": np.random.randint(1, 101),
                      "Intelligence": np.random.randint(1, 101),
                      "Magic": np.random.randint(1, 101),
                      "Attack": np.random.randint(1, 101),
                      "Defence": np.random.randint(1, 101),
                      "Health Points": np.random.randint(1, 101),
                      "Stamina Points": np.random.randint(1, 101),
                      "Mana Points": np.random.randint(1, 101)}
                    

