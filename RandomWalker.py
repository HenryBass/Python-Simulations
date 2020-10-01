import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("RandomWalker")

x = 400
y = 400
size = 1
run = True
r = random.randint(1, 255)
g = random.randint(1, 255)
b = random.randint(1, 255)
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(screen, (r, g, b), (x, y, size, size))

    i = [-1, 1]
    choice = random.choice(i)
    print('x + ' + str(choice))
    x = x + choice
    choice = random.choice(i)
    print('y + ' + str(choice))
    y = y + choice

    pygame.display.update()
