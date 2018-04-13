import pygame

from settings import WIDTH, HEIGHT


class Shoot(pygame.sprite.Sprite):
    speed = -5  # скорость выстрела

    def __init__(self, position):
        super(Shoot, self).__init__()

        self.image = pygame.image.load('/home/kovals/PycharmProjects/PyGame/game/shoot.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = position

    def update(self):
        self.rect.move_ip((0, self.speed))


class Player(pygame.sprite.Sprite):  # класс игрок
    max_speed = 10  # скорость игока
    shooting_cooldown = 150

    def __init__(self, clock, shoots):
        super(Player, self).__init__()

        self.clock = clock
        self.shoot = shoots

        self.image = pygame.image.load('/home/kovals/PycharmProjects/PyGame/game/spaceShip.jpg')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2  # его располодение
        self.rect.bottom = HEIGHT - 10  # его расположения

        self.current_speed = 0

        self.current_shooting_cooldown = 0

    def update(self):  # функция перемещения игрока
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:  # клавиша лево
            self.current_speed = -self.max_speed
        elif keys[pygame.K_RIGHT]:  # клавиша право
            self.current_speed = self.max_speed
        else:
            self.current_speed = 0

        self.rect.move_ip((self.current_speed, 0))

        self.process_shooting()

    def process_shooting(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.current_shooting_cooldown <= 0:  # ограничываем возможность стрельбы
            self.shoots.add(Shoot(self.rect.midtop))
            self.current_shooting_cooldown = self.shooting_cooldown
        else:
            self.current_shooting_cooldown -= self.clock.get_time()

        for shoot in list(self.shoots):
            if shoot.rect.bottom < 0:
                self.shoots.remove(shoot)


class Background (pygame.sprite.Sprite):  # фон
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load('game/12.jpg')
        self.rect = self.image.get_rect()  # размер и расположение фона

        self.rect.bottom = HEIGHT

    def update(self):  # иллюзия движения
        self.rect.bottom += 5

        if self.rect.bottom >= self.rect.height:
            self.rect.bottom = HEIGHT


class Meteorite(pygame.sprite.Sprite):  # класс для метеоритов
    cooldown = 250
    current_cooldown = 0

    def __init__(self):
        super(Meteorite, self).__init__()
