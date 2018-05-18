# import bibliotek
import random
import pygame

from settings import WIDTH, HEIGHT


# klas strzal i jego obraz (Sprite)
class Shoot(pygame.sprite.Sprite):
    speed = -15  # szybkość strzału

    # konstruktor
    def __init__(self, position):
        super(Shoot, self).__init__()

        self.image = pygame.image.load('../PyGame/game/shoot.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = position  # pozycja w której musi się pojawiać kula

    # metoda żeby kula nie stala na miejscu
    def update(self):
        self.rect.move_ip((0, self.speed))  # nie bedzie zmieniać swojej pozycji po X, tylko po Y= -15


# klas gracza i jego obraz (Sprite)
class Player(pygame.sprite.Sprite):
    max_speed = 10  # szybkość ruchu gracza
    shooting_cooldown = 180  # przerwy miedzy strzelaniem

    def __init__(self, clock, shoots):  # konstruktor, "self" jest linkiem na sam obiekt
        super(Player, self).__init__()

        # atrybuty wewnętrzne
        self.clock = clock
        self.shoots = shoots

        self.image = pygame.image.load('../PyGame/game/player.png')  # ladujemy obraz gracza
        self.rect = self.image.get_rect()  # rozmiar gracza, który równa się obrazu gracza

        # koordynaty gracza
        self.rect.centerx = WIDTH / 2  # na polowie ekranu
        self.rect.bottom = HEIGHT - 10  # od dolu głównego ekranu

        self.current_speed = 0  # szybkość na dany moment

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

        self.rect.move_ip((self.current_speed, 0))  # metoda która pozwala wprowadzać относительное смещение

        self.process_shooting()

    # metoda która umożliwia strzelanie
    def process_shooting(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.current_shooting_cooldown <= 0:  # jaki przycisk odpowiada za strzelanie oraz ograniczenie strzelanie za jednym razem
            self.shoots.add(Shoot(self.rect.midtop))  # przekazujemy koordynaty gracza
            self.current_shooting_cooldown = self.shooting_cooldown  # częstotliwość strzelania
        else:
            self.current_shooting_cooldown -= self.clock.get_time()  # zmniejszamy cooldown do poprzedniej pozycji

        for shoot in list(self.shoots):
            if shoot.rect.bottom < 0:
                self.shoots.remove(shoot)


# klas fonu i jego obraz (Sprite)
class Background (pygame.sprite.Sprite):
    # konstruktor
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load('../PyGame/game/background.png')
        self.rect = self.image.get_rect()  # rozmiar i miejsce fonu
        self.rect.bottom = HEIGHT

    # tworzymy illuzje poruszanie się w przestrzeni
    def update(self):
        self.rect.bottom += 5  # szybkość

        # warunek, jeżeli background się skończyl, żeby on zaczynał się od początku
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
