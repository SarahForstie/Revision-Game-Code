#Imports
import pygame as pg
import tiles as t
import random
import os

#Global variables
global len_of_mymap_minus#Global as isn't changed by any functions

#Global tile amounts because it's easier to track is is only changed in one function
global q1TileAmount
global q2TileAmount
global q3TileAmount
global saTileAmount
global cTileAmount

q1TileAmount = 38#Amount of question tile 1
q2TileAmount = 28#Amount of question tile 2
q3TileAmount = 18#Amount of question tile 3
saTileAmount = 10#Amount of safe tiles
cTileAmount = 12#Amount of chance tiles

len_of_mymap = 10
len_of_mymap_minus = len_of_mymap - 1


def scaffolding(tile_folder):#Makes a 2d list of blank tiles as a template of tiles
    tf = tile_folder
    mymap = [[t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)],
             [t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf), t.blankTile(tf)]]
    return mymap

def mapInitiation(tile_sprites, game_folder):#Coordinates the creation of the tile map
    tile_folder = os.path.join(game_folder, "tiles")#Makes the file path of the tile images folder
    mymap = scaffolding(tile_folder)

    #Makes the boarder of tiles for the game board
    number = 0
    for i in mymap[0]:#Makes the tiles on the top of the board
        whichTile(mymap, 0, number, tile_folder)
        number = number + 1
    number = 0
    for i in mymap[len_of_mymap_minus]:#Makes the tiles on the bottom of the board
        whichTile(mymap, len_of_mymap_minus, number, tile_folder)
        number = number + 1
    number = 1
    while number < len_of_mymap_minus:#Makes the tiles on the left and right of the board
        whichTile(mymap, number, 0, tile_folder)
        whichTile(mymap, number, len_of_mymap_minus, tile_folder)
        number = number + 1

    mymap[0][0] = t.startTile(tile_folder)#Makes the start tile in a set place
    mymap[len_of_mymap_minus][len_of_mymap_minus] = t.endTile(tile_folder)#Makes the end tile in a set place
    
    randomXorY = random.randint(0,10)#Decides whether the random path will be across or down
    if randomXorY % 2 == 0:
        mymap = randomXpath(mymap, tile_folder)#Random path will be across
    else:
        mymap = randomYpath(mymap, tile_folder)#Random path will be down

    #Makes the inner corners blank tiles
    mymap[1][1] = t.blankTile(tile_folder)
    mymap[len_of_mymap_minus - 1][1] = t.blankTile(tile_folder)
    mymap[1][len_of_mymap_minus - 1] = t.blankTile(tile_folder)
    mymap[len_of_mymap_minus - 1][len_of_mymap_minus - 1] = t.blankTile(tile_folder)
    
    noGo, yesGo = noOrYesGo(mymap)
    mymap, jailtile  = makeJail(mymap, tile_folder, yesGo)#Makes the jail and the go to jail tile
    mymap = MakeNodeRelations(mymap, tile_sprites)#Sets the tiles surroundings

    return mymap, noGo, yesGo, jailtile
        
def whichTile(mymap, number1, number2, tile_folder):#Changes one of the blank tiles into a different tile
    #Global variables
    global q1TileAmount
    global q2TileAmount
    global q3TileAmount
    global saTileAmount
    global cTileAmount
    
    done = False
    while not done:#Makes a loop until a tile has been changed
        randomnum = random.randint(1,5)#For choosing a random tile type
        if randomnum == 1 and q1TileAmount > 0:#Question 1 tile
            mymap[number1][number2] = t.questionTile1(tile_folder)
            q1TileAmount = q1TileAmount - 1
            done = True
        elif randomnum == 2 and q2TileAmount > 0:#Question 2 tile
            mymap[number1][number2] = t.questionTile2(tile_folder)
            q2TileAmount = q2TileAmount - 1
            done = True
        elif randomnum == 3 and q3TileAmount > 0:#Question 3 tile
            mymap[number1][number2] = t.questionTile3(tile_folder)
            q3TileAmount = q3TileAmount - 1
            done = True
        elif randomnum == 4 and cTileAmount > 0:#Chance tile
            mymap[number1][number2] = t.chanceTile(tile_folder)
            cTileAmount = cTileAmount - 1
            done = True
        elif randomnum == 5 and saTileAmount > 0:#Safe tile
            mymap[number1][number2] = t.safeTile(tile_folder)
            saTileAmount = saTileAmount - 1
            done = True

def MakeNodeRelations(mymap, tile_sprites):#Sets the tiles surroundings
    y = 0
    for i in mymap:#Loops through all nodes in the array
        x = 0
        counter = 0
        for n in i:
            counter += 1
            n.setNodes(mymap, x, y, len_of_mymap)
            tile_sprites.add(n)#Adds the current tile to the tile sprite group for display
            x = x + 1
        y = y + 1
    return mymap

def noOrYesGo(mymap):#Returns a list of tiles which can or can't be moved onto
    dontgo = []
    dogo = []
    x = 0
    y = 0
    for i in mymap:
        for n in i:
            if str(n.getType()) == 'b':#If the tile type is blank then its position is added to dontgo list
                dontgo.append([x,y])
            else:
                dogo.append([x,y])#If the tile type isn't blank then its position is added to dogo list
            x = x + 1
        y = y + 1
        x = 0
    return dontgo, dogo

def randomXpath(mymap, tile_folder):#Makes a random path across the board
    done = False
    visited = []#Makes a list of coordinates that the path has been placed on
    mymapy = random.randint(2, len_of_mymap_minus - 2)#Random y coordinate for the path to start
    mymapx = 1#The path starts one x coordinate in
    whichTile(mymap, mymapy, mymapx, tile_folder)
    visited.append([mymapx,mymapy])

    while not done:
        UorD = random.randint(0,12)
        
        if mymapx == (len_of_mymap_minus - 1):#Stops the path when the path raches the right side
            done = True
            
        elif (UorD % 3 != 0) and (mymapx > 1):#Makes the path go either up or down
            PorM = random.randint(0,12)
            if (PorM % 2 == 0) and (mymapy < (len_of_mymap_minus - 2)):#Makes the path go down one
                mymapy = mymapy + 1
                if ([(mymapx + 1),mymapy] not in visited) and ([(mymapx - 1),mymapy] not in visited) and ([mymapx,mymapy] not in visited):
                    whichTile(mymap, mymapy, mymapx, tile_folder)
                    visited.append([mymapx,mymapy])
                else:
                    mymapy = mymapy - 1
            elif (PorM % 2 != 0) and (mymapx > 2):#Makes the path go up one
                mymapy = mymapy - 1
                if ([(mymapx + 1),mymapy] not in visited) and ([(mymapx - 1),mymapy] not in visited) and ([mymapx,mymapy] not in visited):
                    whichTile(mymap, mymapy, mymapx, tile_folder)
                    visited.append([mymapx,mymapy])
                else:
                    mymapy = mymapy + 1
            else:
                pass

        elif (UorD % 3 == 0):#Makes the path go forward
            mymapx = mymapx + 1
            whichTile(mymap, mymapy, mymapx, tile_folder)
            visited.append([mymapx,mymapy])
            
    across = random.randint(0,10)
    if across % 2 == 0:#Decides whether the straight paths are horizontal or vertical
        mymap = Ypaths(mymap, tile_folder, visited)#Makes vertical paths
    else:
        mymap = Xpaths(mymap, tile_folder, visited)#Makes horizontal paths
    return mymap

def randomYpath(mymap, tile_folder):
    done = False
    visited = []#Makes a list of coordinates that the path has been placed on
    mymapy = 1#The path starts one y coordinate in
    mymapx = random.randint(2, len_of_mymap_minus - 2)#Random x coordinate for the path to start
    whichTile(mymap, mymapy, mymapx, tile_folder)
    visited.append([mymapx,mymapy])

    while not done:
        UorD = random.randint(0,12)
        
        if mymapy == (len_of_mymap_minus - 1):#Stops the path when the path raches the bottom
            done = True
            
        elif (UorD % 3 != 0) and (mymapy > 1):#Makes the path go either left or right
            PorM = random.randint(0,12)
            if (PorM % 2 == 0) and (mymapx < (len_of_mymap_minus - 2)):#Makes the path go right one
                mymapx = mymapx + 1
                if ([mymapx,(mymapy + 1)] not in visited) and ([mymapx,(mymapy - 1)] not in visited) and ([mymapx,mymapy] not in visited):
                    whichTile(mymap, mymapy, mymapx, tile_folder)
                    visited.append([mymapx,mymapy])
                else:
                    mymapx = mymapx - 1
            elif (PorM % 2 != 0) and (mymapx > 2):#Makes the path go left one
                mymapx = mymapx - 1
                if ([mymapx,(mymapy + 1)] not in visited) and ([mymapx,(mymapy - 1)] not in visited) and ([mymapx,mymapy] not in visited):
                    whichTile(mymap, mymapy, mymapx, tile_folder)
                    visited.append([mymapx,mymapy])
                else:
                    mymapx = mymapx + 1
            else:
                pass

        elif (UorD % 3 == 0):
            mymapy = mymapy + 1
            whichTile(mymap, mymapy, mymapx, tile_folder)
            visited.append([mymapx,mymapy])
            
    across = random.randint(0,10)
    if across % 2 == 0:#Decides whether the straight paths are horizontal or vertical
        mymap = Ypaths(mymap, tile_folder, visited)#Makes vertical paths
    else:
        mymap = Xpaths(mymap, tile_folder, visited)#Makes horizontal paths
    return mymap

def Xpaths(mymap, tile_folder, visited):#Makes randomly placed horizontal straight paths
    done = False
    amount_of_paths = random.randint(2,4)#Decides how many paths are created
    while not done:
        if amount_of_paths > 0:
            leftorRight = random.randint(0,10)#Decides if the path goes left or right
            if leftorRight % 2 == 0:#Makes the path come from the left
                mymapy = random.randint(2, len_of_mymap_minus - 2)#Makes the y random
                mymapx = 1#Sets the x on the left side
                if ([mymapx,(mymapy + 1)] not in visited) and ([mymapx,(mymapy - 1)] not in visited) and ([mymapx,mymapy] not in visited):
                    done2 = False
                    while not done2:#Makes the path
                        whichTile(mymap, mymapy, mymapx, tile_folder)
                        visited.append([mymapx,mymapy])
                        if mymapx == len_of_mymap_minus:
                            amount_of_paths = amount_of_paths - 1
                            done2 = True
                        if ([mymapx,(mymapy + 1)] not in visited) and ([mymapx,(mymapy - 1)] not in visited) and ([(mymapx + 1),mymapy] not in visited):
                            mymapx = mymapx + 1
                        else:
                            amount_of_paths = amount_of_paths - 1
                            done2 = True
                else:
                    pass
            elif leftorRight % 2 != 0:#Makes the path come from the right
                mymapy = random.randint(2, len_of_mymap_minus - 2)#Makes the y random
                mymapx = len_of_mymap_minus#Sets the x on the right hand side
                if ([mymapx,(mymapy + 1)] not in visited) and ([mymapx,(mymapy - 1)] not in visited) and ([mymapx,mymapy] not in visited):
                    done2 = False
                    while not done2:#Makes the path
                        whichTile(mymap, mymapy, mymapx, tile_folder)
                        visited.append([mymapx,mymapy])
                        if mymapx == 1:
                            amount_of_paths = amount_of_paths - 1
                            done2 = True
                        if ([mymapx,(mymapy + 1)] not in visited) and ([mymapx,(mymapy - 1)] not in visited) and ([(mymapx - 1),mymapy] not in visited):
                            mymapx = mymapx - 1
                        else:
                            amount_of_paths = amount_of_paths - 1
                            done2 = True
                else:
                    pass
        elif amount_of_paths == 0:#Stops the loop
            done = True
        else:
            pass

    return mymap

def Ypaths(mymap, tile_folder, visited):#Makes randomly placed vertical straight paths
    done = False
    amount_of_paths = random.randint(2,4)#Decides how many paths are created
    while not done:
        if amount_of_paths > 0:
            UporDown = random.randint(0,10)#Decides if the path goes up or down
            if UporDown % 2 == 0:#Makes the path come from the top
                mymapy = 1#Sets the y at the top
                mymapx = random.randint(2, len_of_mymap_minus - 2)#Makes the x random
                if ([(mymapx + 1),mymapy] not in visited) and ([(mymapx - 1),mymapy] not in visited) and ([mymapx,mymapy] not in visited):
                    done2 = False
                    while not done2:#Makes the path
                        whichTile(mymap, mymapy, mymapx, tile_folder)
                        visited.append([mymapx,mymapy])
                        if mymapy == len_of_mymap_minus:
                            amount_of_paths = amount_of_paths - 1
                            done2 = True
                        if ([(mymapx + 1),mymapy] not in visited) and ([(mymapx - 1),mymapy] not in visited) and ([mymapx ,(mymapy + 1)] not in visited):
                            mymapy = mymapy + 1
                        else:
                            amount_of_paths = amount_of_paths - 1
                            done2 = True
                else:
                    pass
            elif UporDown % 2 != 0:#Makes the path come from the bottom
                mymapy = random.randint(2, len_of_mymap_minus - 2)#Makes the y random
                mymapx = len_of_mymap_minus#Sets the x at the bottom
                if ([(mymapx + 1),mymapy] not in visited) and ([(mymapx - 1),mymapy] not in visited) and ([mymapx,mymapy] not in visited):
                    done2 = False
                    while not done2:#Makes the path
                        whichTile(mymap, mymapy, mymapx, tile_folder)
                        visited.append([mymapx,mymapy])
                        if mymapy == 1:
                            amount_of_paths = amount_of_paths - 1
                            done2 = True
                        if ([(mymapx + 1),mymapy] not in visited) and ([(mymapx - 1),mymapy] not in visited) and ([mymapx ,(mymapy + 1)] not in visited):
                            mymapy = mymapy - 1
                        else:
                            amount_of_paths = amount_of_paths - 1
                            done2 = True
                else:
                    pass
        elif amount_of_paths == 0:#Stops the loop
            done = True
        else:
            pass

    return mymap

def makeJail(mymap, tile_folder, yesGo):#Sets the jail and the get out of jail tiles
    done = False
    while not done:#Randomly places the jail tile in nearly any position that is allowed to be moved onto
        jail_location = yesGo[random.randint(0,len_of_mymap_minus)]
        if (jail_location != [0,0]) and (jail_location != [len_of_mymap_minus, len_of_mymap_minus]):
            mymap[jail_location[0]][jail_location[1]] = t.jailTile(tile_folder)
            done = True

    done = False
    while not done:#Randomly places the go to jail tile in nearly any position that is allowed to be moved onto
        gotojail_location = yesGo[random.randint(0,len_of_mymap_minus)]
        if (gotojail_location != [0,0]) and (gotojail_location != [len_of_mymap_minus, len_of_mymap_minus]) and (gotojail_location != jail_location):
            mymap[gotojail_location[0]][gotojail_location[1]] = t.gotojailTile(tile_folder)
            done = True

    return mymap, jail_location
