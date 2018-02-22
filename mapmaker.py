import pygame as pg
import tiles as t
import random
import os

def scaffolding(tile_folder):
    tf = tile_folder
    mymap = [[t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)]]
    return mymap

def mapInitiation(tile_sprites, game_folder):
    tile_folder = os.path.join(game_folder, "tiles")
    mymap = scaffolding(tile_folder)
    number = 0
    for i in mymap[0]:
        whichTile(mymap, 0, number, tile_folder)
        number = number + 1
    number = 0
    for i in mymap[7]:
        whichTile(mymap, 7, number, tile_folder)
        number = number + 1
    number = 1
    while number < 7:
        whichTile(mymap, number, 0, tile_folder)
        whichTile(mymap, number, 7, tile_folder)
        number = number + 1

    mymap[0][0] = t.startTile(tile_folder)
    tile_sprites.add(mymap[0][0])
    mymap[7][7] = t.endTile(tile_folder)
    tile_sprites.add(mymap[7][7])
    mymap = makeMiddle(mymap, tile_folder)
    mymap = MakeNodeRelations(mymap, tile_sprites)
    return mymap
        
def whichTile(mymap, number1, number2, tile_folder):
    rnum = random.randint(1,5)
    if rnum == 1:
        mymap[number1][number2] = t.questionTile1(tile_folder)
    elif rnum == 2:
        mymap[number1][number2] = t.questionTile2(tile_folder)
    elif rnum == 3:
        mymap[number1][number2] = t.questionTile3(tile_folder)
    elif rnum == 4:
        mymap[number1][number2] = t.chanceTile(tile_folder)
    else:
        mymap[number1][number2] = t.safeTile(tile_folder)

def MakeNodeRelations(mymap, tile_sprites):
    y = 0
    for i in mymap:
        x = 0
        for n in i:
            n.setNodes(mymap, x, y)
            tile_sprites.add(n)
            x = x + 1
        y = y + 1
    return mymap

def makeMiddle(mymap, tile_folder):
    ycoord = random.randint(2,5)
    xcoord = 1
    while xcoord < 7:
        whichTile(mymap, ycoord, xcoord, tile_folder)
        xcoord = xcoord + 1
    xcoord = random.randint(2,5)
    ycoord = 1
    while ycoord < 7:
        whichTile(mymap, ycoord, xcoord, tile_folder)
        ycoord = ycoord + 1
    return mymap

def noGo(mymap):
    donot = []
    do = []
    x = 0
    y = 0
    for i in mymap:
        for n in i:
            if str(n.getType()) == 'b':
                donot.append([x,y])
            else:
                do.append([x,y])
            x = x + 1
        y = y + 1
        x = 0
    return donot, do
