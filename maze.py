from pygame import *
'''Необходимые классы'''

#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Персонажи игры:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
wall1 = Wall(0, 255, 0, 200, 125, 200, 10)
wall2 = Wall(0, 255, 0, 290, 125, 10, 200)
wall3 = Wall(0, 255, 0, 390, 0, 10, 125)
wall4 = Wall(0, 255, 0, 290, 425, 10, 125)
wall5 = Wall(0, 255, 0, 390, 225, 10, 400)
wall6 = Wall(0, 255, 0, 390, 315, 80, 10)


game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)
lose = font.render('YOU LOSE', True, (250, 0, 0))
win = font.render('YOU WIN', True, (0, 250, 0))

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(player, monster):
        window.blit(lose, (200, 200))
    if sprite.collide_rect(player, wall1):
        window.blit(lose, (200, 200))
    if sprite.collide_rect(player, wall2):
        window.blit(lose, (200, 200))
    if sprite.collide_rect(player, wall3):
        window.blit(lose, (200, 200))
    if sprite.collide_rect(player, wall4):
        window.blit(lose, (200, 200))
    if sprite.collide_rect(player, wall5):
        window.blit(lose, (200, 200))
    if sprite.collide_rect(player, wall6):
        window.blit(lose, (200, 200))
    if sprite.collide_rect(player, final):
        window.blit(win, (200, 200))

    if finish != True:

        window.blit(background,(0, 0))
        player.update()
        monster.update()
        wall1.update()
        wall2.update()
        wall3.update()
        wall4.update()
        wall5.update()
        wall6.update()

        player.reset()
        monster.reset()
        final.reset() 
        wall1.reset()
        wall2.reset()
        wall3.reset()
        wall4.reset()
        wall5.reset()
        wall6.reset()

    display.update()
    clock.tick(FPS)