from collections import defaultdict 

maxpeople = 2

m, c, b = 3, 3, 0

# Lab 2 de implement edilen Stack
class Stack:
    
    def __init__(self):
        self.list = []

    def push(self, pushObj):
        self.list.append(pushObj)
        
    def pop(self):
        if(len(self.list) > 0):
            poped = self.list.pop()
            return poped
        else:
            print("List is empty, do not Poped...")
            return None
        
    def top(self):
        lengthofList = len(self.list);
        if lengthofList != 0:
            return self.list[lengthofList - 1] 
        return None
    
    def isEmpty(self):
        if len(self.list) != 0:
            return False
        return True
    def printStack(self):
        if len(self.list) > 0:
            print('Stack : ', end='')
            for elem in self.list:
                print(str(elem),  end=' ')
            print()
        else:
            print("There is no element in Stack")
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
# A function used by DFS
def DFSRecursive(visited, stack):
    stack.printStack()
    v = stack.pop()
    
    print(str(v) + " =>  ", end='')
    if(v[0] == v[1] == 0 and v[2] == 1):
        stack.push(v)
        stack.printStack()
        return True
    
    visited["".join(map(str, v))] = True
    
    nexts = getNextStates(v, ((v[2] + 1) % 2))
    for neighbour in nexts:
        if visited["".join(map(str, neighbour))] == False:
            stack.push(neighbour)
            
    if(DFSRecursive(visited, stack) == True):
        return True
        
def DFS(v):
    print("Current\t\t"+ "Found states(F:not usable state, A: usable state)")
    visited = defaultdict(lambda: False)
    stack = Stack()
    stack.push(v)
    DFSRecursive(visited, stack)


InitialState = [3,3,0]
DFS(InitialState)