#Imports
import pygame as pg
import os
import play
import menus

def makeScreen():#Makes the pygame surface and returns it
    width  = 960
    height = 640
    pg.init()
    pg.display.set_caption('Revision Run')
    screen = pg.display.set_mode([width, height])
    pg.font.init()
    return screen

def main():#The main function
    screen = makeScreen()#Calls the make screen function
    game_folder = os.path.dirname(__file__)#Makes the file path of the game
    menus.welcomeScreen(screen)#Displays the welcome screen
    done = False
    while not done:#Makes a loop
        players = menus.mainMenu(screen)#Calls the main menu function to get the amount of players
        counterList, multipliers = play.play(screen, players, game_folder)#Plays the game
        menus.scoreMenu(screen, game_folder, counterList, multipliers)#Displays the scores
            

main()#Calls main
pg.quit()#Quits pygame
