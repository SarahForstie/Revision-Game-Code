import random
import pygame as pg
import os

class tileBase(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.__up = None
        self.__left = None
        self.__down = None
        self.__right = None
        self._type = None
        self.image = pg.Surface((64,64))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def setPosition(self, x, y):
        self.rect.x = x*64
        self.rect.y = y*64

    def getTopLeft(self):
        return self.rect.topleft

    def getTopRight(self):
        return self.rect.topright

    def getBottomLeft(self):
        return self.rect.bottomleft

    def getBottomRight(self):
        return self.rect.bottomright

    def setNodes(self, mymap, x, y):
        if (y - 1) > 0:
            self.setUp(mymap[y-1][x])
        else:
            pass
        if (y + 1) < 8:
            self.setDown(mymap[y+1][x])
        else:
            pass
        if (x - 1) > 0:
            self.setLeft(mymap[y][x-1])
        else:
            pass
        if (x + 1) < 8:
            self.setRight(mymap[y][x+1])
        else:
            pass
        self.setPosition(x, y)

    def getUp(self):
        return self.__up

    def setUp(self, node):
        self.__up = node

    def getLeft(self):
        return self.__left

    def setLeft(self, node):
        self.__left = node

    def getDown(self):
        return self.__down

    def setDown(self, node):
        self.__down = node

    def getRight(self):
        return self.__right

    def setRight(self, node):
        self.__right = node

    def getType(self):
        return self._type

class blankTile(tileBase, pg.sprite.Sprite):
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'b'
        self.image = pg.image.load(os.path.join(tile_folder, "blanktile.png")).convert()
        self.rect = self.image.get_rect()

class questionTile1(tileBase, pg.sprite.Sprite):
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'q1'
        self.__qpack = []
        self.__difficulty = 1
        self.image = pg.image.load(os.path.join(tile_folder, "qtile1.png")).convert()
        self.rect = self.image.get_rect()

    def getDifficulty(self):
        return self.__difficulty

class questionTile2(tileBase, pg.sprite.Sprite):
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'q2'
        self.__qpack = []
        self.__difficulty = 2
        self.image = pg.image.load(os.path.join(tile_folder, "qtile2.png")).convert()
        self.rect = self.image.get_rect()

    def getDifficulty(self):
        return self.__difficulty

class questionTile3(tileBase, pg.sprite.Sprite):
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'q3'
        self.__qpack = []
        self.__difficulty = 2
        self.image = pg.image.load(os.path.join(tile_folder, "qtile3.png")).convert()
        self.rect = self.image.get_rect()

    def getDifficulty(self):
        return self.__difficulty
        
class chanceTile(tileBase, pg.sprite.Sprite):
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'c'
        self.image = pg.image.load(os.path.join(tile_folder, "ctile.png")).convert()
        self.rect = self.image.get_rect()


class safeTile(tileBase, pg.sprite.Sprite):
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'sa'
        self.image = pg.image.load(os.path.join(tile_folder, "safetile.png")).convert()
        self.rect = self.image.get_rect()
        

class startTile(tileBase, pg.sprite.Sprite):
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'st'
        self.__ycoords = 0
        self.__xcoords = 0
        self.image = pg.image.load(os.path.join(tile_folder, "starttile.png")).convert()
        self.rect = self.image.get_rect()

class endTile(tileBase, pg.sprite.Sprite):
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'end'
        self.image = pg.image.load(os.path.join(tile_folder, "endtile.png")).convert()
        self.rect = self.image.get_rect()
      
