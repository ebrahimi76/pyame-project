import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
print(type(screen))

while True:
    pygame.event.pump()