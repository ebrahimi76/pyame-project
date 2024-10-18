import pygame
from math import pi

pygame.init()
screen = pygame.display.set_mode((800, 600))

# colors
red = (252.2, 0, 0)
blue = (0, 0, 255)
amber = (100, 75, 0)
aqua = (0, 100, 100)
bittersweet = (100, 44, 37)
green = (0, 255, 0)
aero_blue = (75, 91, 84)
gray = (128, 128, 128)

screen.fill(gray)

# line
pygame.draw.line(screen, red, (300, 300), (600, 400), 10)

# lines
pygame.draw.lines(screen, amber, False, [(700, 350), (600, 350), (550, 300), (650, 290)], 8)

# circle
pygame.draw.circle(screen, blue, (200, 200), 20, 4)

# rect
pygame.draw.rect(screen, aqua, (400, 400, 30, 80), 6)

# ellipse
pygame.draw.ellipse(screen, bittersweet, (450, 450, 100, 50), 9)

# polygon
pygame.draw.polygon(screen, green, [(700, 500), (600, 500), (550, 450), (650, 440)], 11)

# arc
pygame.draw.arc(screen, aero_blue, (210, 75, 150, 125), 3 * pi / 2, 2 * pi, 15)

pygame.display.update()

while True:
    pygame.event.pump()
