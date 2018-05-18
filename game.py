# importujemy biblioteki
import pygame
import sys

# importujemy dane z obiektów
from game_objects import Player, Background, Shoot
from settings import SIZE, WHITE

pygame.init()  # inicjalizacja i uruchamianie jądra pygame
pygame.display.set_caption("Space Invaders")  # nazwa ekranu głównego

screen = pygame.display.set_mode(SIZE)  # zmienna która przyjmuje główny ekran, importujemy CONSTANCE
clock = pygame.time.Clock()  # ogranicza częstotliwośc kadrów i żeby gracz nie szybko poruszał się w przestrzeni

# metoda która pozwala lączyć obiekty/sprite w grupy dla tego żeby nie opisywać kazdy obiekt
all_objects = pygame.sprite.Group()
shoots = pygame.sprite.Group()

# Obiekty gry
player = Player(clock, shoots)
background = Background()

# musimy uważać na kolejnośc dodawania obiektów
all_objects.add(background)
all_objects.add(player)
# all_objects.add(Shoot(player.rect.midtop))

while True:  # główny cykl gry
    for event in pygame.event.get():  # helper który pracuje nad wszystkimi eventami gry, metoda zwraca array wszystkich eventów
        if event.type == pygame.QUIT:  # przyklad wykonywania eventów, WYJSCIE z gry
            sys.exit(0)  # zakończenie cyklu

    # ważna jest kolejnść pokazywania obrazów na ekranie
    screen.fill(WHITE)  # zmiana koloru ekranu na biały

    all_objects.update()  # updejtijemy wszystkie obiekty/eventy cyklu gry
    shoots.update()

    all_objects.draw(screen)  # żeby nie pokazywać/opisywać kazdy obiekt, podajemy grupe
    shoots.draw(screen)

    pygame.display.flip()  # metoda która pokazuje końcowy wynik na główny ekran
    clock.tick(50)  # szybkośc odswiezenia kadrów na sekunde


