import pygame

# Initialize pygame
pygame.init()

# Create a font object
font = pygame.font.SysFont("comicsansms", 30)

# Render text
text_surface = font.render("Hello, Pygame!", True, (255, 0, 0))

# Now you can blit this text surface onto your game window or another surface
