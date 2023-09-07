from pygame import *
init()

WIDTH =  1200
HEIGHT = 910

BLUE = (0, 0, 255)
GREEN = (0, 143, 95)
PURPLE = (67, 41, 171)
BROWN = (89, 28, 4)
BLUE = (0, 120, 215)
BG = image.load('BG.png')
BG = transform.scale(BG, (WIDTH, HEIGHT))
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Лабиринт')

clock = time.Clock()

class Sprite(sprite.Sprite):
    def __init__(self, pic, x, y, width, height):
        super().__init__()
        self.pic = image.load(pic)
        self.pic = transform.scale(self.pic, (width, height))
        self.rect = self.pic.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.pic, (self.rect.x, self.rect.y))

class Player(Sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= 3
        if keys[K_d]:
            self.rect.x += 3
        if keys[K_w]:
            self.rect.y -= 3
        if keys[K_s]:
            self.rect.y += 3
        

        if self.rect.x >= 1170:
            self.rect.x -= 3
        elif self.rect.x <= -15:
            self.rect.x += 3
        if self.rect.y <= -10:
            self.rect.y += 3
        elif self.rect.y >= 890:
            self.rect.y -= 3

class Enemy(Sprite):
    def update_x(self, x_start, x_end):
        self.rect.x += self.dx
        if self.rect.x <= x_start or self.rect.x >= x_end:
            self.dx = -self.dx
    def update_y(self, y_start, y_end):
        self.rect.y += self.dx
        if self.rect.y <= y_start or self.rect.y >= y_end:
            self.dx = -self.dx

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()       
        self.image = Surface((width, height))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



walls = sprite.Group()

door = Wall(950, 40, 20, 80) # 6
door.image.fill(BROWN)
# Внешние стены
walls.add(Wall(100, 20, 870, 20))  # 1
walls.add(Wall(100, 20, 20, 450))  # 2
walls.add(Wall(100, 590, 20, 280)) # 3
walls.add(Wall(100, 870, 870, 20)) # 4
walls.add(Wall(950, 120, 20, 770)) # 5

walls.add(Wall(200, 20, 20, 410))  # 7
walls.add(Wall(200, 500, 100, 20)) # 8
walls.add(Wall(200, 590, 20, 110)) # 9
walls.add(Wall(100, 780, 120, 20)) # 10
walls.add(Wall(300, 780, 100, 20)) # 11
walls.add(Wall(300, 680, 20, 100)) # 12
walls.add(Wall(200, 680, 100, 20)) # 13
walls.add(Wall(480, 780, 20, 100)) # 14
walls.add(Wall(580, 780, 20, 100)) # 15
walls.add(Wall(680, 500, 20, 300)) # 16
walls.add(Wall(770, 680, 20, 200)) # 17
walls.add(Wall(860, 680, 20, 100)) # 18
walls.add(Wall(770, 680, 100, 20)) # 19
walls.add(Wall(770, 590, 200, 20)) # 20
walls.add(Wall(580, 500, 300, 20)) # 21
walls.add(Wall(860, 300, 20, 200)) # 22
walls.add(Wall(770, 300, 100, 20)) # 23
walls.add(Wall(770, 120, 20, 200)) # 24
walls.add(Wall(770, 120, 200, 20)) # 25
walls.add(Wall(300, 120, 100, 20)) # 26
walls.add(Wall(380, 120, 20, 100)) # 27
walls.add(Wall(300, 220, 300, 20)) # 28
walls.add(Wall(300, 220, 20, 390)) # 29
walls.add(Wall(300, 590, 100, 20)) # 30
walls.add(Wall(380, 590, 20, 190)) # 31
walls.add(Wall(380, 680, 300, 20)) # 32
walls.add(Wall(480, 590, 120, 20)) # 33
walls.add(Wall(480, 400, 20, 200)) # 34
walls.add(Wall(380, 320, 20, 200)) # 35
walls.add(Wall(380, 300, 300, 20)) # 36
walls.add(Wall(480, 400, 200, 20)) # 37
walls.add(Wall(680, 20, 20, 400))  # 38
walls.add(Wall(480, 120, 200, 20)) # 39


trap_1 = Wall(200, 220, 100, 20)
trap_1.image.fill(BLUE)
trap_2 = Wall(860, 500, 100, 20)
trap_2.image.fill(BLUE)


Inky = Player('hero.png', 10, 100, 30, 30)

Key_1 = Enemy('key.png', 137, 70, 40, 40)
Key_1.dx = 1
Key_2 = Enemy('key.png', 803, 710, 40, 40)
Key_2.dx = 1
Key_3 = Enemy('key.png', 810, 230, 40, 40)
Key_3.dx = 1


Enemies = sprite.Group()
Cyborg1 = Enemy('cyborg.png', 135, 120, 50, 50)
Cyborg1.dx = 5

Cyborg2 = Enemy('cyborg.png', 450, 720, 50, 50)
Cyborg2.dx = 4

spike_up = Enemy('spike_up.png', 210, 410, 100, 100)
spike_up.dx = 5
spike_down = Enemy('spike_down.png', 865, 120, 100, 100)
spike_down.dx = 5

treasure = Enemy('treasure.png', 1000, 700, 200, 200)

Enemies.add(Cyborg1)
Enemies.add(Cyborg2)


def restart():
    global paused, door_open, fin, key1, key2, key3, trap1, trap2
    key1 = 0
    key2 = 0
    key3 = 0
    trap1 = 0
    trap2 = 0
    spike_down.rect.x = 865
    spike_down.rect.y = 120
    spike_up.rect.x = 210
    spike_up.rect.y = 410
    Inky.rect.x = 10
    Inky.rect.y = 100
    paused = False
    fin = False
    door_open = False


mixer.music.load('Beats of Water Drops.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()


kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

my_font = font.SysFont('verdana', 70)

text_pause = my_font.render('PAUSE', True, PURPLE)
text_win = my_font.render('YOU WIN!', True, PURPLE)
text_lose = my_font.render('GAME OVER', True, PURPLE)

my_font = font.SysFont('verdana', 40)

text_restart = my_font.render('Press R to restart', True, PURPLE)
text_continue = my_font.render('Press R to continue', True, PURPLE)

text_fin = None

run = True
paused = False
door_open = False
fin = False
cheats = False
key1 = 0
key2 = 0
key3 = 0
trap1 = 0
trap2 = 0
timer_update = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_r and fin:
                restart()

            elif e.key == K_r and not fin:
                paused = not paused

            if e.key == K_p:
                if not cheats:
                    cheats = True
                else:
                    cheats = False


    if not fin and not paused:
        window.blit(BG, (0, 0))
        
        # ключи
        if key3 != 1:
            Key_3.update_y(215, 240)
            Key_3.draw()
        if key2 != 1:
            Key_2.update_y(705, 725)
            Key_2.draw()
        if key1 != 1:
            Key_1.update_y(60, 75)
            Key_1.draw()

        # дверь
        if key1 == 1 and key2 == 1 and key3 == 1:
            door_open = True
        if not door_open:
            door.update()
            door.draw()

        treasure.update()
        treasure.draw()

        # ловушки
        trap_2.update()
        trap_2.draw()
        trap_1.update()
        trap_1.draw()

        if trap2 == 1:
            if sprite.collide_rect(Inky, spike_down):
                paused = True
                fin = True
                text_fin = text_lose
            spike_down.update()
            spike_down.rect.y += spike_down.dx
        if spike_down.rect.y <= 590 and trap2 == 1:
            spike_down.draw()


        if trap1 == 1:
            if sprite.collide_rect(Inky, spike_up):
                paused = True
                fin = True
                text_fin = text_lose
            spike_up.update()
            spike_up.rect.y -= spike_up.dx
        if spike_up.rect.y >= 40 and trap1 == 1:
            spike_up.draw()

        # игрок
        Inky.update()
        Inky.draw()

        # враги
        Cyborg1.update_y(100, 730)
        Cyborg2.update_x(400, 640)
        Cyborg1.draw()
        Cyborg2.draw()

        # Стены   
        walls.draw(window)
        if not cheats:
            if sprite.spritecollideany(Inky, walls) or sprite.spritecollideany(Inky, Enemies) or sprite.collide_rect(Inky, door):
                paused = True
                fin = True
                text_fin = text_lose
                kick.play()
        if sprite.collide_rect(Inky, Key_1):
            key1 = 1
        if sprite.collide_rect(Inky, Key_2):
            key2 = 1
        if sprite.collide_rect(Inky, Key_3):
            key3 = 1
        if sprite.collide_rect(Inky, trap_1):
            trap1 = 1
        if sprite.collide_rect(Inky, trap_2):
            trap2 = 1
        if sprite.collide_rect(Inky, treasure):
            paused = True
            fin = True
            text_fin = text_win
            money.play()

    elif paused and fin:
        window.blit(BG, (0, 0))
        window.blit(text_fin, (400, 300))
        window.blit(text_restart, (430, 400))

    elif paused and not fin:
        window.blit(BG, (0, 0))
        window.blit(text_pause, (500, 300))
        window.blit(text_continue, (430, 400))
    display.update()
    clock.tick(60)