# from pprint import pprint

import pygame

# print(type(pygame.image))
#
# pprint(dir(pygame.image))
#
img = pygame.image.load("sq.png")
# print(type(img))

yellow = (255, 255, 0)
screen = pygame.display.set_mode((640, 480))
screen.fill(yellow)

# x, y = 0, 0
#
# while True:
#     screen.fill(yellow)
#     screen.blit(img, (x, y))  # load image
#     x, y = x + 1, y + 1
#     if y > 640:
#         x, y = 0, 0
#     pygame.display.update()
#     pygame.time.delay(5)
#     pygame.event.pump()

# dx, dy = map(int, input().split())
# t = int(input())
#
# purple = (128, 0, 128)
# screen.fill(purple)
#
# for i in range(t):
#     screen.fill(purple)
#     screen.blit(img, (x, y))
#     x, y = x + dx, y + dy
#
# pygame.image.save(screen, "out.png")

size = img.get_rect().size
pic_string = pygame.image.tostring(img, "RGB")
img2 = pygame.image.fromstring(pic_string, size, "RGB")
pygame.image.save(img2, "out.png")
