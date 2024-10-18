import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
background_color = (255, 255, 255)
default_width = 1
default_color = (0, 0, 0)
screen.fill(background_color)
pygame.display.update()

while True:
    input_text = input()
    if input_text.startswith("change size"):
        default_width = int(input_text.split(" ")[-1])
    elif input_text.startswith("change color"):
        default_color = (
            int(input_text.split(" ")[-3]),
            int(input_text.split(" ")[-2]),
            int(input_text.split(" ")[-1]),
        )
    elif input_text.startswith("draw line"):
        pygame.draw.line(
            screen,
            default_color,
            (int(input_text.split(" ")[-4]), int(input_text.split(" ")[-3])),
            (int(input_text.split(" ")[-2]), int(input_text.split(" ")[-1])),
            default_width,
        )
        pygame.display.update()
    elif input_text.startswith("draw circle"):
        pygame.draw.circle(
            screen,
            default_color,
            (int(input_text.split(" ")[-3]), int(input_text.split(" ")[-2])),
            int(input_text.split(" ")[-1]),
            default_width,
        )
        pygame.display.update()
    elif input_text.startswith("draw polygon"):
        text = input_text.split("polygon")[-1].strip().split(" ")
        list_points = list()
        for i in range(0, len(text) - 1, 2):
            x = int(text[i])
            y = int(text[i + 1])
            list_points.append((x, y))
        if len(list_points) >= 3:
            pygame.draw.polygon(screen, default_color, list_points, default_width)
            pygame.display.update()
    elif input_text == "end drawing":
        break

pygame.image.save(screen, "draw.png")
