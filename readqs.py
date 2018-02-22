def readfile():
    f  = open('questionpack.txt', 'r')
    qpack = f.readlines()
    f.close()
    return qpack

def makeQP1(qpack):
    qp1 = []
    for i in qpack:
        dif, question, a1, a2, a3, a4, ca = i.split(",")
        ca = ca.replace("\n","")
        if int(dif) == 1:
            qp1.append([question, a1, a2, a3, a4, ca])
        else:
            pass
    return qp1

def makeQP2(qpack):
    qp2 = []
    for i in qpack:
        dif, question, a1, a2, a3, a4, ca = i.split(",")
        ca = ca.replace("\n","")
        if int(dif) == 2:
            qp2.append([question, a1, a2, a3, a4, ca])
        else:
            pass
    return qp2
    
def makeQP3(qpack):
    qp3 = []
    for i in qpack:
        dif, question, a1, a2, a3, a4, ca = i.split(",")
        ca = ca.replace("\n","")
        if int(dif) == 3:
            qp3.append([question, a1, a2, a3, a4, ca])
        else:
            pass
    return qp3
