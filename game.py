import pygame
import sys

from game_objects import Player
from settings import SIZE, WHITE

pygame.init()
pygame.display.set_caption("Space Invaders")

screen = pygame.display.set_mode(SIZE)  # импортируем настройки

# отображение класса игрока
player = Player()


while True:  # игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # обработка события
            sys.exit(0)  # завершение циклаб

    screen.fill(WHITE)  # изменение цвета экрана

    player.update()

    screen.blit(player.image, player.rect)  # отображение игрока

    pygame.display.flip()



