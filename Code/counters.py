#Imports
import pygame as pg
import tiles as t
import os

#Parent counter class
class counter(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32,32))#Default 32*32 black square as default
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)#Default position on the screen
        self._xcoord = 0#The x coodinate on the mymap list
        self._ycoord = 0#The y coodinate on the mymap list
        self.playernum = 0#For displaying text on the screen
        self.points = 0#All players start with 0 points
        self.finished = 0#Whether the player is done or not
        self.getoutofjailfree = 0#The amount of get out of jail free items a player has
        self.skipquestion = 0#The amount of skip question items a player has
        self.doublepoints = 0#The amount of double point items a player has
        self.inJail = 'n'#Whether the player is in jail or not.

    def getFinished(self):#Returns whether the player is done or not
        return self.finished

    def setFinished(self):#Sets the player to finished
        self.finished = 1

    def getPlayerPoints(self):#Gets the amount of points a player has
        return self.points

    def setPlayerPoints(self, num):#Sets the amount of points the player has.
        self.points = self.points + num#If num is negative then the points are taken away
        
    def setMultiplier(self, num):#When players finish, they get a multiplier to points
        self.points = self.points * num
        
    def getPlayerNum(self):#Returns the player's number
        return self.playernum

    def getxCoord(self):#Returns the x coordinate on mymap
        return self._xcoord

    def getyCoord(self):#Returns the y coordinate on mymap
        return self._ycoord

    def setxCoord(self, num):#Sets the x coordinate on mymap
        self._xcoord = num

    def setyCoord(self, num):#Sets the y coordinate on mymap
        self._ycoord = num

    def moveRight(self, screen):#Moves the counter 64 pixels to the right on the screen
        self.updateCountx(screen, 64)
        
    def moveLeft(self, screen):#Moves the counter 64 pixels to the left on the screen
        self.updateCountx(screen, -64)

    def moveUp(self, screen):#Moves the counter 64 pixels upwards on the screen
        self.updateCounty(screen, -64)

    def moveDown(self, screen):#Moves the counter 64 pixels downwards on the screen
        self.updateCounty(screen, 64)

    def updateCountx(self, screen, movement):#Updates the counter x position
        self.rect.x = self.rect.x + movement

    def updateCounty(self, screen, movement):#Updates the counter y position
        self.rect.y = self.rect.y + movement

    def teleport(self, pos, newy, newx):#A method to be specialised by the child classes
        pass

    def setGetOutOfJail(self, number):#Sets the player's amount of get out of jail free items the player has
        self.getoutofjailfree = self.getoutofjailfree + number

    def getGetOutOfJail(self):#Returns the amount of get out of jail free items the player has
        return self.getoutofjailfree

    def setSkipQuestion(self, number):#Sets the player's amount of skip question items the player has
        self.skipquestion = self.skipquestion + number

    def getSkipQuestion(self):#Returns the amount of skip question items the player has
        return self.skipquestion

    def setDoublePoints(self, number):#Sets the player's amount of double point items the player has
        self.doublepoints = self.doublepoints + number

    def getDoublePoints(self):#Returns the amount of double point items the player has
        return self.doublepoints

    def setInJail(self, injail):#Sets whether a player is in jail or not
        self.inJail = injail

    def getInJail(self):#Returns whether a player is in jail or not
        return self.inJail

#Child Classes. Each have a given starting position
class cyan(counter, pg.sprite.Sprite):#Player 1's child class
    def __init__(self, counter_folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(counter_folder, "counter1.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)#Default position on the screen
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 1
        self.finished = 0
        self.points = 0
        self.inJail = 'n'
        self.getoutofjailfree = 0
        self.skipquestion = 0
        self.doublepoints = 0
        
    def setFinished(self):#Sets the player to finished
        self.finished = 1

    def teleport(self, pos, newy, newx):#Sets the player's position to a given place on the board
        self.rect.topleft = pos
        self.setxCoord(newx)
        self.setyCoord(newy)

class magenta(counter, pg.sprite.Sprite):#Player 2's child class
    def __init__(self, counter_folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(counter_folder, "counter2.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (32,0)#Default position on the screen
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 2
        self.finished = 0
        self.points = 0
        self.inJail = 'n'
        self.getoutofjailfree = 0
        self.skipquestion = 0
        self.doublepoints = 0

    def setFinished(self):#Sets the player to finished
        self.finished = 1

    def teleport(self, pos, newy, newx):#Sets the player's position to a given place on the board
        self.rect.topright = pos
        self.setxCoord(newx)
        self.setyCoord(newy)

class red(counter, pg.sprite.Sprite):#Player 3's child class
    def __init__(self, counter_folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(counter_folder, "counter3.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,32)#Default position on the screen
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 3
        self.finished = 0
        self.points = 0
        self.inJail = 'n'
        self.getoutofjailfree = 0
        self.skipquestion = 0
        self.doublepoints = 0

    def setFinished(self):#Sets the player to finished
        self.finished = 1

    def teleport(self, pos, newy, newx):#Sets the player's position to a given place on the board
        self.rect.bottomleft = pos
        self.setxCoord(newx)
        self.setyCoord(newy)

class blue(counter, pg.sprite.Sprite):#Player 4's child class
    def __init__(self, counter_folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(counter_folder, "counter4.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (32,32)#Default position on the screen
        self._xcoord = 0
        self._ycoord = 0
        self.playernum = 4
        self.finished = 0
        self.points = 0
        self.inJail = 'n'
        self.getoutofjailfree = 0
        self.skipquestion = 0
        self.doublepoints = 0

    def setFinished(self):#Sets the player to finished
        self.finished = 1

    def teleport(self, pos, newy, newx):#Sets the player's position to a given place on the board
        self.rect.bottomright = pos
        self.setxCoord(newx)
        self.setyCoord(newy)
