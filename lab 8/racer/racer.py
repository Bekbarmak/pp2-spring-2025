import pygame, sys
from pygame.locals import *
import random, time

# ИНИЦИАЛИЗАЦИЯ
pygame.init()

# СТАВИМ ФПС
FPS = 60
FramePerSec = pygame.time.Clock()

# СОЗДАЕМ ЦВЕТА
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ПРОЧИЕ ПЕРЕМЕННЫЕ НУЖНЫЕ ДЛЯ ПРОГРАММЫ
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # Количество монет

# СТАВИМ ШРИФТЫ
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# СОЗДАЕМ ЭКРАН
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


# СОЗДАЕМ СПРАЙТЫ
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# КЛАСС МОНЕТЫ
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")  
        self.image = pygame.transform.smoothscale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# СОЗДАЕМ СПРАЙТЫ
P1 = Player()
E1 = Enemy()
C1 = Coin()

# СОЗДАЕМ ГРУППЫ СПРАЙТОВ
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# СОЗДАНИЕ НОВОГО СОБЫТИЯ ПОЛЬЗОВАТЕЛЯ
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# ЦИКЛ ИГРЫ В КОТОРОМ ВСЕ ПРОИСХОДИТ
while True:
    # ПРОХОДИТСЯ ПО ВСЕМ ИВЕНТАМ КОТОРЫЕ ПРОИСХОДЯТ
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins_collected = font_small.render(f"Coins: {COINS}", True, BLACK)  # Отображаем монеты
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_collected, (SCREEN_WIDTH - 100, 10))  # Отображаем монеты в верхнем правом углу

    # ДВИГАЕТ И ПЕРЕРИСОВЫВАЕТ ВСЕ СПРАЙТЫ
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # ПРОВЕРКА НА СТОЛКНОВЕНИЕ С МОНЕТОЙ
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1  
        C1.rect.top = 0  
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # ИСПОЛЬЗОВАТЬ КОГДА ПРОИСХОДИТ СТОЛКНОВЕНИЕ ИГРОКА И МАШИНЫ
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
