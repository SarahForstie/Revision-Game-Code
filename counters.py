import pygame as pg
import tiles as t
import os


class counter(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32,32))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 0
        self.points = 0
        self.finished = 0

    def getFinished(self):
        return self.finished

    def setFinished(self):
        self.finished = 1

    def getPlayerPoints(self):
        return self.points

    def setPlayerPoints(self, num):
        self.points = self.points + num

    def getPlayerNum(self):
        return self.playernum

    def getxCoord(self):
        return self._xcoord

    def getyCoord(self):
        return self._ycoord

    def setxCoord(self, num):
        self._xcoord = num

    def setyCoord(self, num):
        self._ycoord = num

    def moveRight(self, screen):
        self.updateCountx(screen, 64)
        
    def moveLeft(self, screen):
        self.updateCountx(screen, -64)

    def moveUp(self, screen):
        self.updateCounty(screen, -64)

    def moveDown(self, screen):
        self.updateCounty(screen, 64)

    def updateCountx(self, screen, movement):
        self.rect.x = self.rect.x + movement

    def updateCounty(self, screen, movement):
        self.rect.y = self.rect.y + movement

    def teleport(self, pos):
        pass

class cyan(counter, pg.sprite.Sprite):
    def __init__(self, counter_folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(counter_folder, "counter1.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 1
        self.finished = 0
        self.points = 0
        
    def setFinished(self):
        self.finished = 1

    def teleport(self, pos):
        self.rect.topleft = pos

class magenta(counter, pg.sprite.Sprite):
    def __init__(self, counter_folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(counter_folder, "counter2.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (32,0)
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 2
        self.finished = 0
        self.points = 0

    def setFinished(self):
        self.finished = 1

    def teleport(self, pos):
        self.rect.topright = pos

class red(counter, pg.sprite.Sprite):
    def __init__(self, counter_folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(counter_folder, "counter3.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,32)
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 3
        self.finished = 0
        self.points = 0

    def setFinished(self):
        self.finished = 1

    def teleport(self, pos):
        self.rect.bottomleft = pos

class blue(counter, pg.sprite.Sprite):
    def __init__(self, counter_folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(counter_folder, "counter4.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (32,32)
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 4
        self.finished = 0
        self.points = 0

    def setFinished(self):
        self.finished = 1

    def teleport(self, pos):
        self.rect.bottomright = pos
