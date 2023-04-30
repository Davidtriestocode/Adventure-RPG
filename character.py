import pygame
import random
import numpy as np

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
GRID_WIDTH = 200
GRID_HEIGHT = 200
TILE_SIZE = (20, 20)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# place the character on a random location on the grid
char_row, char_col = np.random.randint(10), np.random.randint(10)

# place the monster on a random location on the grid that is different from the player's location
while True:
    monster_row, monster_col = np.random.randint(10), np.random.randint(10)
    if monster_row != char_row or monster_col != char_col:
        break



# update the display window
pygame.display.flip()

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

# define the function to move the character
def move_character(dx, dy):
    global char_col, char_row
    new_col = char_col + dx
    new_row = char_row + dy
    if 0 <= new_col < GRID_WIDTH and 0 <= new_row < GRID_HEIGHT:
        char_col, char_row = new_col, new_row
    print(char_row, char_col)

    # update the character's position on the grid
    char_rect = pygame.Rect(char_col * TILE_SIZE[0], char_row * TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1])


# create a character with random attributes
char_attributes = {"Strength": np.random.randint(1, 101),
                   "Agility": np.random.randint(1, 101),
                   "Endurance": np.random.randint(1, 101),
                   "Intelligence": np.random.randint(1, 101),
                   "Magic": np.random.randint(1, 101),
                   "Attack": np.random.randint(1, 101),
                   "Defence": np.random.randint(1, 101),
                   "Experience Points": 0,
                   "Level": 0,
                   "Health Points": np.random.randint(1, 101),
                   "Stamina Points": np.random.randint(1, 101),
                   "Mana Points": np.random.randint(1, 101)}


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
                    

   
