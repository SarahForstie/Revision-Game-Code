#Imports
import pygame as pg
import os
import time
import makeButtons
import playSounds

#Global variables
global COLOUR
global TEXT_COLOUR
global TEXT

TEXT_COLOUR = (255,255,255)
COLOUR = (20,2,92)
TEXT = 'saxmono.ttf'

def welcomeScreen(screen):#Displays the welcome screen
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    screen.fill(COLOUR)
    nameTxt = font.render("Revision Run", True, TEXT_COLOUR, None)
    nameTxtrect = nameTxt.get_rect()
    nameTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(nameTxt, nameTxtrect)#Displays the game's name
    subTxt = font2.render("Press Any Key To Continue", True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+20))
    screen.blit(subTxt, subTxtrect)#Displays the sub text
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when any pygame event happens
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            if event.type == pg.KEYDOWN:
                playSounds.buttonClickSound()
                done = True
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if pressed1 or pressed2 or pressed3:
                playSounds.buttonClickSound()
                done = True

def mainMenu(screen):
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    menu_buttons, menubutton_sprites = makeButtons.makeMainMenuButtons(screen)
    screen.fill(COLOUR)
    nameTxt = font.render("Revision Run", True, TEXT_COLOUR, None)
    nameTxtrect = nameTxt.get_rect()
    nameTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-200))
    screen.blit(nameTxt, nameTxtrect)#Display title
    menubutton_sprites.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when mouse 1 pygame event happens
        change = False
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if menu_buttons[0].getPressed(mousepos) == True and pressed1:#Goes to the first page of instructions
                playSounds.buttonClickSound()
                instructPG1(screen)
                change = True
            elif menu_buttons[1].getPressed(mousepos) == True and pressed1:#Goes to the player choice screen
                playSounds.buttonClickSound()
                players = playerCount(screen)
                if players != 0:
                    done = True
                else:
                    change = True
        if change == True:#Redraws the screen when the other menus are accessed
            screen.fill(COLOUR)
            nameTxt = font.render("Revision Run", True, TEXT_COLOUR, None)
            nameTxtrect = nameTxt.get_rect()
            nameTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-200))
            screen.blit(nameTxt, nameTxtrect)
            menubutton_sprites.draw(screen)
            pg.display.flip()
    return players
            

def instructPG1(screen):
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    backbutton_sprites, backbutton, nextbutton_sprites, nextbutton, aimOfGame_sprite, tileDisplay_sprite, tileExplain_sprite, itemExplain_sprite = makeButtons.makeInstructionMenuButtons(screen)
    screen.fill(COLOUR)
    HowToPlayTxt = font.render("How to Play", True, TEXT_COLOUR, None)
    HowToPlayTxtrect = HowToPlayTxt.get_rect()
    HowToPlayTxtrect.midtop = ((screen.get_rect().centerx),(screen.get_rect().top))
    screen.blit(HowToPlayTxt, HowToPlayTxtrect)
    backbutton_sprites.draw(screen)
    nextbutton_sprites.draw(screen)
    aimOfGame_sprite.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when mouse 1 pygame event happens
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if backbutton.getPressed(mousepos) == True and pressed1:#Returns to the last page
                playSounds.buttonClickSound()
                done = True
            elif nextbutton.getPressed(mousepos) == True and pressed1:#draws the next page of the instructions then redraws the screen when it's exited
                playSounds.buttonClickSound()
                instructPG2(screen, backbutton_sprites, backbutton, nextbutton_sprites, nextbutton, tileDisplay_sprite, tileExplain_sprite, itemExplain_sprite)
                screen.fill(COLOUR)
                screen.blit(HowToPlayTxt, HowToPlayTxtrect)
                backbutton_sprites.draw(screen)
                nextbutton_sprites.draw(screen)
                aimOfGame_sprite.draw(screen)
                pg.display.flip()#Displays screen

def instructPG2(screen, backbutton_sprites, backbutton, nextbutton_sprites, nextbutton, tileDisplay_sprite, tileExplain_sprite, itemExplain_sprite):
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    screen.fill(COLOUR)
    tilesTxt = font.render("Tiles", True, TEXT_COLOUR, None)
    tilesTxtrect = tilesTxt.get_rect()
    tilesTxtrect.midtop = ((screen.get_rect().centerx),(screen.get_rect().top))
    screen.blit(tilesTxt, tilesTxtrect)
    backbutton_sprites.draw(screen)
    nextbutton_sprites.draw(screen)
    tileDisplay_sprite.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when mouse 1 pygame event happens
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if backbutton.getPressed(mousepos) == True and pressed1:#Returns to the last page
                playSounds.buttonClickSound()
                done = True
            elif nextbutton.getPressed(mousepos) == True and pressed1:#draws the next page of the instructions then redraws the screen when it's exited
                playSounds.buttonClickSound()
                instructPG3(screen, backbutton_sprites, backbutton, nextbutton_sprites, nextbutton, tileExplain_sprite, itemExplain_sprite)
                screen.fill(COLOUR)
                screen.blit(tilesTxt, tilesTxtrect)
                backbutton_sprites.draw(screen)
                nextbutton_sprites.draw(screen)
                tileDisplay_sprite.draw(screen)
                pg.display.flip()#Displays screen

def instructPG3(screen, backbutton_sprites, backbutton, nextbutton_sprites, nextbutton, tileExplain_sprite, itemExplain_sprite):
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    screen.fill(COLOUR)
    tilesTxt = font.render("What the Tiles Do", True, TEXT_COLOUR, None)
    tilesTxtrect = tilesTxt.get_rect()
    tilesTxtrect.midtop = ((screen.get_rect().centerx),(screen.get_rect().top))
    screen.blit(tilesTxt, tilesTxtrect)
    backbutton_sprites.draw(screen)
    nextbutton_sprites.draw(screen)
    tileExplain_sprite.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when mouse 1 pygame event happens
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if backbutton.getPressed(mousepos) == True and pressed1:#Returns to the last page
                playSounds.buttonClickSound()
                done = True
            elif nextbutton.getPressed(mousepos) == True and pressed1:#draws the next page of the instructions then redraws the screen when it's exited
                playSounds.buttonClickSound()
                instructPG4(screen, backbutton_sprites, backbutton, itemExplain_sprite)
                screen.fill(COLOUR)
                screen.blit(tilesTxt, tilesTxtrect)
                backbutton_sprites.draw(screen)
                nextbutton_sprites.draw(screen)
                tileExplain_sprite.draw(screen)
                pg.display.flip()#Displays screen

def instructPG4(screen, backbutton_sprites, backbutton, itemExplain_sprite):
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    screen.fill(COLOUR)
    tilesEffectTxt = font.render("Items", True, TEXT_COLOUR, None)
    tilesEffectTxtrect = tilesEffectTxt.get_rect()
    tilesEffectTxtrect.midtop = ((screen.get_rect().centerx),(screen.get_rect().top))
    screen.blit(tilesEffectTxt, tilesEffectTxtrect)
    backbutton_sprites.draw(screen)
    itemExplain_sprite.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when mouse 1 pygame event happens
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if backbutton.getPressed(mousepos) == True and pressed1:#Returns to the last page
                playSounds.buttonClickSound()
                done = True

def playerCount(screen):
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 44)

    #Displays the text
    backbutton_sprites, backbutton, playernumbutton_sprites, player_buttons = makeButtons.makePlayerMenuButtons(screen)
    screen.fill(COLOUR)
    playerCountTxt = font.render("Choose the Amount of Players", True, TEXT_COLOUR, None)
    playerCountTxtrect = playerCountTxt.get_rect()
    playerCountTxtrect.midtop = ((screen.get_rect().centerx),(screen.get_rect().top))
    screen.blit(playerCountTxt, playerCountTxtrect)
    backbutton_sprites.draw(screen)
    playernumbutton_sprites.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when mouse 1 pygame event happens
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if player_buttons[0].getPressed(mousepos) == True and pressed1:#Sets the players to 2
                playSounds.buttonClickSound()
                returning = 2
                done = True
            elif player_buttons[1].getPressed(mousepos) == True and pressed1:#Sets the players to 3
                playSounds.buttonClickSound()
                returning = 3
                done = True
            elif player_buttons[2].getPressed(mousepos) == True and pressed1:#Sets the players to 4
                playSounds.buttonClickSound()
                returning = 4
                done = True
            elif backbutton.getPressed(mousepos) == True and pressed1:#Returns to the main menu
                playSounds.buttonClickSound()
                returning = 0
                done = True
    return returning

def scoreMenu(screen, game_folder, counterList, multipliers):
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    back_button, backbutton_sprite = makeButtons.makeScoreMenuButtons(screen)
    playSounds.winningSound()
    screen.fill(COLOUR)
    resultTxt = font.render("RESULTS", True, TEXT_COLOUR, None)
    resultTxtrect = resultTxt.get_rect()
    resultTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery) - 250))
    screen.blit(resultTxt, resultTxtrect)
    backbutton_sprite.draw(screen)
    winnerTxt = font.render("Congratulations", True, TEXT_COLOUR, None)
    winnerTxtrect = winnerTxt.get_rect()
    winnerTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery) + 450))
    screen.blit(winnerTxt, winnerTxtrect)
    backbutton_sprite.draw(screen)
    startycoord = (screen.get_rect().centery) - 100
    
    multiply = 4
    for i in multipliers:#Implements the point multipliers
        i.setMultiplier(multiply)
        multiply = multiply - 1
        
    for i in counterList:#Displays each players scores
        mytext = "Player "+ str(i.getPlayerNum())+": " + str(i.getPlayerPoints())
        playerscore = font.render(mytext, True, TEXT_COLOUR, None)
        playerscorerect = playerscore.get_rect()
        playerscorerect.center = ((screen.get_rect().centerx),(startycoord+50))
        startycoord = startycoord + 65
        screen.blit(playerscore, playerscorerect)
        pg.display.flip()#Displays screen
        
    done = False
    while not done:#A loop which ends when mouse 1 pygame event happens
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if back_button.getPressed(mousepos) == True and pressed1:#Sends user to the main menu
                playSounds.buttonClickSound()
                done = True

def pauseMenu(screen):
    #Defines the text look
    global COLOUR
    global TEXT_COLOUR
    global TEXT
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    menu_buttons, menubutton_sprites = makeButtons.makePauseMenuButtons(screen)
    mytext = "PAUSED"
    pausedTxt = font.render(mytext, True, TEXT_COLOUR, None)
    pausedTxtrect = pausedTxt.get_rect()
    pausedTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-250))
    screen.fill(COLOUR)
    screen.blit(pausedTxt, pausedTxtrect)
    menubutton_sprites.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#A loop which ends when mouse 1 pygame event happens
        for event in pg.event.get():
                if event.type == pg.QUIT:#Exits the game
                    pg.quit()
        mousepos = pg.mouse.get_pos()
        pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
        if menu_buttons[0].getPressed(mousepos) == True and pressed1:#Resumes the game
            returning = False
            playSounds.buttonClickSound()
            done = True
        elif menu_buttons[1].getPressed(mousepos) == True and pressed1:#Exits to the main menu
            returning = True
            playSounds.buttonClickSound()
            done = True

    return returning
