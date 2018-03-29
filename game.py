import pygame
import sys

from game_objects import Player, Background
from settings import SIZE, WHITE

pygame.init()
pygame.display.set_caption("Space Invaders")

screen = pygame.display.set_mode(SIZE)  # импортируем настройки
clock = pygame.time.Clock()  # что бы быстро не перемещался



# отображение класса игрока
player = Player()
background = Background()

while True:  # игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # обработка события
            sys.exit(0)  # завершение циклаб

    screen.fill(WHITE)  # изменение цвета экрана

    player.update()
    background.update()

    screen.blit(background.image, background.rect)  # отображение фона
    screen.blit(player.image, player.rect)  # отображение игрока


    pygame.display.flip()
    clock.tick(30)  # скорость обновления экрана


