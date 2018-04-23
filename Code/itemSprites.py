#Imports
import pygame as pg
import os

#Parent sprite class
class SpriteDisplay(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20,20))#Default 20*20 black square as default
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        #No methods are needed for the items, they are just needed for displays

#Child Classes. Each have a given position
class getOutOfJailItem1(SpriteDisplay, pg.sprite.Sprite):#Player 1's get out of jail item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "getoutofjail.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 45), 160)

class getOutOfJailItem2(SpriteDisplay, pg.sprite.Sprite):#Player 2's get out of jail item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "getoutofjail.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 45), 190)

class getOutOfJailItem3(SpriteDisplay, pg.sprite.Sprite):#Player 3's get out of jail item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "getoutofjail.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 45), 220)

class getOutOfJailItem4(SpriteDisplay, pg.sprite.Sprite):#Player 4's get out of jail item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "getoutofjail.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 45), 250)

class doublePointsItem1(SpriteDisplay, pg.sprite.Sprite):#Player 1's double point item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "doublepoints.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 75), 160)

class doublePointsItem2(SpriteDisplay, pg.sprite.Sprite):#Player 2's double point item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "doublepoints.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 75), 190)

class doublePointsItem3(SpriteDisplay, pg.sprite.Sprite):#Player 3's double point item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "doublepoints.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 75), 220)

class doublePointsItem4(SpriteDisplay, pg.sprite.Sprite):#Player 4's double point item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "doublepoints.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 75), 250)

class skipQuestionItem1(SpriteDisplay, pg.sprite.Sprite):#Player 1's skip question item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "skipquestion.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 105), 160)

class skipQuestionItem2(SpriteDisplay, pg.sprite.Sprite):#Player 2's skip question item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "skipquestion.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 105), 190)

class skipQuestionItem3(SpriteDisplay, pg.sprite.Sprite):#Player 3's skip question item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "skipquestion.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 105), 220)

class skipQuestionItem4(SpriteDisplay, pg.sprite.Sprite):#Player 4's skip question item class
    def __init__(self, item_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(item_folder, "skipquestion.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (((screen.get_rect().right)- 105), 250)
