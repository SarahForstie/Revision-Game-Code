#Imports
import pygame as pg
import random
import counters
import time
import playSounds

#Global variables
global TEXT
TEXT = 'saxmono.ttf'

def getTileEffect(mymap, player, xcoord, ycoord, qp1, qp2, qp3, screen, ABCDbutton_sprites, YNbutton_sprites, ABCDbuttonList, YNbuttonList, yesGo, jailtile, counterList):#Decides which effect happens to the player
    if player == 0:
        pass
    elif int(player.getFinished()) == 1:#No effect if the player is finished
        pass
    else:
        currenttile = mymap[ycoord][xcoord]#Gets the tile that the player is on
        tiletype = str(currenttile.getType())#Gets the tile type
        
        if tiletype == 'q1':#Gives an easy question
            if player.getSkipQuestion() > 0:#Asks whether the player would like to skip the question
                useSQ = useSkipQuestion(screen, YNbutton_sprites, YNbuttonList, player)
            else:
                useSQ = False
            if useSQ == False:#If skip question not used
                points = 20
                if player.getDoublePoints() > 0:#Asks whether the player would like to double their points
                    double = useDoublePointsText(screen, YNbutton_sprites, YNbuttonList, player)
                    points = points * double
                else:
                    pass
                length = (len(qp1) - 1)
                q = random.randint(0, length)
                q = qp1[q]
                question = q[0]#Question
                a1 = q[1]#Answer 1
                a2 = q[2]#Answer 2
                a3 = q[3]#Answer 3
                a4 = q[4]#Answer 4
                ca = q[5]#Correct answer
                preQDisplay(screen, tiletype, question, a1, a2, a3, a4)
                myans = getAns(screen, tiletype, ABCDbutton_sprites, ABCDbuttonList)
                if myans == int(ca):
                    displayWorR(screen, 'r', tiletype)
                    player.setPlayerPoints(points)#Awards points for correct answer
                else:
                    if int(ca) == 1:
                        ca = a1
                    elif int(ca) == 2:
                        ca = a2
                    elif int(ca) == 3:
                        ca = a3
                    elif int(ca) == 4:
                        ca = a4
                    displayWorR(screen, 'w', tiletype)
                    player.setPlayerPoints(-30)#Take away points if wrong answer
            else:
                player.setPlayerPoints(20)

        elif tiletype == 'q2':#Gives a medium question
            if player.getSkipQuestion() > 0:#Asks whether the player would like to skip the question
                useSQ = useSkipQuestion(screen, YNbutton_sprites, YNbuttonList, player)
            else:
                useSQ = False
            if useSQ == False:#If skip question not used
                points = 30
                if player.getDoublePoints() > 0:#Asks whether the player would like to double their points
                    double = useDoublePointsText(screen, YNbutton_sprites, YNbuttonList, player)
                    points = points * double
                else:
                    pass
                length = (len(qp2) - 1)
                q = random.randint(0, length)
                q = qp2[q]
                question = q[0]#Question
                a1 = q[1]#Answer 1
                a2 = q[2]#Answer 2
                a3 = q[3]#Answer 3
                a4 = q[4]#Answer 4
                ca = q[5]#Correct answer
                preQDisplay(screen, tiletype, question, a1, a2, a3, a4)
                myans = getAns(screen, tiletype, ABCDbutton_sprites, ABCDbuttonList)
                if myans == int(ca):
                    displayWorR(screen, 'r', tiletype)
                    player.setPlayerPoints(points)#Awards points for correct answer
                else:
                    if int(ca) == 1:
                        ca = a1
                    elif int(ca) == 2:
                        ca = a2
                    elif int(ca) == 3:
                        ca = a3
                    elif int(ca) == 4:
                        ca = a4
                    displayWorR(screen, 'w', tiletype)
                    player.setPlayerPoints(-30)#Take away points if wrong answer
            else:
                player.setPlayerPoints(30)

        elif tiletype == 'q3':#Gives a hard question
            if player.getSkipQuestion() > 0:#Asks whether the player would like to skip the question
                useSQ = useSkipQuestion(screen, YNbutton_sprites, YNbuttonList, player)
            else:
                useSQ = False
            if useSQ == False:#If skip question not used
                points = 40
                if player.getDoublePoints() > 0:#Asks whether the player would like to double their points
                    double = useDoublePointsText(screen, YNbutton_sprites, YNbuttonList, player)
                    points = points * double
                else:
                    pass
                length = (len(qp3) - 1)
                q = random.randint(0, length)
                q = qp3[q]
                question = q[0]#Question
                a1 = q[1]#Answer 1
                a2 = q[2]#Answer 2
                a3 = q[3]#Answer 3
                a4 = q[4]#Answer 4
                ca = q[5]#Correct answer
                preQDisplay(screen, tiletype, question, a1, a2, a3, a4)
                myans = getAns(screen, tiletype, ABCDbutton_sprites, ABCDbuttonList)
                if myans == int(ca):
                    displayWorR(screen, 'r', tiletype)
                    player.setPlayerPoints(points)#Awards points for correct answer
                else:
                    if int(ca) == 1:
                        ca = a1
                    elif int(ca) == 2:
                        ca = a2
                    elif int(ca) == 3:
                        ca = a3
                    elif int(ca) == 4:
                        ca = a4
                    displayWorR(screen, 'w', tiletype)
                    player.setPlayerPoints(-30)#Take away points if wrong answer
            else:
                player.setPlayerPoints(40)

        elif tiletype == 'c':#Gives a random chance
            choice = random.randint(1,13)#Makes the choice random
            if choice == 1 or choice == 2:#Teleports the player
                chanceTeleport(yesGo, player, mymap, screen)
            elif choice == 3 or choice == 4:#Exchanges points
                chanceCoinExchangeGood(player, screen, counterList)
            elif choice == 5 or choice == 6:#Exchanges points
                chanceCoinExchangeBad(player, screen, counterList)
            elif choice == 7:#Gives get out of jail free item
                chanceGiveGetOutOfJail(player, screen)
            elif choice == 8:#Gives skip question item
                chanceGiveSkipQuestion(player, screen)
            elif choice == 9:#Gives double points item
                chanceGiveDoublePoints(player, screen)
            elif choice == 10 or choice == 11:#Gives the player points
                chanceFindPoints(player, screen)
            elif choice == 12 or choice == 13:#Takes points from the player
                chanceLosePoints(player, screen)

        elif tiletype == 'st':#Gives the player 10 points
            player.setPlayerPoints(10)

        elif tiletype == 'sa':#Doesn't do anything
            pass

        elif tiletype == 'end':#Gives the player an option to finish
            cont = endornot(screen, YNbutton_sprites, YNbuttonList)
            if cont == False:
                player.setFinished()
            else:
                pass

        elif tiletype == 'gtj':#Sends the player to jail
            playSounds.goToJailSound()
            goToJailText(screen)
            if player.getGetOutOfJail() > 0:#Uses a get out of jail item
                player.setGetOutOfJail(-1)
                useGetOutOfJailText(screen)
            else:
                goToJail(player, mymap, jailtile)

        elif tiletype == 'j':#Doesn't do anything
            playSounds.jailSound()

def preQDisplay(screen, dif, question, a1, a2, a3, a4):#Displays the difficulty and reward
    #Defines the text look
    global TEXT
    font = pg.font.Font(TEXT, 64)
    EASY = (91,173,37)
    MED = (252,168,41)
    HARD = (206,16,26)
    COLOUR = (170,170,170)
    TEXT_COLOUR = (255,255,255)

    #Displays the text
    if dif == 'q1':
        difTxt = "Difficulty: Easy"
        pointTxt = "Worth 20 Points"
        screen.fill(EASY)
        difandpointTxt(screen, difTxt, pointTxt, font, TEXT_COLOUR)#Displays the text
        pg.display.flip()#Displays screen
        time.sleep(1)
        screen.fill(EASY)
    elif dif == 'q2':
        difTxt = "Difficulty: Medium"
        pointTxt = "Worth 30 Points"
        screen.fill(MED)
        difandpointTxt(screen, difTxt, pointTxt, font, TEXT_COLOUR)#Displays the text
        pg.display.flip()#Displays screen
        time.sleep(1)
        screen.fill(MED)
    elif dif == 'q3':
        difTxt = "Difficulty: Hard"
        pointTxt = "Worth 40 Points"
        screen.fill(HARD)
        difandpointTxt(screen, difTxt, pointTxt, font, TEXT_COLOUR)#Displays the text
        pg.display.flip()#Displays screen
        time.sleep(0.5)
        screen.fill(HARD)
    displayQ(screen, question, a1, a2, a3, a4, TEXT_COLOUR)#Displays the question

def difandpointTxt(screen, difTxt, pointTxt, font, TEXT_COLOUR):#Displays the difficulty text
    quarter = ((screen.get_rect().centery)/4)-20#A value for positioning
    
    difficultyTxt = font.render(difTxt, True, TEXT_COLOUR, None)
    difficultyTxtrect = difficultyTxt.get_rect()
    difficultyTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-quarter))
    screen.blit(difficultyTxt, difficultyTxtrect)#Displays the difficulty

    pointTxt = font.render(pointTxt, True, TEXT_COLOUR, None)
    pointTxtrect = pointTxt.get_rect()
    pointTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+quarter))
    screen.blit(pointTxt, pointTxtrect)#Displays the amount of points

def displayQ(screen, question, a1, a2, a3, a4, TEXT_COLOUR):#Displays the question
    #Defines the text look
    global TEXT
    fontsize1, fontsize2 = findFontsize(a1, a2, a3, a4, question, screen)#Scales the text size
    font1 = pg.font.Font(TEXT, fontsize1)
    font2 = pg.font.Font(TEXT, fontsize2)
    quarter = (screen.get_rect().centery)/4#A value for positioning
    
    #Displays the text
    Question = font1.render(question, True, TEXT_COLOUR, None)
    Questionrect = Question.get_rect()
    Questionrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-quarter))
    screen.blit(Question, Questionrect)

    A1 = font2.render(("A) "+ a1), True, TEXT_COLOUR, None)
    A1rect = A1.get_rect()
    A1rect.center = ((screen.get_rect().centerx),(screen.get_rect().centery))
    screen.blit(A1, A1rect)#Displays answer 1

    A2 = font2.render(("B) "+ a2), True, TEXT_COLOUR, None)
    A2rect = A2.get_rect()
    A2rect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+60))
    screen.blit(A2, A2rect)#Displays answer 2

    A3 = font2.render(("C) "+ a3), True, TEXT_COLOUR, None)
    A3rect = A3.get_rect()
    A3rect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+120))
    screen.blit(A3, A3rect)#Displays answer 3

    A4 = font2.render(("D) "+ a4), True, TEXT_COLOUR, None)
    A4rect = A4.get_rect()
    A4rect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+180))
    screen.blit(A4, A4rect)#Displays answer 4

    pg.display.flip()#Displays screen
    time.sleep(3)

def displayWorR(screen, WorR, dif):#Displays whether the player answered the question wrong or right
    #Defines the text look
    global TEXT
    BG_COLOUR = (255,255,255)
    TEXT_COLOUR1 = (91,173,37)
    TEXT_COLOUR2 = (206,16,26)
    font = pg.font.Font(TEXT, 64)

    #Displays the text
    screen.fill(BG_COLOUR)

    if WorR == 'r':#Sets the correct text
        if dif == 'q1':#Sets the correct text for easy questions
            WorRTxt = font.render("Correct!", True, TEXT_COLOUR1, None)
            pointTxt = font.render("+20 Points", True, TEXT_COLOUR1, None)
            correct = 'y'
        elif dif == 'q2':#Sets the correct text for medium questions
            WorRTxt = font.render("Correct!", True, TEXT_COLOUR1, None)
            pointTxt = font.render("+30 Points", True, TEXT_COLOUR1, None)
            correct = 'y'
        elif dif == 'q3':#Sets the correct text for hard questions
            WorRTxt = font.render("Correct!", True, TEXT_COLOUR1, None)
            pointTxt = font.render("+40 Points", True, TEXT_COLOUR1, None)
            correct = 'y'

    elif WorR == 'w':#Sets the wrong text
        WorRTxt = font.render("Wrong!", True, TEXT_COLOUR2, None)
        pointTxt = font.render("-30 Points", True, TEXT_COLOUR2, None)
        correct = 'n'

    WorRTxtrect = WorRTxt.get_rect()
    WorRTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-30))
    screen.blit(WorRTxt, WorRTxtrect)

    pointTxtrect = pointTxt.get_rect()
    pointTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(pointTxt, pointTxtrect)

    pg.display.flip()#Displays screen
    playSounds.correctOrWrongSound(correct)
    time.sleep(1)

def getAns(screen, dif, ABCDbutton_sprites, ABCDbuttonList):#Get the answer of the player
    startTime = 2100#Time limit
    time = 8#Time shown to the player
    done = False
    while not done:#Loop that quits when a answer is given or time runs out
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = False
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_a):#Given answer is 1
                    returning = 1
                    done = True
                elif (event.key==pg.K_b):#Given answer is 2
                    returning = 2
                    done = True
                elif (event.key==pg.K_c):#Given answer is 3
                    returning = 3
                    done = True
                elif (event.key==pg.K_d):#Given answer is 4
                    returning = 4
                    done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if ABCDbuttonList[0].getPressed(mousepos) == True and pressed1:#Given answer is 1
                returning = 1
                done = True
            elif ABCDbuttonList[1].getPressed(mousepos) == True and pressed1:#Given answer is 2
                returning = 2
                done = True
            elif ABCDbuttonList[2].getPressed(mousepos) == True and pressed1:#Given answer is 3
                returning = 3
                done = True
            elif ABCDbuttonList[3].getPressed(mousepos) == True and pressed1:#Given answer is 4
                returning = 4
                done = True
        if startTime == 0:#Time has run out
            returning = 5#Given answer is 5, which is always wrong
            done = True
        if startTime % 300 == 0:#Decrease counter
            time = time - 1
        startTime = startTime - 1
        updateQtimer(screen, time, dif, ABCDbutton_sprites)#Displays the current counter
    return returning

def updateQtimer(screen, time, dif, ABCDbutton_sprites):#Displays the current counter
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (255,255,255)
    EASY = (91,173,37)
    MED = (252,168,41)
    HARD = (206,16,26)
    font = pg.font.Font(TEXT, 64)

    #Displays the text
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

    ABCDbutton_sprites.draw(screen)#Draws the buttons

    pg.display.flip()#Displays screen

def endornot(screen, YNbutton_sprites, YNbuttonList):
    #Defines the text look
    global TEXT
    font = pg.font.Font(TEXT, 64)
    TEXT_COLOUR = (255,255,255)
    COLOUR = (0,162,232)

    #Displays the text
    screen.fill(COLOUR)
    Txt = font.render("Do You Want To Continue?", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    YNbutton_sprites.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#Loop that quits when a answer is given
        for event in pg.event.get():
            if event.type == pg.QUIT:#Exits the game
                pg.quit()
                done = False
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_n):#Player finishes
                    returning = False
                    done = True
                elif (event.key==pg.K_y):#Player doesn't finish
                    returning = True
                    done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if YNbuttonList[0].getPressed(mousepos) == True and pressed1:#Player doesn't finish
                returning = True
                done = True
            elif YNbuttonList[1].getPressed(mousepos) == True and pressed1:#Player finishes
                returning = False
                done = True
    return returning

def chanceTeleport(yesGo, player, mymap, screen):#Teleports the player to a random space on the board
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (213,165,0)
    COLOUR = (255,242,0)
    font = pg.font.Font(TEXT, 64)
    
    length = (len(yesGo)) - 1
    place = random.randint(0,length)
    destination = yesGo[place]#A random place is chosenn
    newx,newy = destination[0],destination[1]
    if player.getPlayerNum() == 1:#Teleports player 1 to the top left of the random tile
        pos = (mymap[newy][newx]).getTopLeft()
        player.teleport(pos, newy, newx)
    elif player.getPlayerNum() == 2:#Teleports player 2 to the top right of the random tile
        pos = (mymap[newy][newx]).getTopRight()
        player.teleport(pos, newy, newx)
    elif player.getPlayerNum() == 3:#Teleports player 3 to the bottom left of the random tile
        pos = (mymap[newy][newx]).getBottomLeft()
        player.teleport(pos, newy, newx)
    elif player.getPlayerNum() == 4:#Teleports player 4 to the bottom right of the random tile
        pos = (mymap[newy][newx]).getBottomRight()
        player.teleport(pos, newy, newx)

    #Displays the text
    screen.fill(COLOUR)
    Txt = font.render("TELEPORTING", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    pg.display.flip()#Displays screen
    playSounds.teleportSound()
    time.sleep(2.5)

def chanceCoinExchangeGood(player, screen, counterList):#Gives the current player points and takes points from another
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (213,165,0)
    COLOUR = (255,242,0)
    font = pg.font.Font(TEXT, 55)
    font2 = pg.font.Font(TEXT, 32)
    
    points = random.randint(1,40)#Chooses how many points are exchanged
    done = False
    while not done:#Decides which other player is effected
        otherPlayer = counterList[random.randint(0,(len(counterList) - 1))]
        if otherPlayer.getPlayerNum() != player.getPlayerNum():
            done = True
            
    #Displays the text
    screen.fill(COLOUR)
    myText = "Player " + str(otherPlayer.getPlayerNum()) + " Owes You Points"
    Txt = font.render(myText, True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
    screen.blit(Txt, Txtrect)
    myText = "Player " + str(otherPlayer.getPlayerNum()) + " -" + str(points)
    subTxt = font2.render(myText, True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    myText = "Player " + str(player.getPlayerNum()) + " +" + str(points)
    subTxt2 = font2.render(myText, True, TEXT_COLOUR, None)
    subTxt2rect = subTxt2.get_rect()
    subTxt2rect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+70))
    screen.blit(subTxt2, subTxt2rect)
    playSounds.coinExchangeSound()
    pg.display.flip()#Displays screen
    player.setPlayerPoints(points)#Player has points added
    otherPlayer.setPlayerPoints((points * -1))#Other player has points taken away
    time.sleep(2.5)

def chanceCoinExchangeBad(player, screen, counterList):#Takes the current player points and gives the points to another
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (213,165,0)
    COLOUR = (255,242,0)
    font = pg.font.Font(TEXT, 55)
    font2 = pg.font.Font(TEXT, 32)
    
    points = random.randint(1,40)#Chooses how many points are exchanged
    done = False
    while not done:#Decides which other player is effected
        otherPlayer = counterList[random.randint(0,(len(counterList) - 1))]
        if otherPlayer.getPlayerNum() != player.getPlayerNum():
            done = True

    #Displays the text
    screen.fill(COLOUR)
    myText = "You Owe Player " + str(otherPlayer.getPlayerNum()) + " Points"
    Txt = font.render(myText, True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
    screen.blit(Txt, Txtrect)
    myText = "Player " + str(otherPlayer.getPlayerNum()) + " +" + str(points)
    subTxt = font2.render(myText, True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    myText = "Player " + str(player.getPlayerNum()) + " -" + str(points)
    subTxt2 = font2.render(myText, True, TEXT_COLOUR, None)
    subTxt2rect = subTxt2.get_rect()
    subTxt2rect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+70))
    screen.blit(subTxt2, subTxt2rect)
    playSounds.coinExchangeSound()
    pg.display.flip()#Displays screen
    player.setPlayerPoints((points * -1))#Player has points taken away
    otherPlayer.setPlayerPoints(points)#Other player has points added
    time.sleep(2.5)

def chanceGiveGetOutOfJail(player, screen):#Gives the player a get out of jail free item
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (34,177,76)
    COLOUR = (61,218,107)
    font = pg.font.Font(TEXT, 55)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    screen.fill(COLOUR)
    Txt = font.render("Item Obtained", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
    screen.blit(Txt, Txtrect)
    subTxt = font2.render("You Got a Get Out Of Jail Free Item", True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    player.setGetOutOfJail(1)#Adds a get out of jail free item to the player
    time.sleep(2.5)

def chanceGiveSkipQuestion(player, screen):#Gives the player a skip question item
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (96,43,96)
    COLOUR = (163,73,164)
    font = pg.font.Font(TEXT, 55)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    screen.fill(COLOUR)
    Txt = font.render("Item Obtained", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
    screen.blit(Txt, Txtrect)
    subTxt = font2.render("You Got a Skip Question Item", True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    player.setSkipQuestion(1)#Adds a skip question item to the player
    time.sleep(2.5)

def chanceGiveDoublePoints(player, screen):#Gives the player a double points item
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (255,108,156)
    COLOUR = (255,174,201)
    font = pg.font.Font(TEXT, 55)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    screen.fill(COLOUR)
    Txt = font.render("Item Obtained", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
    screen.blit(Txt, Txtrect)
    subTxt = font2.render("You Got a Double Points Item", True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    player.setDoublePoints(1)#Adds a double points item to the player
    time.sleep(2.5)

def chanceFindPoints(player, screen):#Gives the player points
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (213,165,0)
    COLOUR = (255,242,0)
    font = pg.font.Font(TEXT, 55)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    points = random.randint(1,40)#Chooses how many points are gained
    screen.fill(COLOUR)
    mytext = str(points) + " Points Found"
    Txt = font.render(mytext, True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
    screen.blit(Txt, Txtrect)
    mytext = "Player " + str(player.getPlayerNum()) + " +" + str(points)
    subTxt = font2.render(mytext, True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    player.setPlayerPoints(points)#Gives the player points
    playSounds.coinExchangeSound()
    time.sleep(2.5)

def chanceLosePoints(player, screen):
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (213,165,0)
    COLOUR = (255,242,0)
    font = pg.font.Font(TEXT, 55)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    points = random.randint(1,40)#Chooses how many points are lost
    screen.fill(COLOUR)
    mytext = str(points) + " Points Lost"
    Txt = font.render(mytext, True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-25))
    screen.blit(Txt, Txtrect)
    mytext = "Player " + str(player.getPlayerNum()) + " -" + str(points)
    subTxt = font2.render(mytext, True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    player.setPlayerPoints((points * -1))#Take the player's points
    playSounds.coinExchangeSound()
    time.sleep(2.5)

def findFontsize(a1, a2, a3, a4, question, screen):#Scales the text size
    global TEXT
    screen_width, screen_height = screen.get_width(), screen.get_height()
    fontsize1 = 64
    font1 = pg.font.Font(TEXT, fontsize1)
    text_width, text_height = font1.size(question)
    while text_width > screen_width:#Reduces the text size until it fits the screen
        fontsize1 = fontsize1 - 1
        font1 = pg.font.Font(TEXT, fontsize1)
        text_width, text_height = font1.size(question)
    longestAnswer = a1#Finds the longest answer so that all answers fit on screen
    if len(a2) > len(longestAnswer):
        longestAnswer = a2
    if len(a3) > len(longestAnswer):
        longestAnswer = a3
    if len(a2) > len(longestAnswer):
        longestAnswer = a4
    fontsize2 = 44
    font2 = pg.font.Font(TEXT, fontsize2)
    text_width, text_height = font2.size(("A) " + longestAnswer))
    while text_width > screen_width:#Reduces the text size until it fits the screen
        fontsize2 = fontsize2 - 1
        font2 = pg.font.Font(TEXT, fontsize2)
        text_width, text_height = font2.size(question)

    return int(fontsize1), int(fontsize2)#Returns integer values

def goToJail(player, mymap, jailtile):#Sends the player to the jail tile
    if player.getPlayerNum() == 1:#Teleports player 1 to the top left of the jail tile
        pos = (mymap[jailtile[0]][jailtile[1]]).getTopLeft()
        newx = jailtile[1]
        newy = jailtile[0]
        player.teleport(pos, newy, newx)
        player.setInJail(3)#The player is set as in jail
        
    elif player.getPlayerNum() == 2:#Teleports player 2 to the top right of the jail tile
        pos = (mymap[jailtile[0]][jailtile[1]]).getTopRight()
        newx = jailtile[1]
        newy = jailtile[0]
        player.teleport(pos, newy, newx)
        player.setInJail(3)#The player is set as in jail
        
    elif player.getPlayerNum() == 3:#Teleports player 3 to the bottom left of the jail tile
        pos = (mymap[jailtile[0]][jailtile[1]]).getBottomLeft()
        newx = jailtile[1]
        newy = jailtile[0]
        player.teleport(pos, newy, newx)
        player.setInJail(3)#The player is set as in jail
        
    elif player.getPlayerNum() == 4:#Teleports player 4 to the bottom right of the jail tile
        pos = (mymap[jailtile[0]][jailtile[1]]).getBottomRight()
        newx = jailtile[1]
        newy = jailtile[0]
        player.teleport(pos, newy, newx)
        player.setInJail(3)#The player is set as in jail

def goToJailText(screen):#Displays the go to jail text
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (157,157,157)
    COLOUR = (111,111,111)
    font1 = pg.font.Font(TEXT, 64)
    font2 = pg.font.Font(TEXT, 32)

    #Displays the text
    screen.fill(COLOUR)
    Txt = font1.render("You Are Accused of Theft", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    subTxt = font2.render("Go To Jail", True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    time.sleep(2)

def useGetOutOfJailText(screen):#Displays the use of a go to jail item
    #Defines the text look
    global TEXT
    TEXT_COLOUR = (34,177,76)
    COLOUR = (61,218,107)
    font1 = pg.font.Font(TEXT, 64)
    font2 = pg.font.Font(TEXT, 32)
    
    #Displays the text
    screen.fill(COLOUR)
    Txt = font1.render("You Won the Case Against You", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    subTxt = font2.render("-1 Get Out Of Jail Free Item", True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    time.sleep(2)

def useDoublePointsText(screen, YNbutton_sprites, YNbuttonList, player):#Gives the option of using a double points item
    #Defines the text look
    global TEXT
    font = pg.font.Font(TEXT, 60)
    TEXT_COLOUR = (255,108,156)
    COLOUR = (255,174,201)

    #Displays the text
    screen.fill(COLOUR)
    Txt = font.render("Do You Want To Use a Double Points Item?", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    YNbutton_sprites.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#Loops until an answer is given
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                done = False
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_n):#Double point item isn't used
                    returning = 1
                    done = True
                elif (event.key==pg.K_y):#Double point item is used
                    returning = 2
                    usedDoublePoints(screen, player)
                    done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if YNbuttonList[0].getPressed(mousepos) == True and pressed1:#Double point item is used
                returning = 2
                usedDoublePoints(screen, player)
                done = True
            elif YNbuttonList[1].getPressed(mousepos) == True and pressed1:#Double point item isn't used
                returning = 1
                done = True
    return returning

def usedDoublePoints(screen, player):#Displays the use of a double points item
    #Defines the text look
    global TEXT
    font = pg.font.Font(TEXT, 60)
    TEXT_COLOUR = (255,108,156)
    COLOUR = (255,174,201)

    #Displays the text
    player.setDoublePoints(-1)
    screen.fill(COLOUR)
    font1 = pg.font.Font(TEXT, 64)
    font2 = pg.font.Font(TEXT, 32)
    Txt = font1.render("Double Points Item Used", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    subTxt = font2.render("-1 Double Points Item", True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    time.sleep(2)

def useSkipQuestion(screen, YNbutton_sprites, YNbuttonList, player):#Gives the option of using a skip question item
    #Defines the text look
    global TEXT
    font = pg.font.Font(TEXT, 60)
    TEXT_COLOUR = (96,43,96)
    COLOUR = (163,73,164)

    #Displays the text
    screen.fill(COLOUR)
    Txt = font.render("Do You Want To Use a Skip Question Item?", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    YNbutton_sprites.draw(screen)
    pg.display.flip()#Displays screen
    done = False
    while not done:#Loops until an answer is given
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                done = False
            if (event.type == pg.KEYDOWN):
                if (event.key==pg.K_n):#Skip question item isn't used
                    returning = False
                    done = True
                elif (event.key==pg.K_y):#Skip question item is used
                    returning = True
                    usedSkipQuestion(screen, player)
                    done = True
            mousepos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()
            if YNbuttonList[0].getPressed(mousepos) == True and pressed1:#Skip question item is used
                returning = True
                usedSkipQuestion(screen, player)
                done = True
            elif YNbuttonList[1].getPressed(mousepos) == True and pressed1:#Skip question item isn't used
                returning = False
                done = True
    return returning

def usedSkipQuestion(screen, player):#Displays the use of a skip question item
    #Defines the text look
    global TEXT
    font = pg.font.Font(TEXT, 60)
    TEXT_COLOUR = (96,43,96)
    COLOUR = (163,73,164)

    #Displays the text
    player.setSkipQuestion(-1)
    screen.fill(COLOUR)
    font1 = pg.font.Font(TEXT, 64)
    font2 = pg.font.Font(TEXT, 32)
    Txt = font1.render("Skip Question Item Used", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)-20))
    screen.blit(Txt, Txtrect)
    subTxt = font2.render("-1 Skip Question Item", True, TEXT_COLOUR, None)
    subTxtrect = subTxt.get_rect()
    subTxtrect.center = ((screen.get_rect().centerx),((screen.get_rect().centery)+30))
    screen.blit(subTxt, subTxtrect)
    pg.display.flip()#Displays screen
    time.sleep(2)

def timeUp(screen):#Displays when the time is up
    #Defines the text look
    global TEXT
    font = pg.font.Font(TEXT, 60)
    TEXT_COLOUR = (255,255,255)
    COLOUR = (20,2,92)

    #Displays the text
    screen.fill(COLOUR)
    font1 = pg.font.Font(TEXT, 64)
    Txt = font1.render("Time's Up!", True, TEXT_COLOUR, None)
    Txtrect = Txt.get_rect()
    Txtrect.center = ((screen.get_rect().centerx),(screen.get_rect().centery))
    screen.blit(Txt, Txtrect)
    pg.display.flip()#Displays screen
    playSounds.timeUp()
    time.sleep(2)
