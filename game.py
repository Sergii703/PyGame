import pygame
import sys

from game_objects import Player, Background, Shoot
from settings import SIZE, WHITE

pygame.init()
pygame.display.set_caption("Space Invaders")

screen = pygame.display.set_mode(SIZE)  # импортируем настройки
clock = pygame.time.Clock()  # что бы быстро не перемещался

# отображение класса игрока
player = Player()  # присваеваем объекты к переменным
background = Background()
# shoot = Shoot()

# Группв создается для того чтобы не лписывать каждый объкет по отдельности
all_objects = pygame.sprite.Group()

all_objects.add(background)
all_objects.add(player)
all_objects.add(Shoot(player.rect.midtop))

while True:  # игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # обработка события
            sys.exit(0)  # завершение циклаб

    screen.fill(WHITE)  # изменение цвета экрана

    # player.update()
    # background.update()
    all_objects.update()

    # screen.blit(background.image, background.rect)  # отображение фона
    # screen.blit(player.image, player.rect)  # отображение игрока
    all_objects.draw(screen)  # что ьы не отображать по одному объекту сразу отображаем группу

    pygame.display.flip()
    clock.tick(30)  # скорость обновления экрана


