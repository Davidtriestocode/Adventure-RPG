import pygame
import random
import character
from character import move_character, level_up, char_attributes, monster_attributes, monster_row, monster_col
import numpy as np
from combat import combat

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
BAR_HEIGHT = 20
TILE_SIZE = (20, 20)
GRID_WIDTH = 200
GRID_HEIGHT = 200
FONT_SIZE = 16

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up fonts
font = pygame.font.SysFont(None, FONT_SIZE)

map_image = pygame.image.load("C:\\Users\\User\\Downloads\\shadowquestmap.jpg")

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

# place the character on a random location on the grid
char_row, char_col = np.random.randint(10), np.random.randint(10)

# place the monster on a random location on the grid that is different from the player's location
while True:
    monster_row, monster_col = np.random.randint(10), np.random.randint(10)
    if monster_row != char_row or monster_col != char_col:
        break

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
    if char_row == monster_row and char_col == monster_col:
        if combat(char_attributes, monster_attributes):
            # Spawn a new monster at a random location on the grid
            while True:
                new_monster_row, new_monster_col = np.random.randint(10), np.random.randint(10)
                if new_monster_row != char_row or new_monster_col != char_col:
                    break
            monster_row, monster_col = new_monster_row, new_monster_col
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
    monster_rect = pygame.Rect(monster_col * TILE_SIZE[0], monster_row * TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1])
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






