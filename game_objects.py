import pygame

from settings import WIDTH, HEIGHT


class Shoot(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Shoot, self).__init__()

        self.image = pygame.image.load('/home/kovals/PycharmProjects/PyGame/game/shoot.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = position


class Player(pygame.sprite.Sprite):  # класс игрока

    max_speed = 10

    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.image.load('/home/kovals/PycharmProjects/PyGame/game/spaceShip.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2  # его располодение
        self.rect.bottom = HEIGHT - 10  # его расположения

        self.current_speed = 0

    def update(self):  # функция перемещения игрока
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:  # клавиша лево
            self.current_speed = -self.max_speed
        elif keys[pygame.K_RIGHT]:  # клавиша право
            self.current_speed = self.max_speed
        else:
            self.current_speed = 0

        self.rect.move_ip((self.current_speed, 0))


class Background (pygame.sprite.Sprite):  # фон
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load('/home/kovals/PycharmProjects/PyGame/game/stars.png')
        self.rect = self.image.get_rect()  # размер и располодение фона

        self.rect.bottom = HEIGHT

    def update(self):  # иллюзия движения
        self.rect.bottom += 5

        if self.rect.bottom >= self.rect.height:
            self.rect.bottom = HEIGHT
