#Imports
import pygame as pg
import os

#Global variables
global game_folder
global sound_folder

game_folder = os.path.dirname(__file__)
sound_folder = os.path.join(game_folder, "sounds")

def buttonClickSound():
    #A sound for when a button is clicked
    global sound_folder
    button_sound = pg.mixer.Sound(os.path.join(sound_folder, "buttonPush.wav"))
    button_sound.play()

def winningSound():
    #A sound for when the scores are displayed
    global sound_folder
    victory_sound = pg.mixer.Sound(os.path.join(sound_folder, "winning.wav"))
    victory_sound.play()
    
def diceSound():
    #A sound for when the dice is rolled
    global sound_folder
    dice_sound = pg.mixer.Sound(os.path.join(sound_folder, "diceRoll.wav"))
    dice_sound.play()

def counterMoveSound():
    #A sound for when the counter moves
    global sound_folder
    counter_sound = pg.mixer.Sound(os.path.join(sound_folder, "counterPop.wav"))
    counter_sound.play()

def nextPlayerSound():
    #A sound for when the next player is announced
    global sound_folder
    next_sound = pg.mixer.Sound(os.path.join(sound_folder, "nextPlayer.wav"))
    next_sound.play()

def teleportSound():
    #A sound for when a player is teleported
    global sound_folder
    teleport_sound = pg.mixer.Sound(os.path.join(sound_folder, "teleport.wav"))
    teleport_sound.play()

def coinExchangeSound():
    #A sound for when points are exchanged
    global sound_folder
    coin_sound = pg.mixer.Sound(os.path.join(sound_folder, "pointExchange.wav"))
    coin_sound.play()

def goToJailSound():
    #A sound for when a player is sent to jail
    global sound_folder
    jail_sound = pg.mixer.Sound(os.path.join(sound_folder, "goToJail.wav"))
    jail_sound.play()

def correctOrWrongSound(correct):
    #A sound for when a player answers a question
    global sound_folder
    if correct == 'y':
        correct_sound = pg.mixer.Sound(os.path.join(sound_folder, "correctAnswer.wav"))
        correct_sound.play()
    elif correct == 'n':
        wrong_sound = pg.mixer.Sound(os.path.join(sound_folder, "wrongAnswer.wav"))
        wrong_sound.play()

def jailSound():
    #A sound for when a player is in jail
    global sound_folder
    jail_sound = pg.mixer.Sound(os.path.join(sound_folder, "jail.wav"))
    jail_sound.play()

def timeUp():
    #A sound for when the time runs out
    global sound_folder
    jail_sound = pg.mixer.Sound(os.path.join(sound_folder, "timeUp.wav"))
    jail_sound.play()
