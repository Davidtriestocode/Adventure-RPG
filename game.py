import pygame
import random
import time

# D - python is not searching in the folder for modules you can see what folders are being checked with sys.path.
import sys
print("- SYS.PATH - ")
print(sys.path)

# D - to get the current working directory we can use os.getcwd()
import os
print("- Currenct Working Directory (cwd) -")
print(os.getcwd ())

# D - To get python to search for modules you can add the path with sys.path.append()
sys.path.append(os.getcwd())

import character
# D - deleted monster_col and monster_row from imports as they do not exist.
from character import level_up, char_attributes, char_col, char_row
import monster
import numpy as np
from combat import combat
import settings

# Initialize Pygame
pygame.init()

# Set up the display

WINDOW_WIDTH = settings.WINDOW_WIDTH
WINDOW_HEIGHT = settings.WINDOW_HEIGHT
BAR_HEIGHT = settings.BAR_HEIGHT
TILE_SIZE = settings.TILE_SIZE
GRID_WIDTH = settings.GRID_WIDTH
GRID_HEIGHT = settings.GRID_HEIGHT
FONT_SIZE = settings.FONT_SIZE

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up fonts
font = pygame.font.SysFont(None, FONT_SIZE)

# D - relative paths are better as they will work when you move the whole folder from one place to another.
map_image = pygame.image.load("shadowquestmap.jpg")
#map_image = pygame.image.load("C:\\Users\\User\\Downloads\\shadowquestmap.jpg")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up character stats
health = 100
stamina = 100
mana = 100

# Define functions

def draw_bar(color, x, y, value, height):
    """
    Draw a bar with the given color, x-coordinate, y-coordinate, value, and height.
    """
    bar_width = 100
    bar_fill_width = int((value / 100) * bar_width)
    
    pygame.draw.rect(window, BLACK, (x, y, bar_width, height))
    pygame.draw.rect(window, color, (x + 2, y + 2, bar_fill_width, height - 4))



def update_stats_text():
    """
    Update and draw the text for the character stats.
    """
    health_text = font.render(f'Health: {health}', True, WHITE)
    stamina_text = font.render(f'Stamina: {stamina}', True, WHITE)
    mana_text = font.render(f'Mana: {mana}', True, WHITE)
    
    window.blit(health_text, (10, 0))
    window.blit(stamina_text, (120, 0))
    window.blit(mana_text, (230, 0))


def draw_map(map_image):
    """
    Draw the map image on the screen.
    """
    window.blit(map_image, (0, 0))

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
    
    # add a time delay of 0.2 seconds
    time.sleep(0.2)
    
    
def game_loop():
    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            move_character(0, -1)
        if keys[pygame.K_DOWN]:
            move_character(0, 1)
        if keys[pygame.K_LEFT]:
            move_character(-1, 0)
        if keys[pygame.K_RIGHT]:
            move_character(1, 0)

        # Check for combat
        if char_row == monster.monster_row and char_col == monster.monster_col:
            if combat(char_attributes, monster_attributes):
                # Spawn a new monster at a random location on the grid
                while True:
                    new_monster_row, new_monster_col = np.random.randint(10), np.random.randint(10)
                    if new_monster_row != char_row or new_monster_col != char_col:
                        break
                monster.monster_row, monster.monster_col = new_monster_row, new_monster_col
            else:
                # Game over
                running = False

        # Draw the map
        draw_map(map_image)

        # Draw the character and monster
        char_color = (0, 0, 255)
        char_rect = pygame.Rect(char_col * TILE_SIZE[0], char_row * TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1])
        pygame.draw.rect(window, char_color, char_rect)

        monster_color = (255, 0, 0)
        monster_rect = pygame.Rect(monster_col * TILE_SIZE[0], monster.monster_row * TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1])
        pygame.draw.rect(window, monster_color, monster_rect)

        # Draw character stats
        draw_bar(RED, 10, 0, health, BAR_HEIGHT)
        draw_bar(GREEN, 120, 0, stamina, BAR_HEIGHT)
        draw_bar(BLUE, 230, 0, mana, BAR_HEIGHT)

        update_stats_text()

        # Update the display
        pygame.display.update()
        
    
# Quit Pygame
pygame.quit()








