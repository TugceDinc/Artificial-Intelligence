#####################################
# @author Tuğçe Dinç                #
# 08:12:2020                        #
# Lab-5 8-Puzzle Problem            #
# With BFS Algorithm                #
# Python 3.6                        #
#####################################

##############---NOT---##############
#Adım adım gösterilmesi için output #
#birçok yerde kullanıldı. Output    #
#işlemleri çıkarıldığında gerçek    #
#performans gözlemlenebilir.        #
#####################################

from collections import defaultdict 

import copy

# Lab 2 de implement edilen Queue
def printPuzzle(node):
    for i in node:
        for j in i:
            print(str(j) + " ", end=" ")
        print()
class Queue:
    
    def __init__(self):
        self.list = []

    def enqueue(self, pushObj):
        self.list.append(pushObj)
        
    def dequeue(self):
        if(len(self.list) > 0):
            poped = self.list.pop(0)
            return poped
        else:
            return None
        
    def front(self):
        lengthofList = len(self.list);
        if lengthofList != 0:
            return self.list[0] 
        return None
        
    def back(self):
        lengthofList = len(self.list);
        if lengthofList != 0:
            return self.list[lengthofList - 1] 
        return None
        
    def isEmpty(self):
        if len(self.list) != 0:
            return False
        return True
    
    # Queue nun içindeki elemanları listelemek için kullanılı.
    def printQueue(self):
        if len(self.list) > 0:
            print('Queue : ', end='')
            for elem in self.list:
                print(str(elem),  end=' ')
            print()
        else:
            print("There is no element in Queue")
            
def printList(liste):
    if len(liste) > 0:
        print('Elements : ', end='')
        for elem in liste:
            print(str(elem),  end=' ')
        print()
    else:
        print("There is no element in Queue")
        
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

# Breadth firs Search İmplement edildi.
def BFS(s): 
    searchResult = []
    visited = defaultdict(lambda: False)
    queue = Queue()
    queue.enqueue(s) 
    visited["".join(map(str, s))] = True
    
    print("Steps:")
    
    flag = False
    # Queue içinde eleman kalmadığında search işlemi tamalanmış olur.
    while queue.isEmpty() == False: 
        queue.printQueue()
        s = queue.dequeue()
        searchResult.append(s)
        
        
        if(str(s) == str(goalState)):
            printPuzzle(s)
            break
        
        printPuzzle(s)
        nexts = getNextStates(s)
        for i in nexts:
            if visited["".join(map(str, i))] == False: 
                queue.enqueue(i) 
                visited["".join(map(str, i))] = True
            if(str(s) == str(goalState)):
                print("Hedefe Ulaşıldı!!!")
                printPuzzle(i)
                flag = True
                break
        if(flag == True):
            break
            
    return searchResult


sonuclar = BFS(initialState)
printList(sonuclar)