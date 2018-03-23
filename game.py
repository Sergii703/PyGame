import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Space Invaders")

while True:  # игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # обработка события
            sys.exit(0)  # завершение цикла




