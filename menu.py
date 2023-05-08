import pygame
from character import char_attributes
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
screen = settings.screen

def character_creation_screen(screen, class_name):
    # Set up the font
    font = pygame.font.SysFont(None, 48)
    # Set up the buttons
    plus_symbol = font.render("+", True, (255, 255, 255))
    minus_symbol = font.render("-", True, (255, 255, 255))
    buttons = []
    for i, (attribute, value) in enumerate(char_attributes.items()):
        button = {
            "name": attribute,
            "value": value,
            "pos": (50, 50 + 60 * i),
            "plus_rect": pygame.Rect(200, 50 + 60 * i, 30, 30),
            "minus_rect": pygame.Rect(240, 50 + 60 * i, 30, 30),
            "plus_pressed": False,
            "minus_pressed": False
        }
        buttons.append(button)

    # Set up the pool of points
    points_left = 100

    return buttons, font, plus_symbol, minus_symbol, points_left

class_name = "Wizard"
buttons, font, plus_symbol, minus_symbol, points_left = character_creation_screen(screen, class_name)

# Main loop
while True:
    # Draw the buttons
    screen.fill((0, 0, 0))
    for button in buttons:
        text_surface = font.render(button["name"], True, (255, 255, 255))
        rect = text_surface.get_rect()
        rect.topleft = button["pos"]
        screen.blit(text_surface, rect)
        screen.blit(plus_symbol, button["plus_rect"].topleft)
        screen.blit(minus_symbol, button["minus_rect"].topleft)

        # Draw the value of the attribute
        value_surface = font.render(str(button["value"]), True, (255, 255, 255))
        value_rect = value_surface.get_rect()
        value_rect.topright = (190, button["pos"][1])
        screen.blit(value_surface, value_rect)

    # Draw the points pool
    pygame.draw.rect(screen, (255, 255, 255), (50, 500, 200, 30))
    pygame.draw.rect(screen, (0, 0, 255), (50, 500, 200 * points_left / 100, 30))

    # Update the screen
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Quit the game
                pygame.quit()
                exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()

            # Check if the mouse click is on one of the buttons
            for button in buttons:
                if button["plus_rect"].collidepoint(pos):
                    if not button["plus_pressed"] and points_left > 0:
                        button["plus_pressed"] = True
                        points_left -= 1
                        button["value"] += 1
                    elif button["plus_pressed"]:
                        button["plus_pressed"] = False
                        points_left += 1
                        button["value"] -= 1
                elif button["minus_rect"].collidepoint(pos):
                    if not button["minus_pressed"] and button["value"] > 0:
                        button["minus_pressed"] = True
                        points_left += 1
                        button["value"] -= 1
                    elif button["minus_pressed"]:
                        button["minus_pressed"] = False
                        points_left -= 1
                        button["value"] += 1

        elif event.type == pygame.MOUSEBUTTONUP:
            # Reset the button pressed flags
            for button in buttons:
                button["plus_pressed"] = False
                button["minus_pressed"] = False




def display_character_options(screen):
    # Set up the font
    font = pygame.font.SysFont(None, 48)

    # Load character images
    wizard_image = pygame.image.load("MagicUser.jpg")
    wizard_rect = wizard_image.get_rect(center=(WINDOW_WIDTH/4, WINDOW_HEIGHT/2))
    rogue_image = pygame.image.load("Thief.jpg")
    rogue_rect = rogue_image.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    fighter_image = pygame.image.load("Fighter.jpg")
    fighter_rect = fighter_image.get_rect(center=(WINDOW_WIDTH*3/4, WINDOW_HEIGHT/2))

    # Set up the class images and options
    class_images = [
        (wizard_image, wizard_rect, "Wizard"),
        (rogue_image, rogue_rect, "Rogue"),
        (fighter_image, fighter_rect, "Fighter")
    ]
    options = [option[2] for option in class_images]

    # Display the class images
    for image, rect, class_name in class_images:
        screen.blit(image, rect)

    # Update the screen
    pygame.display.flip()

    # Handle events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Quit the game
                    pygame.quit()
                    exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                pos = pygame.mouse.get_pos()

                # Check if the mouse click is on one of the class images
                for image, rect, class_name in class_images:
                    if rect.collidepoint(pos):
                        return class_name  # Return the selected class name



def main_menu():
    # Set up the window
    WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Main Menu")

    # Set up the font
    font = pygame.font.SysFont(None, 48)

    # Set up the menu options
    options = [
        ("Start New Game", (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100)),
        ("Load Game", (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 50)),
        ("Quit Game", (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 )),
    ]

    # Main menu loop
    while True:
        # Draw the menu options
        screen.fill((0, 0, 0))
        for option_text, option_pos in options:
            text_surface = font.render(option_text, True, (255, 255, 255))
            rect = text_surface.get_rect()
            rect.center = option_pos
            screen.blit(text_surface, rect)

        # Update the screen
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Quit the game
                    pygame.quit()
                    exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                pos = pygame.mouse.get_pos()

                # Check if the mouse click is on one of the options
                for option_text, option_pos in options:
                    text_surface = font.render(option_text, True, (255, 255, 255))
                    rect = text_surface.get_rect()
                    rect.center = option_pos

                    # If the mouse click is on the "Start New Game" option, display character options
                    if option_text == "Start New Game" and rect.collidepoint(pos):
                        display_character_options(screen)

        # Draw the menu options
        screen.fill((0, 0, 0))
        for option_text, option_pos in options:
            text_surface = font.render(option_text, True, (255, 255, 255))
            rect = text_surface.get_rect()
            rect.center = option_pos
            screen.blit(text_surface, rect)


    # Update the screen
    pygame.display.flip()

