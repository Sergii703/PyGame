# import bibliotek
import random
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


# klas gracza i jego obraz (Sprite)
class Player(pygame.sprite.Sprite):
    max_speed = 10  # скорость игока
    shooting_cooldown = 150

    def __init__(self, clock, shoots):  # konstruktor, "self" jest linkiem na sam obiekt
        super(Player, self).__init__()

        self.clock = clock
        self.shoot = shoots

        self.image = pygame.image.load('../PycharmProjects/PyGame/game/spaceShip.jpg')  # ladujemy obraz gracza
        self.rect = self.image.get_rect()  # rozmiar gracza, który równa się obrazu gracza

        # koordynaty gracza
        self.rect.centerx = WIDTH / 2  # na polowie ekranu
        self.rect.bottom = HEIGHT - 10  # od dolu głównego ekranu

        # szybkość
        self.current_speed = 0

        self.current_shooting_cooldown = 0

    # pracujemy nad inputem od usera
    def update(self):
        keys = pygame.key.get_pressed()  # lapiemy przyciski które wciska user

        if keys[pygame.K_LEFT]:  # przycisk w levo
            self.current_speed = -self.max_speed  # szybkość
        elif keys[pygame.K_RIGHT]:  # przycik w prawo
            self.current_speed = self.max_speed
        else:
            self.current_speed = 0  # jezeli nic nie było wciśnięte gracz stoi na miejscu

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
    speed = 10

    def __init__(self):
        super(Meteorite, self).__init__()

        image_name = 'game/meteorit{}.jpg'.format(random.randint(1, 11))
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

        self.rect.midbottom = (random.randint(0, WIDTH), 0)

    def update(self):
        self.rect.move_ip((0, self.speed))
