import pygame as pg
import tiles as t
import random
import mapmaker as mmake
import moving
import counters
import os
import readqs
import tileeffect as te
import button

def makeScreen():
    width  = 768
    height = 512
    pg.init()
    pg.display.set_caption('Revision Game')
    screen = pg.display.set_mode([width, height])
    pg.font.init()
    return screen

def main():
    COLOUR = (170,170,170)
    TEXT_COLOUR = (40,40,40)
    clock = pg.time.Clock()
    FPS = 30
    players = 2
    currentplayer = 0
    qpack = readqs.readfile()
    qp1 = readqs.makeQP1(qpack)
    qp2 = readqs.makeQP2(qpack)
    qp3 = readqs.makeQP3(qpack)
    game_folder = os.path.dirname(__file__)
    play_sprites = pg.sprite.Group()
    ABCDbutton_sprites = pg.sprite.Group()
    YNbutton_sprites = pg.sprite.Group()
    tile_sprites = pg.sprite.Group()
    screen = makeScreen()
    font = pg.font.Font(None, 32)
    mymap = mmake.mapInitiation(tile_sprites, game_folder)
    noGo, yesGo = mmake.noGo(mymap)
    counterList = moving.makeCounters(players, screen, play_sprites, game_folder)
    ABCDbuttonList, YNbuttonList = makeButtons(screen, game_folder, ABCDbutton_sprites, YNbutton_sprites)
    screen.fill(COLOUR)
    tile_sprites.draw(screen)
    play_sprites.draw(screen)
    pg.display.flip()
    turn = 1
    move = True
    while move:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                move = False
        clock.tick(FPS)
        turn, currentplayer = moving.whichPlayer(counterList, players, screen, mymap, play_sprites, tile_sprites, turn, noGo)
        if currentplayer == 0:
            currentplayer = counterList[0]
        else:
            te.getTileEffect(mymap, currentplayer, currentplayer.getxCoord(), currentplayer.getyCoord(), qp1, qp2, qp3, screen, ABCDbutton_sprites, YNbutton_sprites, ABCDbuttonList, YNbuttonList, yesGo)
        play_sprites.update()
        screen.fill(COLOUR)
        tile_sprites.draw(screen)
        play_sprites.draw(screen)
        pg.display.flip()
        
        turn = turn + 1

def makeButtons(screen, game_folder, ABCDbutton_sprites, YNbutton_sprites):
    button_folder = os.path.join(game_folder, "buttons")
    buttonA = button.aKey(button_folder, screen)
    ABCDbutton_sprites.add(buttonA)
    buttonB = button.bKey(button_folder, screen)
    ABCDbutton_sprites.add(buttonB)
    buttonC = button.cKey(button_folder, screen)
    ABCDbutton_sprites.add(buttonC)
    buttonD = button.dKey(button_folder, screen)
    ABCDbutton_sprites.add(buttonD)
    ABCDbuttonList = [buttonA, buttonB, buttonC, buttonD]

    buttonY = button.yKey(button_folder, screen)
    YNbutton_sprites.add(buttonY)
    buttonN = button.nKey(button_folder, screen)
    YNbutton_sprites.add(buttonN)
    YNbuttonList = [buttonY, buttonN]

    return ABCDbuttonList, YNbuttonList
    
main()
pg.quit()
