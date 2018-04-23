#Imports
import pygame as pg
import os

#Parent button class
class Button(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((64,64)) #A default 64*64 black box for the parent class sprite
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

    def getPressed(self, mouse): #Returns true when the mouse position is within the button's area
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

#Child Classes. Each have a given position
class aKey(Button, pg.sprite.Sprite):#Makes the A key button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "aKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)-((screen.get_rect().centerx)/2))),((screen.get_rect().centery)-((screen.get_rect().centery)/4)))

class bKey(Button, pg.sprite.Sprite):#Makes the B key button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "bKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)+((screen.get_rect().centerx)/2))),((screen.get_rect().centery)-((screen.get_rect().centery)/4)))

class cKey(Button, pg.sprite.Sprite):#Makes the C key button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "cKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)-((screen.get_rect().centerx)/2))),((screen.get_rect().centery)+((screen.get_rect().centery)/4)))

class dKey(Button, pg.sprite.Sprite):#Makes the D key button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "dKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)+((screen.get_rect().centerx)/2))),((screen.get_rect().centery)+((screen.get_rect().centery)/4)))

class yKey(Button, pg.sprite.Sprite):#Makes the Y key button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "yKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)-((screen.get_rect().centerx)/4))),((screen.get_rect().centery)+((screen.get_rect().centery)/4)))

class nKey(Button, pg.sprite.Sprite):#Makes the N key button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "nKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)+((screen.get_rect().centerx)/4))),((screen.get_rect().centery)+((screen.get_rect().centery)/4)))

class player2But(Button, pg.sprite.Sprite):#Makes the 2 player button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "2playerbut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_rect().centerx,((screen.get_rect().centery)-60))

class player3But(Button, pg.sprite.Sprite):#Makes the 3 player button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "3playerbut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (((screen.get_rect().centerx)-70),((screen.get_rect().centery)+60))

class player4But(Button, pg.sprite.Sprite):#Makes the 3 player button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "4playerbut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (((screen.get_rect().centerx)+70),((screen.get_rect().centery)+60))

class backBut(Button, pg.sprite.Sprite):#Makes the back button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "backbut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (screen.get_rect().left,screen.get_rect().top)

class nextBut(Button, pg.sprite.Sprite):#Makes the next button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "nextbut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = (screen.get_rect().right,screen.get_rect().top)

class diceBut(Button, pg.sprite.Sprite):#Makes the dice button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "dicebut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_rect().centerx,((screen.get_rect().centery)+((screen.get_rect().centery)/3)))

class instructBut(Button, pg.sprite.Sprite):#Makes the instructions button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "instructbut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_rect().centerx,((screen.get_rect().centery)-((screen.get_rect().centery)/6)))

class playBut(Button, pg.sprite.Sprite):#Makes the play button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "playbut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_rect().centerx,((screen.get_rect().centery)+((screen.get_rect().centery)/6)))

class pauseBut(Button, pg.sprite.Sprite):#Makes the pause button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "pausebut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottomright = screen.get_rect().bottomright

class resumeBut(Button, pg.sprite.Sprite):#Makes the resume button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "resumebut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_rect().centerx,((screen.get_rect().centery)+((screen.get_rect().centery)/6)))

class tomenuBut(Button, pg.sprite.Sprite):#Makes the exit to menu button and inherits from the Button parent class
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "tomenubut.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_rect().centerx,((screen.get_rect().centery)-((screen.get_rect().centery)/6)))
