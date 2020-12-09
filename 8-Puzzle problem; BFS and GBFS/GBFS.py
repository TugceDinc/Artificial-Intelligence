#####################################
# @author Tuğçe Dinç                #
# 08:12:2020                        #
# Lab-5 8-Puzzle Problem            #
# With GBFS Algorithm               #
# Python 3.6                        #
#####################################

##############---NOT---##############
#Adım adım gösterilmesi için output #
#birçok yerde kullanıldı. Output    #
#işlemleri çıkarıldığında gerçek    #
#performans gözlemlenebilir.        #
#####################################

from queue import PriorityQueue
from collections import defaultdict 
import copy
 
visited = defaultdict(lambda: False)

def printPuzzle(node):
    print("PUZZLE")
    for i in node:
        for j in i:
            print(str(j), end=" ")
        print()
    print("-----")

def printPQ(pq):
    print(pq.queue)

def getHeuristic(source, target):
    heuristic = 0
    for i in range(len(source)):
        for j in range(i):
            if(source[i][j] != target[i][j]):
                heuristic += 1
    return heuristic
            

def GBFS(source, target):
    visited["".join(map(str, source))] = False
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        
        printPuzzle(u)
        if "".join(map(str, u)) == "".join(map(str, target)):
            break
        if visited["".join(map(str, u))] == False:
            visited["".join(map(str, u))] = True
            nexts = getNextStates(u)
            for i in nexts:
                pq.put((getHeuristic(i, target), i))
            printPQ(pq)
 
###############################################################################

initialState = [[1,2,3],[5,6,0],[7,8,4]]
goalState = [[1,2,3],[5,8,6],[0,7,4]]

         
def getNextStates(node):
    nextStates = []
    x = 0
    y = 0
    for i in range(len(node)):
        if 0 in node[i]:
            y = node[i].index(0)
            x = i
            
    if x == 2:
        cpyNode = copy.deepcopy(node)
        cpyNode[x][y], cpyNode[x-1][y] = cpyNode[x-1][y], cpyNode[x][y]
        nextStates.append(copy.deepcopy(cpyNode))
    elif x == 0:
        cpyNode = copy.deepcopy(node)
        cpyNode[x][y], cpyNode[x+1][y] = cpyNode[x+1][y], cpyNode[x][y]
        nextStates.append(copy.deepcopy(cpyNode))
    else:
        cpyNode = copy.deepcopy(node)
        cpyNode[x][y], cpyNode[x+1][y] = cpyNode[x+1][y], cpyNode[x][y]
        nextStates.append(copy.deepcopy(cpyNode))
        cpyNode = copy.deepcopy(node)
        cpyNode[x][y], cpyNode[x-1][y] = cpyNode[x-1][y], cpyNode[x][y]
        nextStates.append(copy.deepcopy(cpyNode))
        
        
    if y == 2:
        cpyNode = copy.deepcopy(node)
        cpyNode[x][y], cpyNode[x][y-1] = cpyNode[x][y-1], cpyNode[x][y]
        nextStates.append(copy.deepcopy(cpyNode))
    elif y == 0:
        cpyNode = copy.deepcopy(node)
        cpyNode[x][y], cpyNode[x][y+1] = cpyNode[x][y+1], cpyNode[x][y]
        nextStates.append(copy.deepcopy(cpyNode))  
    else:
        cpyNode = copy.deepcopy(node)
        cpyNode[x][y], cpyNode[x][y-1] = cpyNode[x][y-1], cpyNode[x][y]
        nextStates.append(copy.deepcopy(cpyNode))
        cpyNode = copy.deepcopy(node)
        cpyNode[x][y], cpyNode[x][y+1] = cpyNode[x][y+1], cpyNode[x][y]
        nextStates.append(copy.deepcopy(cpyNode))
        
    return nextStates

GBFS(initialState, goalState)