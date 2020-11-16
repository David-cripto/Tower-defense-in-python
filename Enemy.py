import math
import pygame

pygame.init()


class Enem:
    def __init__(self, x, y, vel):
        self.live = True
        self.health = 5000
        self.max_health = 5000
        self.vel = vel
        self.path = [(76, 80), (138, 56), (193, 80), (683, 79), (756, 152), (716, 241), (505, 265), (452, 309),
                     (450, 555), (450, 600)]
        self.x = x
        self.y = y
        self.path_pos = 0
        self.i = 0
        self.img_left = []
        self.img_right = []
        for i in range(1, 12):
            self.img_left.append(pygame.image.load("run_left (" + str(i) + ").png"))
            self.img_right.append(pygame.image.load("run_right (" + str(i) + ").png"))
        for i in range(len(self.img_right)):
            self.img_right[i] = pygame.transform.scale(self.img_right[i], (94, 80))
        for i in range(len(self.img_left)):
            self.img_left[i] = pygame.transform.scale(self.img_left[i], (94, 80))
        self.width = self.img_right[0].get_width()
        self.height = self.img_right[0].get_height()

    def move(self):
        if (self.path[self.path_pos][0] - self.x) <= 5 and (self.path[self.path_pos][1] - self.y) <= 5:
            self.path_pos += 1
        x1, y1 = self.x, self.y
        x2, y2 = self.path[self.path_pos]
        hypothenuse = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.x += (x2 - x1) / hypothenuse * self.vel
        self.y += (y2 - y1) / hypothenuse * self.vel

    def draw(self, win):
        if self.path[self.path_pos][0] - self.x < 0:
            win.blit(self.img_left[self.i], (self.x - self.width // 2, self.y - self.height // 2))
        else:
            win.blit(self.img_right[self.i], (self.x - self.width // 2, self.y - self.height // 2))
        self.i += 1
        if self.i >= len(self.img_right):
            self.i = 0
        self.health_bar(win)

    def set_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.live = False
        else:
            self.live = True

    def health_bar(self, win):
        length = 75
        move_by = length / self.max_health
        health_bar = move_by * self.health
        red =(255, 0, 0)
        green = (0, 255, 0)
        rect_size_red = (self.x - self.width // 2, self.y - self.height // 2, length, 10)
        rect_size_green = (self.x - self.width // 2, self.y - self.height // 2, health_bar, 10)
        pygame.draw.rect(win, red, rect_size_red, 0)
        pygame.draw.rect(win, green, rect_size_green, 0)

class Troll(Enem):
    def __init__(self, x, y, vel):
        self.live = True
        self.health = 14000
        self.max_health = 14000
        self.vel = vel
        self.path = [(76, 80), (138, 56), (193, 80), (683, 79), (756, 152), (716, 241), (505, 265), (452, 309),
                     (450, 555), (450, 600)]
        self.x = x
        self.y = y
        self.path_pos = 0
        self.i = 0
        self.img_left = []
        self.img_right = []
        for i in range(1, 21):
            self.img_left.append(pygame.image.load("run_troll_left (" + str(i) + ").png"))
            self.img_right.append(pygame.image.load("run_troll_right (" + str(i) + ").png"))
        for i in range(len(self.img_right)):
            self.img_right[i] = pygame.transform.scale(self.img_right[i], (94, 80))
        for i in range(len(self.img_left)):
            self.img_left[i] = pygame.transform.scale(self.img_left[i], (94, 80))
        self.width = self.img_right[0].get_width()
        self.height = self.img_right[0].get_height()