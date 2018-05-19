# importujemy biblioteki
import pygame
import pyganim
import sys

# importujemy dane z obiektów
from game_objects import Player, Background, Meteorite
from settings import SIZE, WHITE

pygame.init()  # inicjalizacja i uruchamianie jądra pygame
pygame.display.set_caption("Space Invaders")  # nazwa ekranu głównego

screen = pygame.display.set_mode(SIZE)  # zmienna która przyjmuje główny ekran, importujemy CONSTANCE
clock = pygame.time.Clock()  # ogranicza częstotliwośc kadrów i żeby gracz nie szybko poruszał się w przestrzeni

# aniwacja wybuchu meteoryty za pomocą pygaim
explosion_animation = pyganim.PygAnimation([
    ('game/blue_explosion/1_{}.png'.format(i), 50) for i in range(17)
], loop=False)  # wybuch jednorazowy

# dodanie dzwięków
music = pygame.mixer.Sound('game/music/game.wav')
music.play(-1)  # żeby dzięk nigdy sie nie kończył

# metoda która pozwala lączyć obiekty/sprite w grupy dla tego żeby nie opisywać kazdy obiekt
# GRUPY
all_objects = pygame.sprite.Group()
shoots = pygame.sprite.Group()
meteors = pygame.sprite.Group()

explosions = []  # lista wybuchów

# OBIEKTY
player = Player(clock, shoots)
background = Background()

# musimy uważać na kolejnośc dodawania obiektów
all_objects.add(background)
all_objects.add(player)


while True:  # główny cykl gry
    for event in pygame.event.get():  # helper który pracuje nad wszystkimi eventami gry, metoda zwraca array wszystkich eventów
        if event.type == pygame.QUIT:  # przyklad wykonywania eventów, WYJSCIE z gry
            sys.exit(0)  # zakończenie cyklu

    # ważna jest kolejnść pokazywania obrazów na ekranie
    screen.fill(WHITE)  # zmiana koloru ekranu na biały

    Meteorite.process_meteorite(clock, meteors)

    all_objects.update()  # apdejtujemy wszystkie obiekty/eventy cyklu gry
    shoots.update()
    meteors.update()

    shoots_meteors_collided = pygame.sprite.groupcollide(meteors, shoots, True, True)  # lapiemy dwie grupy i zwracamy wszystkie столкновкния

    for collided in shoots_meteors_collided:  # dla kazdego obiektu które się spotkały
        explosion = explosion_animation.getCopy()  # tworzymy kopie animacji wybuchu
        explosion.play()  # odpalamy animacje wybuchu
        explosions.append((explosion, (collided.rect.center)))  # i dodajemy do listy wszystkich wybuchów

    # jezeli meteoryt i statek się spotkają to znikają oba
    player_and_Meteors_collided = pygame.sprite.spritecollide(player, meteors, True)
    if player_and_Meteors_collided:
        all_objects.remove(player)

    all_objects.draw(screen)  # żeby nie pokazywać/opisywać kazdy obiekt, podajemy grupe
    shoots.draw(screen)
    meteors.draw(screen)

    # bezposrednio sama animacja
    for explosion, position in explosions.copy():  # bierzemy wybuch z listy, nie można usuwać z oryginalu elementów listy, dlatego używamy kopie
        if explosion.isFinished():  # sprawdzamy czy wybuch już sie nie skończył
            explosions.remove((explosion, position))  # i usuwamy z listy/pamięci animacje/wybuch
        else:
            x, y = position  # jeżeli wybuch się nie skończył, to bierzemy go pozycje
            explosion.blit(screen, (x-128, y-128))  # pokazukjemy animacje na ekranie, odejmujemy polowe szerokości animacji

    pygame.display.flip()  # metoda która pokazuje końcowy wynik na główny ekran
    clock.tick(50)  # szybkośc odswiezenia kadrów na sekunde


