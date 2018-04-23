def makeQpacks():#Coordinates the making of the question packs
    qpack = readfile()#Reads the questions
    qp1 = makeQP1(qpack)#Makes the easy question pack
    qp2 = makeQP2(qpack)#Makes the medium question pack
    qp3 = makeQP3(qpack)#Makes the hard question pack
    return qp1, qp2, qp3

def readfile():#Reads the question file and closes it
    f  = open('questionpack.txt', 'r')
    qpack = f.readlines()
    f.close()
    return qpack

def makeQP1(qpack):#Makes the easy question pack
    qp1 = []
    for i in qpack:
        dif, question, a1, a2, a3, a4, ca = i.split(",")
        ca = ca.replace("\n","")
        if int(dif) == 1:
            qp1.append([question, a1, a2, a3, a4, ca])
        else:
            pass
    return qp1

def makeQP2(qpack):#Makes the medium question pack
    qp2 = []
    for i in qpack:
        dif, question, a1, a2, a3, a4, ca = i.split(",")
        ca = ca.replace("\n","")
        if int(dif) == 2:
            qp2.append([question, a1, a2, a3, a4, ca])
        else:
            pass
    return qp2
    
def makeQP3(qpack):#Makes the hard question pack
    qp3 = []
    for i in qpack:
        dif, question, a1, a2, a3, a4, ca = i.split(",")
        ca = ca.replace("\n","")
        if int(dif) == 3:
            qp3.append([question, a1, a2, a3, a4, ca])
        else:
            pass
    return qp3
