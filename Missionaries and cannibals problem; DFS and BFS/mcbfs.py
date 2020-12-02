from collections import defaultdict 

maxpeople = 2

m, c, b = 3, 3, 0

# Lab 2 de implement edilen Queue
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
        
def checkStatus(node):
    karsi = []
    karsi.append(m - node[0])
    karsi.append(c - node[1])
    if(karsi[0] == 0 or node[0] == 0):
        print("A:" + str(node), end='')
        return True
    if(karsi[1] <= karsi[0] and node[1] <= node[0]):
        print("A:" + str(node), end='')
        return True
    print("F:" + str(node), end='')
    return False    
         
def getNextStates(node, side):
    nextStates = []
    
    if side == 0:
        xxx = m if (node[0] + maxpeople) > m  else (node[0] + maxpeople)
        for i in range(node[0] + 1, xxx+1, 1):
            temp = [i, node[1], side]
            if checkStatus(temp):
                nextStates.append(temp)
                
        xxx = c if (node[1] + maxpeople) > c  else (node[1] + maxpeople)
        for i in range(node[1] + 1, xxx+1, 1):
            temp = [node[0], i, side]
            if checkStatus(temp):
                nextStates.append(temp)
                
        if not ( node[0] + 1 >= m or node[1] + 1 >= c):
            temp = [node[0] + 1, node[1] + 1, side]
            print("A:" + str(temp), end='')
            nextStates.append(temp)
            
    if side == 1:
        xxx = (node[0] - maxpeople) if (node[0] - maxpeople) > 0  else 0
        for i in range(xxx, node[0], 1):
            temp = [i, node[1], side]
            if checkStatus(temp):
                nextStates.append(temp)
                
        xxx = (node[1] - maxpeople) if (node[1] - maxpeople) > 0  else 0
        for i in range(xxx, node[1], 1):
            temp = [node[0], i, side]
            if checkStatus(temp):
                nextStates.append(temp)
                
        if not (node[0] - 1 < 0 or node[1] - 1 < 0):
            temp = [node[0] - 1, node[1] - 1, side]
            print("A:" + str(temp), end='')
            nextStates.append(temp)   
    print()
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
        if(s[0] == s[1] == 0 and s[2] == 1):
            break
        print(str(s) + " => ", end=' ')
        nexts = getNextStates(s,((s[2] + 1) % 2))
        for i in nexts:
            if visited["".join(map(str, i))] == False: 
                queue.enqueue(i) 
                visited["".join(map(str, i))] = True
            if(i[0] == i[1] == 0 and i[2] == 1):
                print(str(i) + " => Bulundu!!!  ", end=' ')
                flag = True
                break
        if(flag == True):
            break
            
    return searchResult

InitialState = [3,3,0]
sonuclar = BFS(InitialState)
printList(sonuclar)