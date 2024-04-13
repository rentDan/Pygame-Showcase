from os import scandir
import pygame
import sys
from pygame.locals import *

"""
TODO: Add description inside of the game
    Tell them to move the cursor around
    Tell them to click the left mouse button
    Tell them how to exit the game
"""


def runGame3():
    # Initialize Pygame
    pygame.init()

    # Set up the window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Cursor Example")

    # Set up colors
    white = (255, 255, 255)
    red = (255, 0, 0)

    # Set up the clock
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        
        screen.fill(white)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor_pos = pygame.mouse.get_pos()
                    
                    pygame.draw.circle(screen, red, cursor_pos, 10)

        # Get the position of the cursor
        cursor_pos = pygame.mouse.get_pos()

        # Draw the cursor position
        pygame.draw.circle(screen, red, cursor_pos, 5)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

