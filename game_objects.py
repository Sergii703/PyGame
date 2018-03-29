import pygame

from settings import WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):  #класс игрока
    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.image.load('/home/kovals/PycharmProjects/PyGame/game/space.jpeg')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2  # его располодение
        self.rect.bottom = HEIGHT - 10  # его расположения

        def update(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:  # клавиша лево
                print('LEFT')
            elif keys[pygame.K_RIGHT]:  # клавиша право
                print('RIGHT')