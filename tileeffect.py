import pygame as pg
import tiles as t
import random
import mapmaker as mmake
import counters
import os
import button
import time

def getTileEffect(mymap, player, x, y, qp1, qp2, qp3, screen, ABCDbutton_sprites, YNbutton_sprites, ABCDbuttonList, YNbuttonList, yesGo):
    if player == 0:
        pass
    elif int(player.getFinished()) == 1:
        pass
    else:
        currenttile = mymap[y][x]
        tiletype = str(currenttile.getType())
        if tiletype == 'q1':
            length = (len(qp1) - 1)
            q = random.randint(0, length)
            q = qp1[q]
            question = q[0]
            a1 = q[1]
            a2 = q[2]
            a3 = q[3]
            a4 = q[4]
            ca = q[5]
            preQDisplay(screen, tiletype, question, a1, a2, a3, a4)
            myans = getAns(screen, tiletype, ABCDbutton_sprites, ABCDbuttonList)
            if myans == int(ca):
                print("\nCorrect!")
                displayWorR(screen, 'r', tiletype)
                player.setPlayerPoints(20)
            else:
                if int(ca) == 1:
                    ca = a1
                elif int(ca) == 2:
                    ca = a2
                elif int(ca) == 3:
                    ca = a3
                elif int(ca) == 4:
                    ca = a4
                print("\nWrong! The correct answer was "+str(ca))
                displayWorR(screen, 'w', tiletype)
                player.setPlayerPoints(-30)

        elif tiletype == 'q2':
            length = (len(qp2) - 1)
            q = random.randint(0, length)
            q = qp2[q]
            question = q[0]
            a1 = q[1]
            a2 = q[2]
            a3 = q[3]
            a4 = q[4]
            ca = q[5]
            preQDisplay(screen, tiletype, question, a1, a2, a3, a4)
            myans = getAns(screen, tiletype, ABCDbutton_sprites, ABCDbuttonList)
            if myans == int(ca):
                print("\nCorrect!")
                displayWorR(screen, 'r', tiletype)
                player.setPlayerPoints(30)
            else:
                if int(ca) == 1:
                    ca = a1
                elif int(ca) == 2:
                    ca = a2
                elif int(ca) == 3:
                    ca = a3
                elif int(ca) == 4:
                    ca = a4
                print("\nWrong! The correct answer was "+str(ca))
                displayWorR(screen, 'w', tiletype)
                player.setPlayerPoints(-30)

        elif tiletype == 'q3':
            length = (len(qp3) - 1)
            q = random.randint(0, length)
            q = qp3[q]
            question = q[0]
            a1 = q[1]
            a2 = q[2]
            a3 = q[3]
            a4 = q[4]
            ca = q[5]
            preQDisplay(screen, tiletype, question, a1, a2, a3, a4)
            myans = getAns(screen, tiletype, ABCDbutton_sprites, ABCDbuttonList)
            if myans == int(ca):
                print("\nCorrect!")
                displayWorR(screen, 'r', tiletype)
                player.setPlayerPoints(40)
            else:
                if int(ca) == 1:
                    ca = a1
                elif int(ca) == 2:
                    ca = a2
                elif int(ca) == 3:
                    ca = a3
                elif int(ca) == 4:
                    ca = a4
                print("\nWrong! The correct answer was "+str(ca))
                displayWorR(screen, 'w', tiletype)
                player.setPlayerPoints(-30)

        elif tiletype == 'c':
            length = (len(yesGo)) - 1
            place = random.randint(0,length)
            destination = yesGo[place]
            x,y = destination[0],destination[1]
            player.setxCoord(x)
            player.setyCoord(y)
            if player.getPlayerNum() == 1:
                pos = (mymap[y][x]).getTopLeft()
                player.teleport(pos)
            elif player.getPlayerNum() == 2:
                pos = (mymap[y][x]).getTopRight()
                player.teleport(pos)
            elif player.getPlayerNum() == 3:
                pos = (mymap[y][x]).getBottomLeft()
                player.teleport(pos)
            elif player.getPlayerNum() == 4:
                pos = (mymap[y][x]).getBottomRight()
                player.teleport(pos)

            font = pg.font.Font(None, 64)
            TEXT_COLOUR = (40,40,40)
            COLOUR = (255,242,0)
            screen.fill(COLOUR)
            Txt = font.render("TELEPORTING", True, TEXT_COLOUR, None)
            Txtrect = Txt.get_rect()
            Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
            screen.blit(Txt, Txtrect)
            pg.display.flip()
            time.sleep(1)

        elif tiletype == 'st':
            player.setPlayerPoints(10)

        elif tiletype == 'sa':
            pass

        elif tiletype == 'end':
            cont = endornot(screen, YNbutton_sprites, YNbuttonList)
            if cont == False:
                player.setFinished()
            else:
                pass
            
def preQDisplay(screen, dif, question, a1, a2, a3, a4):
    font = pg.font.Font(None, 64)
    EASY = (91,173,37)
    MED = (252,168,41)
    HARD = (206,16,26)
    COLOUR = (170,170,170)
    TEXT_COLOUR = (255,255,255)

    if dif == 'q1':
        difTxt = "Difficulty: Easy"
        pointTxt = "Worth 20 Points"
        screen.fill(EASY)
        difandpointTxt(screen, difTxt, pointTxt, font, TEXT_COLOUR)
        pg.display.flip()
        time.sleep(1)
        screen.fill(EASY)
    elif dif == 'q2':
        difTxt = "Difficulty: Medium"
        pointTxt = "Worth 30 Points"
        screen.fill(MED)
        difandpointTxt(screen, difTxt, pointTxt, font, TEXT_COLOUR)
        pg.display.flip()
        time.sleep(1)
        screen.fill(MED)
    elif dif == 'q3':
        difTxt = "Difficulty: Hard"
        pointTxt = "Worth 40 Points"
        screen.fill(HARD)
        difandpointTxt(screen, difTxt, pointTxt, font, TEXT_COLOUR)
        pg.display.flip()
        time.sleep(0.5)
        screen.fill(HARD)
    displayQ(screen, question, a1, a2, a3, a4, TEXT_COLOUR)

def difandpointTxt(screen, difTxt, pointTxt, font, TEXT_COLOUR):
    quarter = ((screen.get_rect().centery)/4)-20
    
    difficultyTxt = font.render(difTxt, True, TEXT_COLOUR, None)
    difficultyTxtrect = difficultyTxt.get_rect()
    difficultyTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-quarter))
    screen.blit(difficultyTxt, difficultyTxtrect)

    pointTxt = font.render(pointTxt, True, TEXT_COLOUR, None)
    pointTxtrect = pointTxt.get_rect()
    pointTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+quarter))
    screen.blit(pointTxt, pointTxtrect)

def displayQ(screen, question, a1, a2, a3, a4, TEXT_COLOUR):
    font1 = pg.font.Font(None, 55)
    font2 = pg.font.Font(None, 50)
    quarter = (screen.get_rect().centery)/4
    
    Question = font1.render(question, True, TEXT_COLOUR, None)
    Questionrect = Question.get_rect()
    Questionrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-quarter))
    screen.blit(Question, Questionrect)

    A1 = font2.render(("A) "+ a1), True, TEXT_COLOUR, None)
    A1rect = A1.get_rect()
    A1rect.center = ((screen.get_rect().centerx),(screen.get_rect().centery))
    screen.blit(A1, A1rect)

    A2 = font2.render(("B) "+ a2), True, TEXT_COLOUR, None)
    A2rect = A2.get_rect()
    A2rect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+40))
    screen.blit(A2, A2rect)

    A3 = font2.render(("C) "+ a3), True, TEXT_COLOUR, None)
    A3rect = A3.get_rect()
    A3rect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+80))
    screen.blit(A3, A3rect)

    A4 = font2.render(("D) "+ a4), True, TEXT_COLOUR, None)
    A4rect = A4.get_rect()
    A4rect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+120))
    screen.blit(A4, A4rect)

    pg.display.flip()
    time.sleep(3)

def displayWorR(screen, WorR, dif):
    BG_COLOUR = (255,255,255)
    TEXT_COLOUR1 = (91,173,37)
    TEXT_COLOUR2 = (206,16,26)
    font = pg.font.Font(None, 64)

    screen.fill(BG_COLOUR)

    if WorR == 'r':
        if dif == 'q1':
            WorRTxt = font.render("Correct!", True, TEXT_COLOUR1, None)
            pointTxt = font.render("+20 Points", True, TEXT_COLOUR1, None)
        elif dif == 'q2':
            WorRTxt = font.render("Correct!", True, TEXT_COLOUR1, None)
            pointTxt = font.render("+30 Points", True, TEXT_COLOUR1, None)
        elif dif == 'q3':
            WorRTxt = font.render("Correct!", True, TEXT_COLOUR1, None)
            pointTxt = font.render("+40 Points", True, TEXT_COLOUR1, None)

    elif WorR == 'w':
        WorRTxt = font.render("Wrong!", True, TEXT_COLOUR2, None)
        pointTxt = font.render("-30 Points", True, TEXT_COLOUR2, None)

    WorRTxtrect = WorRTxt.get_rect()
    WorRTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-30))
    screen.blit(WorRTxt, WorRTxtrect)

    pointTxtrect = pointTxt.get_rect()
    pointTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(pointTxt, pointTxtrect)

    pg.display.flip()
    time.sleep(1)

def getAns(screen, dif, ABCDbutton_sprites, ABCDbuttonList):
    startTime = 1500
    time = 6
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                done = False
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_a):
                    returning = 1
                    done = True
                elif (event.key==pg.K_b):
                    returning = 2
                    done = True
                elif (event.key==pg.K_c):
                    returning = 3
                    done = True
                elif (event.key==pg.K_d):
                    returning = 4
                    done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if ABCDbuttonList[0].getPressed(mousepos) == True and pressed1:
                returning = 1
                done = True
            elif ABCDbuttonList[1].getPressed(mousepos) == True and pressed1:
                returning = 2
                done = True
            elif ABCDbuttonList[2].getPressed(mousepos) == True and pressed1:
                returning = 3
                done = True
            elif ABCDbuttonList[3].getPressed(mousepos) == True and pressed1:
                returning = 4
                done = True
        if startTime == 0:
            returning = 5
            done = True
        if startTime % 300 == 0:
            time = time - 1
        startTime = startTime - 1
        updateQtimer(screen, time, dif, ABCDbutton_sprites)
    return returning

def updateQtimer(screen, time, dif, ABCDbutton_sprites):
    TEXT_COLOUR = (255,255,255)
    EASY = (91,173,37)
    MED = (252,168,41)
    HARD = (206,16,26)
    font = pg.font.Font(None, 64)

    if dif == 'q1':
        screen.fill(EASY)
    elif dif == 'q2':
        screen.fill(MED)
    elif dif == 'q3':
        screen.fill(HARD)

    timeTxt = font.render((str(time)), True, TEXT_COLOUR, None)
    timeTxtrect = timeTxt.get_rect()
    timeTxtrect.center = ((screen.get_rect().centerx),(screen.get_rect().centery))
    screen.blit(timeTxt, timeTxtrect)

    ABCDbutton_sprites.draw(screen)

    pg.display.flip()

def endornot(screen, YNbutton_sprites, YNbuttonList):
    font = pg.font.Font(None, 64)
    TEXT_COLOUR = (40,40,40)
    COLOUR = (239,228,176)
    screen.fill(COLOUR)
    Txt = font.render("Do You Want To Continue?", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    YNbutton_sprites.draw(screen)
    pg.display.flip()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                done = False
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_n):
                    returning = False
                    done = True
                elif (event.key==pg.K_y):
                    returning = True
                    done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if YNbuttonList[0].getPressed(mousepos) == True and pressed1:
                returning = True
                done = True
            elif YNbuttonList[1].getPressed(mousepos) == True and pressed1:
                returning = False
                done = True
    return returning
