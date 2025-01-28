import pygame as pg
import random as rn
import settings as sg


class Sharik:
    def __init__(self):
        self.hitbox = pg.rect.Rect([400, 400], [150, 150])
        self.hitbox.center = [400, 400]

    def otrisovka(self, okno):
        pg.draw.ellipse(okno, [255, 0, 0], self.hitbox)

    def dvijenie(self):
        self.hitbox.center = pg.mouse.get_pos()


class Vragi:
    def __init__(self):
        self.x = rn.randint(0, 800)
        self.y = rn.randint(0, 800)
        self.hitbox = pg.rect.Rect([self.x, self.y], [50, 50])
        self.speed_x = rn.randint(-10, 10)
        self.speed_y = rn.randint(-10, 10)

    def otrisovka(self, okno):
        pg.draw.ellipse(okno, [0, 255, 0], self.hitbox)

    def dvijenie(self):
        self.x += self.speed_x
        self.y += self.speed_y
