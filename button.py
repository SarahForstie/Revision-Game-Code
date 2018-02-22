import pygame as pg
import os

class Button(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.correct = 'n'
        self.image = pg.Surface((64,64))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

    def getPressed(self, mouse):
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

class aKey(Button, pg.sprite.Sprite):
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "aKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)-((screen.get_rect().centerx)/2))),((screen.get_rect().centery)-((screen.get_rect().centery)/4)))

class bKey(Button, pg.sprite.Sprite):
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "bKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)+((screen.get_rect().centerx)/2))),((screen.get_rect().centery)-((screen.get_rect().centery)/4)))

class cKey(Button, pg.sprite.Sprite):
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "cKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)-((screen.get_rect().centerx)/2))),((screen.get_rect().centery)+((screen.get_rect().centery)/4)))

class dKey(Button, pg.sprite.Sprite):
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "dKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)+((screen.get_rect().centerx)/2))),((screen.get_rect().centery)+((screen.get_rect().centery)/4)))

class yKey(Button, pg.sprite.Sprite):
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "yKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)-((screen.get_rect().centerx)/4))),((screen.get_rect().centery)+((screen.get_rect().centery)/4)))

class nKey(Button, pg.sprite.Sprite):
    def __init__(self, button_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(button_folder, "nKey.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((((screen.get_rect().centerx)+((screen.get_rect().centerx)/4))),((screen.get_rect().centery)+((screen.get_rect().centery)/4)))
