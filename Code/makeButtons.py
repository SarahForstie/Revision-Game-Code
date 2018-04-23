#Imports
import pygame as pg
import button
import os
import menuText
import itemSprites

def makeScoreMenuButtons(screen):#Makes the buttons for the score menu
    game_folder = os.path.dirname(__file__)#Makes the file path of the game
    button_folder = os.path.join(game_folder, "buttons")#Makes the file path of the button images
    backbutton_sprite = pg.sprite.Group()#Score menu button sprite group
    
    backbutton = button.backBut(button_folder, screen)#Allows the button to be accessed
    backbutton_sprite.add(backbutton)
    
    return backbutton, backbutton_sprite

def makePauseMenuButtons(screen):#Makes the buttons for the pause menu
    game_folder = os.path.dirname(__file__)#Makes the file path of the game
    button_folder = os.path.join(game_folder, "buttons")#Makes the file path of the button images
    menubutton_sprites = pg.sprite.Group()#Pause menu button sprite group

    resumebutton = button.resumeBut(button_folder, screen)
    menubutton_sprites.add(resumebutton)
    tomenubutton = button.tomenuBut(button_folder, screen)
    menubutton_sprites.add(tomenubutton)
    menu_buttons = [resumebutton, tomenubutton]#Allows the buttons to be accessed individually

    return menu_buttons, menubutton_sprites
    
def makeMainMenuButtons(screen):#Makes the buttons for the main menu
    game_folder = os.path.dirname(__file__)#Makes the file path of the game
    button_folder = os.path.join(game_folder, "buttons")#Makes the file path of the button images
    menubutton_sprites = pg.sprite.Group()#Main menu button sprite group
    
    instructionbutton = button.instructBut(button_folder, screen)
    menubutton_sprites.add(instructionbutton)
    playbutton = button.playBut(button_folder, screen)
    menubutton_sprites.add(playbutton)

    menu_buttons = [instructionbutton, playbutton]#Allows the buttons to be accessed individually
    
    return menu_buttons, menubutton_sprites
    
def makeInstructionMenuButtons(screen):#Makes the buttons for the instructions menus
    game_folder = os.path.dirname(__file__)#Makes the file path of the game
    button_folder = os.path.join(game_folder, "buttons")#Makes the file path of the button images
    menu_folder = os.path.join(game_folder, "menu")#Makes the file path of the menu images
    backbutton_sprites = pg.sprite.Group()#Back button sprite group
    nextbutton_sprites = pg.sprite.Group()#Next button sprite group
    aimOfGame_sprite = pg.sprite.Group()#Aim of the game image sprite group
    tileDisplay_sprite = pg.sprite.Group()#Tile display image sprite group
    tileExplain_sprite = pg.sprite.Group()#Tile explain image sprite group
    itemExplain_sprite = pg.sprite.Group()#Item explain image sprite group

    backbutton = button.backBut(button_folder, screen)#Allows the button to be accessed
    backbutton_sprites.add(backbutton)
    nextbutton = button.nextBut(button_folder, screen)#Allows the button to be accessed
    nextbutton_sprites.add(nextbutton)

    aimOfGame_sprite.add(menuText.aimOfGame(menu_folder, screen))
    tileDisplay_sprite.add(menuText.tileDisplay(menu_folder, screen))
    tileExplain_sprite.add(menuText.tileExplain(menu_folder, screen))
    itemExplain_sprite.add(menuText.itemExplain(menu_folder, screen))

    return backbutton_sprites, backbutton, nextbutton_sprites, nextbutton, aimOfGame_sprite, tileDisplay_sprite, tileExplain_sprite, itemExplain_sprite

def makePlayerMenuButtons(screen):#Makes the buttons for the player menu
    game_folder = os.path.dirname(__file__)#Makes the file path of the game
    button_folder = os.path.join(game_folder, "buttons")#Makes the file path of the button images
    backbutton_sprites = pg.sprite.Group()#Back button sprite group
    nextbutton_sprites = pg.sprite.Group()#Next button sprite group
    playernumbutton_sprites = pg.sprite.Group()#player buttons sprite group

    backbutton = button.backBut(button_folder, screen)#Allows the button to be accessed
    backbutton_sprites.add(backbutton)
    twoPlayers = button.player2But(button_folder, screen)#2 player button
    playernumbutton_sprites.add(twoPlayers)
    threePlayers = button.player3But(button_folder, screen)#3 player button
    playernumbutton_sprites.add(threePlayers)
    fourPlayers = button.player4But(button_folder, screen)#4 player button
    playernumbutton_sprites.add(fourPlayers)

    player_buttons = [twoPlayers, threePlayers, fourPlayers]#Allows the buttons to be accessed individually

    return backbutton_sprites, backbutton, playernumbutton_sprites, player_buttons

def makeButtonsToPlay(screen, ABCDbutton_sprites, YNbutton_sprites, dice_sprite, pause_sprite, pauseMenu_sprites):#Makes the pause, answer and quit buttons
    game_folder = os.path.dirname(__file__)#Makes the file path of the game
    button_folder = os.path.join(game_folder, "buttons")#Makes the file path of the button images

    buttonA = button.aKey(button_folder, screen)#Answer A button
    ABCDbutton_sprites.add(buttonA)
    buttonB = button.bKey(button_folder, screen)#Answer B button
    ABCDbutton_sprites.add(buttonB)
    buttonC = button.cKey(button_folder, screen)#Answer C button
    ABCDbutton_sprites.add(buttonC)
    buttonD = button.dKey(button_folder, screen)#Answer D button
    ABCDbutton_sprites.add(buttonD)
    ABCDbuttonList = [buttonA, buttonB, buttonC, buttonD]#Allows the buttons to be accessed individually

    buttonY = button.yKey(button_folder, screen)#Y button
    YNbutton_sprites.add(buttonY)
    buttonN = button.nKey(button_folder, screen)#N button
    YNbutton_sprites.add(buttonN)
    YNbuttonList = [buttonY, buttonN]#Allows the buttons to be accessed individually

    diceButton = button.diceBut(button_folder, screen)#Allows the button to be accessed
    dice_sprite.add(diceButton)
    pauseButton = button.pauseBut(button_folder, screen)#Allows the button to be accessed
    pause_sprite.add(pauseButton)

    continueButton = button.pauseBut(button_folder, screen)#Continue button
    pauseMenu_sprites.add(continueButton)
    toMenuButton = button.pauseBut(button_folder, screen)#To the menu button
    pauseMenu_sprites.add(toMenuButton)
    pauseMenuList = [continueButton, toMenuButton]#Allows the buttons to be accessed individually

    return ABCDbuttonList, YNbuttonList, diceButton, pauseButton, pauseMenuList

def makeSpriteGroups():#Makes Sprite groups for the buttons
    play_sprites = pg.sprite.Group()#Player sprite group
    ABCDbutton_sprites = pg.sprite.Group()#Answer sprite group
    YNbutton_sprites = pg.sprite.Group()#Y or N sprite group
    tile_sprites = pg.sprite.Group()#Tile sprite group
    dice_sprite = pg.sprite.Group()#Dice sprite group
    pause_sprite = pg.sprite.Group()#Pause sprite group
    pauseMenu_sprites = pg.sprite.Group()#Pause menu sprite group
    return play_sprites, ABCDbutton_sprites, YNbutton_sprites, tile_sprites, dice_sprite, pause_sprite, pauseMenu_sprites

def makeItems(counterList, screen):#Makes the item sprites
    game_folder = os.path.dirname(__file__)#Makes the file path of the game
    item_folder = os.path.join(game_folder, "items")#Makes the file path of the item images
    
    gooj_sprite1 = pg.sprite.Group()#Get out of jail free sprite group for player 1
    gooj_sprite1.add(itemSprites.getOutOfJailItem1(item_folder, screen))
    dp_sprite1 = pg.sprite.Group()#Double points sprite group for player 1
    dp_sprite1.add(itemSprites.doublePointsItem1(item_folder, screen))
    sq_sprite1 = pg.sprite.Group()#Skip question sprite group for player 1
    sq_sprite1.add(itemSprites.skipQuestionItem1(item_folder, screen))

    gooj_sprite2 = pg.sprite.Group()#Get out of jail free sprite group for player 2
    gooj_sprite2.add(itemSprites.getOutOfJailItem2(item_folder, screen))
    dp_sprite2 = pg.sprite.Group()#Double points sprite group for player 2
    dp_sprite2.add(itemSprites.doublePointsItem2(item_folder, screen))
    sq_sprite2 = pg.sprite.Group()#Skip question sprite group for player 2
    sq_sprite2.add(itemSprites.skipQuestionItem2(item_folder, screen))

    gooj_sprite3 = pg.sprite.Group()#Get out of jail free sprite group for player 3
    gooj_sprite3.add(itemSprites.getOutOfJailItem3(item_folder, screen))
    dp_sprite3 = pg.sprite.Group()#Double points sprite group for player 3
    dp_sprite3.add(itemSprites.doublePointsItem3(item_folder, screen))
    sq_sprite3 = pg.sprite.Group()#Skip question sprite group for player 3
    sq_sprite3.add(itemSprites.skipQuestionItem3(item_folder, screen))

    gooj_sprite4 = pg.sprite.Group()#Get out of jail free sprite group for player 4
    gooj_sprite4.add(itemSprites.getOutOfJailItem4(item_folder, screen))
    dp_sprite4 = pg.sprite.Group()#Double points sprite group for player 4
    dp_sprite4.add(itemSprites.doublePointsItem4(item_folder, screen))
    sq_sprite4 = pg.sprite.Group()#Skip question sprite group for player 4
    sq_sprite4.add(itemSprites.skipQuestionItem4(item_folder, screen))

    return gooj_sprite1, dp_sprite1, sq_sprite1, gooj_sprite2, dp_sprite2, sq_sprite2, gooj_sprite3, dp_sprite3, sq_sprite3, gooj_sprite4, dp_sprite4, sq_sprite4
