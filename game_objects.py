import pygame

from settings import WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):  #класс игрока
    def _init_(self):
        super(Player, self).__init__()

        self.image = pygame.image.load('game/space.jpeg')
        self.rect = self.image.get_rect()

        self.rect.conterx = WIDTH / 2  # его располодение
        self.rect.bottom = HEIGHT - 10  # его расположения