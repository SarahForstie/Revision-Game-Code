#Imports
import random
import pygame as pg
import os

#Parent tile class
class tileBase(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.__up = None#The tile above
        self.__left = None#The tile to the left
        self.__down = None#The tile below
        self.__right = None#The tile to the right
        self._type = None#Tile type
        self.image = pg.Surface((64,64))#A default 64*64 black box for the parent class sprite
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

    def draw(self, surface):#Draws the tile to the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def setPosition(self, xcoord, ycoord):#Sets the placement of the tile
        self.rect.x = xcoord*64
        self.rect.y = ycoord*64

    def getTopLeft(self):#Returns the position of the top left
        return self.rect.topleft

    def getTopRight(self):#Returns the position of the top right
        return self.rect.topright

    def getBottomLeft(self):#Returns the position of the bottom left
        return self.rect.bottomleft

    def getBottomRight(self):#Returns the position of the bottom right
        return self.rect.bottomright

    def setNodes(self, mymap, x, y, len_of_mymap):#Sets the surroundings of the tiles
        if (y - 1) > 0:
            self.setUp(mymap[y-1][x])
        else:
            pass
        if (y + 1) < len_of_mymap:
            self.setDown(mymap[y+1][x])
        else:
            pass
        if (x - 1) > 0:
            self.setLeft(mymap[y][x-1])
        else:
            pass
        if (x + 1) < len_of_mymap:
            self.setRight(mymap[y][x+1])
        else:
            pass
        self.setPosition(x, y)

    def getUp(self):#Gets the tile above
        return self.__up

    def setUp(self, node):#Sets the tile above
        self.__up = node

    def getLeft(self):#Gets the tile to the left
        return self.__left

    def setLeft(self, node):#Sets the tile to the left
        self.__left = node

    def getDown(self):#Gets the tile below
        return self.__down

    def setDown(self, node):#Sets the tile below
        self.__down = node

    def getRight(self):#Gets the tile to the right
        return self.__right

    def setRight(self, node):#Sets the tile to the right
        self.__right = node

    def getType(self):#Gets the tile's type
        return self._type

#Child Classes. Each have a given position
class blankTile(tileBase, pg.sprite.Sprite):#Makes the blank tiles
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'b'
        self.image = pg.image.load(os.path.join(tile_folder, "blanktile.png")).convert_alpha()
        self.rect = self.image.get_rect()

class questionTile1(tileBase, pg.sprite.Sprite):#Makes the question 1 tiles
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'q1'
        self.__difficulty = 1
        self.image = pg.image.load(os.path.join(tile_folder, "qtile1.png")).convert()
        self.rect = self.image.get_rect()

    def getDifficulty(self):
        return self.__difficulty

class questionTile2(tileBase, pg.sprite.Sprite):#Makes the question 2 tiles
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'q2'
        self.__difficulty = 2
        self.image = pg.image.load(os.path.join(tile_folder, "qtile2.png")).convert()
        self.rect = self.image.get_rect()

    def getDifficulty(self):
        return self.__difficulty

class questionTile3(tileBase, pg.sprite.Sprite):#Makes the question 3 tiles
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'q3'
        self.__difficulty = 2
        self.image = pg.image.load(os.path.join(tile_folder, "qtile3.png")).convert()
        self.rect = self.image.get_rect()

    def getDifficulty(self):
        return self.__difficulty
        
class chanceTile(tileBase, pg.sprite.Sprite):#Makes the chance tiles
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'c'
        self.image = pg.image.load(os.path.join(tile_folder, "ctile.png")).convert()
        self.rect = self.image.get_rect()


class safeTile(tileBase, pg.sprite.Sprite):#Makes the safe tiles
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'sa'
        self.image = pg.image.load(os.path.join(tile_folder, "safetile.png")).convert()
        self.rect = self.image.get_rect()
        

class startTile(tileBase, pg.sprite.Sprite):#Makes the start tile
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'st'
        self.__ycoords = 0
        self.__xcoords = 0
        self.image = pg.image.load(os.path.join(tile_folder, "starttile.png")).convert()
        self.rect = self.image.get_rect()

class endTile(tileBase, pg.sprite.Sprite):#Makes the end tile
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'end'
        self.image = pg.image.load(os.path.join(tile_folder, "endtile.png")).convert()
        self.rect = self.image.get_rect()
      
class jailTile(tileBase, pg.sprite.Sprite):#Makes the jail tile
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'j'
        self.image = pg.image.load(os.path.join(tile_folder, "jailtile.png")).convert()
        self.rect = self.image.get_rect()

class gotojailTile(tileBase, pg.sprite.Sprite):#Makes the go to jail tile
    def __init__(self, tile_folder):
        pg.sprite.Sprite.__init__(self)
        self._type = 'gtj'
        self.image = pg.image.load(os.path.join(tile_folder, "gotojailtile.png")).convert()
        self.rect = self.image.get_rect()
