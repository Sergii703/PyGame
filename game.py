import pygame
import sys

from settings import SIZE, WHITE

pygame.init()
pygame.display.set_caption("Space Invaders")

screen = pygame.display.set_mode(SIZE)  # импортируем настройки

while True:  # игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # обработка события
            sys.exit(0)  # завершение цикла
    screen.fill(WHITE)  # изменение цвета экрана

    pygame.display.flip()



