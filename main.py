import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Simple")
icon = pygame.image.load("img/download.JPG")

running = True
while running:
    pass

pygame.quit()