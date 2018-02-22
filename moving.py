import pygame as pg
import tiles as t
import random
import mapmaker as mmake
import counters
import os

def diceRoll():
    return (random.randint(1,6) + random.randint(1,6))

def movePlayer(player, screen, diceroll, mymap, play_sprites, tile_sprites, noGo, turntxt, turntxtrect, counterList):
    COLOUR = (170,170,170)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_SPACE):
                    running = False
    playermovecount = diceRoll()
    mytext = "Moves Left: "+str(playermovecount)
    printTxt(mytext, screen, turntxt, turntxtrect)
    printScores(counterList, screen)
    print("\nIt is player "+str(player.getPlayerNum())+"'s turn")
    print("You rolled a: "+str(playermovecount))
    currenty = player.getyCoord()
    currentx = player.getxCoord()
    while playermovecount > 0:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                move = 0
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_LEFT):
                    if (currenty == 0) or (currentx == 0):
                        pass
                    elif [(currentx - 1), currenty] in noGo:
                        pass
                    else:
                        player.moveLeft(screen)
                        currentx = currentx - 1
                        playermovecount = playermovecount - 1
                        mytext = "Moves Left:"+str(playermovecount)
                elif (event.key==pg.K_RIGHT):
                    if (currenty == 7) or (currentx == 7):
                        pass
                    elif [(currentx + 1), currenty] in noGo:
                        pass
                    else:
                        player.moveRight(screen)
                        currentx = currentx + 1
                        playermovecount = playermovecount - 1
                        mytext = "Moves Left:"+str(playermovecount)
                elif (event.key==pg.K_UP):
                    if (currentx == 7) or (currenty == 0):
                        pass
                    elif [currentx, (currenty - 1)] in noGo:
                        pass
                    else:
                        player.moveUp(screen)
                        currenty = currenty - 1
                        playermovecount = playermovecount - 1
                        mytext = "Moves Left:"+str(playermovecount)
                elif (event.key==pg.K_DOWN):
                    if (currentx == 0) or (currenty == 7):
                        pass
                    elif [currentx, (currenty + 1)] in noGo:
                        pass
                    else:
                        player.moveDown(screen)
                        currenty = currenty + 1
                        playermovecount = playermovecount - 1
                        mytext = "Moves Left:"+str(playermovecount)
            play_sprites.update()
            screen.fill(COLOUR)
            printTxt(mytext, screen, turntxt, turntxtrect)
            printScores(counterList, screen)
            tile_sprites.draw(screen)
            play_sprites.draw(screen)
            pg.display.flip()
        player.setxCoord(currentx)
        player.setyCoord(currenty)
    
def makeCounters(players, screen, play_sprites, game_folder):
    counter_folder = os.path.join(game_folder, "counters")
    counterList = []
    cyanCounter = counters.cyan(counter_folder)
    counterList.append(cyanCounter)
    magentaCounter = counters.magenta(counter_folder)
    counterList.append(magentaCounter)
    if players == 3:
        redCounter = counters.red(counter_folder)
        counterList.append(redCounter)
    elif players == 4:
        redCounter = counters.red(counter_folder)
        counterList.append(redCounter)
        blueCounter = counters.blue(counter_folder)
        counterList.append(blueCounter)
    else:
        pass
    for i in counterList:
        play_sprites.add(i)
    return counterList

def whichPlayer(counterList, players, screen, mymap, play_sprites, tile_sprites, turn, noGo):
    TEXT_COLOUR = (40,40,40)
    font = pg.font.Font(None, 32)
    mytext = "Current Player's Turn: "+ str(turn)
    turn_counter = font.render(mytext, True, TEXT_COLOUR, None)
    turn_counterrect = turn_counter.get_rect()
    turn_counterrect.topright = ((screen.get_rect().right),0)
    screen.blit(turn_counter, turn_counterrect)
    printScores(counterList, screen)
    printTxt("Moves Left: -", screen, turn_counter, turn_counterrect)
    pg.display.flip()
    if turn == 1:
        player = counterList[0]
        if int(player.getFinished()) == 0:
            m = movePlayer(player, screen, diceRoll(), mymap, play_sprites, tile_sprites, noGo, turn_counter, turn_counterrect, counterList)
            return turn, counterList[0]
        elif int(player.getFinished()) == 1:
            return turn, counterList[0]
    elif turn == 2:
        player = counterList[1]
        if int(player.getFinished()) == 0:
            m = movePlayer(player, screen, diceRoll(), mymap, play_sprites, tile_sprites, noGo, turn_counter, turn_counterrect, counterList)
            return turn, counterList[1]
        elif int(player.getFinished()) == 1:
            return turn, counterList[1]
    elif (len(counterList) >= 3) and (turn == 3):
        player = counterList[2]
        if int(player.getFinished()) == 0:
            m = movePlayer(player, screen, diceRoll(), mymap, play_sprites, tile_sprites, noGo, turn_counter, turn_counterrect, counterList)
            return turn, counterList[2]
        elif int(player.getFinished()) == 1:
            return turn, counterList[2]
    elif (len(counterList) >= 4) and (turn == 4):
        player = counterList[3]
        if int(player.getFinished()) == 0:
            m = movePlayer(player, screen, diceRoll(), mymap, play_sprites, tile_sprites, noGo, turn_counter, turn_counterrect, counterList)
            return 0, counterList[3]
        elif int(player.getFinished()) == 1:
            return 0, counterList[3]
    else:
        return 0, 0

def printScores(counterList, screen):
    COLOUR = (170,170,170)
    TEXT_COLOUR = (40,40,40)
    font = pg.font.Font(None, 32)
    startycoord = 35
    for i in counterList:
        mytext = "Player "+ str(i.getPlayerNum())+": " + str(i.getPlayerPoints())
        playerscore = font.render(mytext, True, TEXT_COLOUR, None)
        playerscorerect = playerscore.get_rect()
        playerscorerect.topright = ((screen.get_rect().right),(startycoord+20))
        startycoord = startycoord + 20
        screen.blit(playerscore, playerscorerect)
        pg.display.flip()
            
def printTxt(mytext, screen, turntxt, turntxtrect):
    COLOUR = (170,170,170)
    TEXT_COLOUR = (40,40,40)
    font = pg.font.Font(None, 32)
    dice_counter = font.render(mytext, True, TEXT_COLOUR, None)
    dice_counterrect = dice_counter.get_rect()
    dice_counterrect.topright = ((screen.get_rect().right),25)
    turntxtrect.topright = ((screen.get_rect().right),0)
    screen.blit(dice_counter, dice_counterrect)
    screen.blit(turntxt, turntxtrect)
    pg.display.flip()

'''

    dice_counter = font.render(mytext, True, TEXT_COLOUR, None)
    dice_counterrect = dice_counter.get_rect()
    dice_counterrect.topright = ((screen.get_rect().right),25)
    turntxtrect.topright = ((screen.get_rect().right),0)
    '''
