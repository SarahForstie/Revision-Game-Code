#Imports
import pygame as pg
import random
import mapmaker
import moving
import os
import tileeffect
import makeButtons
import readqs
import time

def play(screen, players, game_folder):#Plays the game
    #Defines the text look
    COLOUR = (20,2,92)
    TEXT_COLOUR = (40,40,40)
    clock = pg.time.Clock()
    FPS = 30#Sets the frames per second
    currentplayer = 0
    qp1, qp2, qp3 = readqs.makeQpacks()#Gets the questions
    play_sprites, ABCDbutton_sprites, YNbutton_sprites, tile_sprites, dice_sprite, pause_sprite, pauseMenu_sprites = makeButtons.makeSpriteGroups()#Makes the sprite groups
    mymap, noGo, yesGo, jailtile = mapmaker.mapInitiation(tile_sprites, game_folder)#Makes the game board
    counterList = moving.makeCounters(players, screen, play_sprites, game_folder)#Makes the player counters
    ABCDbuttonList, YNbuttonList, diceButton, pauseButton, pauseMenuList = makeButtons.makeButtonsToPlay(screen, ABCDbutton_sprites, YNbutton_sprites, dice_sprite, pause_sprite, pauseMenu_sprites)#Makes buttons
    screen.fill(COLOUR)
    tile_sprites.draw(screen)
    play_sprites.draw(screen)
    pg.display.flip()#Displays screen
    multipliers = []#Holds the player multipliers
    end_time = time.time() + 60 * 15#Sets the timer end
    turn = 1
    move = True
    while move:#A loop which ends when the game is quit to menu, all players finish or the time stops
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                move = False
        turn, currentplayer, backToMenu = moving.whichPlayer(counterList, players, screen, mymap, play_sprites, tile_sprites, turn, noGo, diceButton, dice_sprite, pauseButton, pause_sprite)#Moves the player
        if backToMenu == True:#Quits back to the menu
            move = False
            return counterList, multipliers
        if currentplayer == 0:
            currentplayer = counterList[0]
        else:#Applies an effect to the player based on the tile they landed on
            tileeffect.getTileEffect(mymap, currentplayer, currentplayer.getxCoord(), currentplayer.getyCoord(), qp1, qp2, qp3, screen, ABCDbutton_sprites, YNbutton_sprites, ABCDbuttonList, YNbuttonList, yesGo, jailtile, counterList)
        play_sprites.update()
        screen.fill(COLOUR)
        tile_sprites.draw(screen)
        play_sprites.draw(screen)
        pause_sprite.draw(screen)
        pg.display.flip()#Displays screen
        
        turn = turn + 1

        if time.time() >= end_time:#Allows the current player to finish their turn then quits when the time limit is reached
            tileeffect.timeUp(screen)
            return counterList, multipliers
        else:
            pass
        
        playersDone = 0
        for i in counterList:#Sets multipliers and finds whether all players have finished
            if i not in multipliers:
                multipliers.append(i)
            finished = int(i.getFinished())
            playersDone = playersDone + finished

        if playersDone == players:#Exit to menu if all players are finished
            move = False
            return counterList, multipliers
