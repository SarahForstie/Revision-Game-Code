#Imports
import pygame as pg
import random
import counters
import os
import time
import menus
import playSounds
import makeButtons

#Global variables
global len_of_mymap_minus

len_of_mymap = 10
len_of_mymap_minus = len_of_mymap - 1

global COLOUR
global TEXT_COLOUR
global TEXT

TEXT_COLOUR = (255,255,255)
COLOUR = (20,2,92)
TEXT = 'saxmono.ttf'

def diceRoll(screen, diceButton, dice_sprite, player, inJail):#Displays the dice roll screen and returns the dice roll
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    printTurn(player, screen)
    if inJail == 'y':
        printInJail(screen)
    screen.fill(COLOUR)
    mytext = "Click to Roll the Dice"
    diceTxt = font.render(mytext, True, TEXT_COLOUR, None)
    diceTxtrect = diceTxt.get_rect()
    diceTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-80))
    screen.blit(diceTxt, diceTxtrect)
    mytext = "Or Press Spacebar"
    diceTxt = font2.render(mytext, True, TEXT_COLOUR, None)
    diceTxtrect = diceTxt.get_rect()
    diceTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-30))
    screen.blit(diceTxt, diceTxtrect)
    dice_sprite.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when spacebar is pressed or the dice button
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_SPACE):
                    playSounds.diceSound()
                    done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if diceButton.getPressed(mousepos) == True and pressed1:
                playSounds.diceSound()
                done = True
    diceroll = (random.randint(1,6) + random.randint(1,6))#Randomly chooses 2 numbers to be the dice
    printDiceRoll(diceroll, screen)#Displays what the player rolled
    return diceroll

def inJailDiceRoll(player, screen, diceButton, dice_sprite):#A function for when a player is in jail for if they stay in or get out
    playermovecount = diceRoll(screen, diceButton, dice_sprite, player, 'y')
    if (playermovecount == 2) or (playermovecount == 12):#If the player rolls 2 or 12 then they are free from jail
        player.setInJail('n')
        out = 'y'
    else:#Any other roll and they stay in jail
        inJail = player.getInJail()
        player.setInJail(inJail - 1)
        out = 'n'

    printGetOutOfJail(screen, player, out)#Displays whether the player got out of jail
    
    return playermovecount

def movePlayer(player, screen, mymap, play_sprites, tile_sprites, noGo, turntxt, turntxtrect, counterList, diceButton, dice_sprite, pauseButton, pause_sprite):#Movement of the player
    global COLOUR
    
    if player.getInJail() == 0:#When the player has spent 3 turns in jail they are set out of jail
        player.setInJail('n')

    if player.getInJail() != 'n':#If the player is in jail then allow chance to get out
        playermovecount = inJailDiceRoll(player, screen, diceButton, dice_sprite)
    else:
        playermovecount = diceRoll(screen, diceButton, dice_sprite, player, 'n')#Else just show the diceroll screen

    mytext = "Moves Left: "+str(playermovecount)
    printTxt(mytext, screen, turntxt, turntxtrect)
    printScores(counterList, screen)
    currenty = player.getyCoord()
    currentx = player.getxCoord()
    drawAll(screen, play_sprites, tile_sprites, pause_sprite, mytext, turntxt, turntxtrect, counterList)#Draws everythin to screen
    if player.getInJail() == 'n':#Only move if the player is not in jail
        while playermovecount > 0:#While the moves left is larger than 0 allow movement
            change = False
            for event in pg.event.get():
                if event.type == pg.QUIT:#Exits the game
                    pg.quit()
                    move = 0
                if (event.type == pg.KEYDOWN):
                    if (event.key==pg.K_LEFT) or (event.key==pg.K_a):#If can go left then go left at key down
                        if (currenty == 0) or (currentx == 0):
                            pass
                        elif [(currentx - 1), currenty] in noGo:
                            pass
                        else:
                            player.moveLeft(screen)
                            currentx = currentx - 1
                            playermovecount = playermovecount - 1
                            mytext = "Moves Left:"+str(playermovecount)
                            playSounds.counterMoveSound()
                            change = True#So screen is only drawn if a change occurs
                    elif (event.key==pg.K_RIGHT) or (event.key==pg.K_d):#If can go right then go right at key down
                        if (currenty == len_of_mymap_minus) or (currentx == len_of_mymap_minus):
                            pass
                        elif [(currentx + 1), currenty] in noGo:
                            pass
                        else:
                            player.moveRight(screen)
                            currentx = currentx + 1
                            playermovecount = playermovecount - 1
                            mytext = "Moves Left:"+str(playermovecount)
                            playSounds.counterMoveSound()
                            change = True#So screen is only drawn if a change occurs
                    elif (event.key==pg.K_UP) or (event.key==pg.K_w):#If can go up then go up at key down
                        if (currentx == len_of_mymap_minus) or (currenty == 0):
                            pass
                        elif [currentx, (currenty - 1)] in noGo:
                            pass
                        else:
                            player.moveUp(screen)
                            currenty = currenty - 1
                            playermovecount = playermovecount - 1
                            mytext = "Moves Left:"+str(playermovecount)
                            playSounds.counterMoveSound()
                            change = True#So screen is only drawn if a change occurs
                    elif (event.key==pg.K_DOWN) or (event.key==pg.K_s):#If can go down then go down at key down
                        if (currentx == 0) or (currenty == len_of_mymap_minus):
                            pass
                        elif [currentx, (currenty + 1)] in noGo:
                            pass
                        else:
                            player.moveDown(screen)
                            currenty = currenty + 1
                            playermovecount = playermovecount - 1
                            mytext = "Moves Left:"+str(playermovecount)
                            playSounds.counterMoveSound()
                            change = True#So screen is only drawn if a change occurs
                mousepos = pg.mouse.get_pos()
                pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
                if pauseButton.getPressed(mousepos) == True and pressed1:#Goes to pause menu when pause button is pressed
                    playSounds.buttonClickSound()
                    backToMenu = menus.pauseMenu(screen)
                    if backToMenu == True:#If the player chooses to return to the menu then the game is exited
                        move = 0
                        return True
                    else:
                        drawAll(screen, play_sprites, tile_sprites, pause_sprite, mytext, turntxt, turntxtrect, counterList)#Everything is redrawn
                if change == True:#Only redrawns everything if a change occurs
                    drawAll(screen, play_sprites, tile_sprites, pause_sprite, mytext, turntxt, turntxtrect, counterList)
            player.setxCoord(currentx)#Changes the player's x coordinate on the tile list
            player.setyCoord(currenty)#Changes the player's y coordinate on the tile list
    else:
        pass
    return False

def makeCounters(players, screen, play_sprites, game_folder):#Makes the players
    counter_folder = os.path.join(game_folder, "counters")
    counterList = []#Allows each counter object to be accessed
    cyanCounter = counters.cyan(counter_folder)#Make player 1
    counterList.append(cyanCounter)
    magentaCounter = counters.magenta(counter_folder)#Make player 2
    counterList.append(magentaCounter)
    if players == 3:
        redCounter = counters.red(counter_folder)#Make player 3
        counterList.append(redCounter)
    elif players == 4:
        redCounter = counters.red(counter_folder)#Make player 3
        counterList.append(redCounter)
        blueCounter = counters.blue(counter_folder)#Make player 4
        counterList.append(blueCounter)
    else:
        pass
    for i in counterList:#Adds the counters to the player sprite group
        play_sprites.add(i)
    return counterList

def whichPlayer(counterList, players, screen, mymap, play_sprites, tile_sprites, turn, noGo, diceButton, dice_sprite, pauseButton, pause_sprite):#Decides which player is to move next
    #Defines the text look
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 20)

    #Displays the text
    mytext = "Current Player's Turn: "+ str(turn)
    turn_counter = font.render(mytext, True, TEXT_COLOUR, None)
    turn_counterrect = turn_counter.get_rect()
    turn_counterrect.topright = ((screen.get_rect().right),0)
    screen.blit(turn_counter, turn_counterrect)
    printScores(counterList, screen)
    printTxt("Moves Left: -", screen, turn_counter, turn_counterrect)
    pg.display.flip()#Displays screen
    time.sleep(1.5)
    if turn == 1:#If it's player 1's turn and they haven't finished then they move
        player = counterList[0]
        if int(player.getFinished()) == 0:
            backToMenu = movePlayer(player, screen, mymap, play_sprites, tile_sprites, noGo, turn_counter, turn_counterrect, counterList, diceButton, dice_sprite, pauseButton, pause_sprite)
            return turn, counterList[0], backToMenu
        elif int(player.getFinished()) == 1:#Skips the player's turn
            return turn, counterList[0], 0
        
    elif turn == 2:#If it's player 2's turn and they haven't finished then they move
        player = counterList[1]
        if int(player.getFinished()) == 0:
            backToMenu = movePlayer(player, screen, mymap, play_sprites, tile_sprites, noGo, turn_counter, turn_counterrect, counterList, diceButton, dice_sprite, pauseButton, pause_sprite)
            return turn, counterList[1], backToMenu
        elif int(player.getFinished()) == 1:#Skips the player's turn
            return turn, counterList[1], 0
        
    elif (len(counterList) >= 3) and (turn == 3):
        player = counterList[2]#If it's player 3's turn and they haven't finished then they move
        if int(player.getFinished()) == 0:
            backToMenu = movePlayer(player, screen, mymap, play_sprites, tile_sprites, noGo, turn_counter, turn_counterrect, counterList, diceButton, dice_sprite, pauseButton, pause_sprite)
            return turn, counterList[2], backToMenu
        elif int(player.getFinished()) == 1:#Skips the player's turn
            return turn, counterList[2], 0
        
    elif (len(counterList) >= 4) and (turn == 4):
        player = counterList[3]#If it's player 4's turn and they haven't finished then they move
        if int(player.getFinished()) == 0:
            backToMenu = movePlayer(player, screen, mymap, play_sprites, tile_sprites, noGo, turn_counter, turn_counterrect, counterList, diceButton, dice_sprite, pauseButton, pause_sprite)
            return 0, counterList[3], backToMenu
        elif int(player.getFinished()) == 1:#Skips the player's turn
            return 0, counterList[3], 0
    else:
        return 0, 0, 0#Resets the turns

def printScores(counterList, screen):#Displays each player's current score
    #Defines the text look
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 20)

    #Displays the text
    startycoord = 35
    for i in counterList:
        mytext = "Player " + str(i.getPlayerNum())+": " + str(i.getPlayerPoints())
        playerscore = font.render(mytext, True, TEXT_COLOUR, None)
        playerscorerect = playerscore.get_rect()
        playerscorerect.topright = ((screen.get_rect().right),(startycoord+20))
        startycoord = startycoord + 20
        screen.blit(playerscore, playerscorerect)
        pg.display.flip()#Displays screen

    startycoord = 130
    for i in counterList:
        mytext = ": " + "P" + str(i.getPlayerNum())
        playerscore = font.render(mytext, True, TEXT_COLOUR, None)
        playerscorerect = playerscore.get_rect()
        playerscorerect.topright = ((screen.get_rect().right),(startycoord+30))
        startycoord = startycoord + 30
        screen.blit(playerscore, playerscorerect)
        pg.display.flip()#Displays screen
            
def printTxt(mytext, screen, turntxt, turntxtrect):#Displays the current player's turn and the amount of moves they have left
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 20)

    #Displays the text
    dice_counter = font.render(mytext, True, TEXT_COLOUR, None)
    dice_counterrect = dice_counter.get_rect()
    dice_counterrect.topright = ((screen.get_rect().right),25)
    turntxtrect.topright = ((screen.get_rect().right),0)
    screen.blit(dice_counter, dice_counterrect)
    screen.blit(turntxt, turntxtrect)
    pg.display.flip()#Displays screen

def printTurn(player, screen):#Displays the current player's turn
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    mytext = "It's Player "+ str(player.getPlayerNum())+"'s Turn"
    playerturn = font.render(mytext, True, TEXT_COLOUR, None)
    playerturnrect = playerturn.get_rect()
    playerturnrect.center = ((screen.get_rect().centerx),(screen.get_rect().centery))
    screen.fill(COLOUR)
    screen.blit(playerturn, playerturnrect)
    pg.display.flip()#Displays screen
    playSounds.nextPlayerSound()
    time.sleep(2)

def printDiceRoll(diceroll, screen):#Displays the amount rolled by the dice
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    mytext = "You Rolled "+ str(diceroll)
    playerdiceroll = font.render(mytext, True, TEXT_COLOUR, None)
    playerdicerollrect = playerdiceroll.get_rect()
    playerdicerollrect.center = ((screen.get_rect().centerx),(screen.get_rect().centery))
    screen.fill(COLOUR)
    screen.blit(playerdiceroll, playerdicerollrect)
    pg.display.flip()#Displays screen
    time.sleep(2)

def drawAll(screen, play_sprites, tile_sprites, pause_sprite, mytext, turntxt, turntxtrect, counterList):#Coordinates the display of the screen
    global COLOUR
    play_sprites.update()
    screen.fill(COLOUR)
    printScores(counterList, screen)
    printTxt(mytext, screen, turntxt, turntxtrect)
    printScores(counterList, screen)
    tile_sprites.draw(screen)
    play_sprites.draw(screen)
    pause_sprite.draw(screen)
    displayItems(screen, counterList)
    pg.display.flip()#Displays screen

def printInJail(screen):#Displays what the player needs to do to get out of jail
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    screen.fill(COLOUR)
    inJailTxt = font.render("To Get Out of Jail", True, TEXT_COLOUR, None)
    inJailTxtrect = inJailTxt.get_rect()
    inJailTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-80))
    screen.blit(inJailTxt, inJailTxtrect)
    diceRollTxt = font2.render("Roll a 2 or a 12", True, TEXT_COLOUR, None)
    diceRollTxtrect = diceRollTxt.get_rect()
    diceRollTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-30))
    screen.blit(diceRollTxt, diceRollTxtrect)
    pg.display.flip()#Displays screen
    time.sleep(2)

def printGetOutOfJail(screen, player, out):#Displays whether the player got out of jail or how many turns they have left
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 54)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    screen.fill(COLOUR)
    if out == 'y':#Displays text for when the player gets out of jail
        inJailTxt = font.render("You Have Been Released", True, TEXT_COLOUR, None)
        inJailTxtrect = inJailTxt.get_rect()
        inJailTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
        screen.blit(inJailTxt, inJailTxtrect)
        subTxt = font2.render("For Now", True, TEXT_COLOUR, None)
        subTxtrect = subTxt.get_rect()
        subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+25))
        screen.blit(subTxt, subTxtrect)
    else:#Displays text for when the player doesn't get out of jail
        turnsLeft = player.getInJail()
        inJailTxt = font.render("You Were Caught Trying to Escape", True, TEXT_COLOUR, None)
        inJailTxtrect = inJailTxt.get_rect()
        inJailTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
        screen.blit(inJailTxt, inJailTxtrect)
        if turnsLeft == 0:#Changes the text so that the grammar is correct
            mytext = "You'll Be Released Next Turn"
        elif turnsLeft == 1:
            mytext = "You Have " + str(turnsLeft) + " Turn Left in Jail"
        else:
            mytext = "You Have " + str(turnsLeft) + " Turns Left in Jail"
        subTxt = font2.render(mytext, True, TEXT_COLOUR, None)
        subTxtrect = subTxt.get_rect()
        subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+25))
        screen.blit(subTxt, subTxtrect)
        playSounds.jailSound()
    pg.display.flip()#Displays screen
    time.sleep(2)

def displayItems(screen, counterList):#Draws all the correct items to the screen
    gooj_sprite1, dp_sprite1, sq_sprite1, gooj_sprite2, dp_sprite2, sq_sprite2, gooj_sprite3, dp_sprite3, sq_sprite3, gooj_sprite4, dp_sprite4, sq_sprite4 = makeButtons.makeItems(counterList, screen)

    if counterList[0].getGetOutOfJail() > 0:#Displays Player 1's items
        gooj_sprite1.draw(screen)
    if counterList[0].getSkipQuestion() > 0:
        dp_sprite1.draw(screen)
    if counterList[0].getDoublePoints() > 0:
        sq_sprite1.draw(screen)

    if counterList[1].getGetOutOfJail() > 0:#Displays Player 2's items
        gooj_sprite2.draw(screen)
    if counterList[1].getSkipQuestion() > 0:
        dp_sprite2.draw(screen)
    if counterList[1].getDoublePoints() > 0:
        sq_sprite2.draw(screen)

    if len(counterList) > 2:
        if counterList[2].getGetOutOfJail() > 0:#Displays Player 3's items
            gooj_sprite3.draw(screen)
        if counterList[2].getSkipQuestion() > 0:
            dp_sprite3.draw(screen)
        if counterList[2].getDoublePoints() > 0:
            sq_sprite3.draw(screen)

    if len(counterList) == 4:
        if counterList[3].getGetOutOfJail() > 0:#Displays Player 4's items
            gooj_sprite4.draw(screen)
        if counterList[3].getSkipQuestion() > 0:
            dp_sprite4.draw(screen)
        if counterList[3].getDoublePoints() > 0:
            sq_sprite4.draw(screen)

    
