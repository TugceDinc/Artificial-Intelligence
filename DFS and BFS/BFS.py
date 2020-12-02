# -*- coding: utf-8 -*-
"""
Python : 3.6
@author: tugce
"""


from collections import defaultdict 

# Lab 2 de implement edilen sort algoritması
def bubbleSort(arr, ascending = True): 
    length = len(arr) 
    if length > 0: #array boşsa
        if length != 1: # Tek elemanı var yani zaten sıralı 
            for i in range(0, length-1): 
                for j in range(0, length-i-1): 
                    if ascending == False :
                        if arr[j] < arr[j+1]: 
                            arr[j], arr[j+1] = arr[j+1], arr[j] 
                    if ascending == True :
                        if arr[j] > arr[j+1]:
                            arr[j], arr[j+1] = arr[j+1], arr[j] 
    

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
        
    def sort(self, ascending = True):
        bubbleSort(self.list, ascending)
    
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
            print('Elements : ', end='')
            for elem in self.list:
                print(str(elem),  end=' ')
            print()
        else:
            print("There is no element in Queue")
    
# Graph implement edildi.    
class Graph: 
  
    # Constructor 
    def __init__(self): 
        self.graph = defaultdict(list) 
        
    # Graph a yeni nodelar eklemek için kullnıldı.
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    # Breadth firs Search İmplement edildi.
    def BFS(self, s): 
        # Search sonuçlarının tutulduğu List
        searchResult = []
        
        # Bulunan tüm nodeların eklenmesi için kullanıldı.
        # Implement edilen ağaca baktığımızda F nodu herhangi bir node gitmemiş.
        # Bu nedenle F nodunu da visited listesine eklemek için,
        # Lab pdfinde verilen psudo koddaki gibi intilize edilmemiştir.
        visited = defaultdict(lambda: False)
        
        # Ağaç gezilirken kullanılacak olan Queue
        # dequeue edilen her elementin komşuları Queue eklenir.
        # Bu sayede gezinme sırası bulunmuş olur.
        queue = Queue()
        # listeye ekleniyor ki Bağlı olduğı nodelar bulunsun.
        queue.enqueue(s) 
        # daha Önceden gezildiğinin anlaşılması için kullanılır bu sayede,
        # aynı node tekrar gezilip sonsuz Döngüde takılı kalmayacak
        visited[s] = True
        
        print("Steps:")
        
        # Queue içinde eleman kalmadığında search işlemi tamalanmış olur.
        while queue.isEmpty() == False: 
            queue.printQueue()
            s = queue.dequeue()
            searchResult.append(s)
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.enqueue(i) 
                    visited[i] = True
        return searchResult

def printList(liste):
    if len(liste) > 0:
        print('Elements : ', end='')
        for elem in liste:
            print(str(elem),  end=' ')
        print()
    else:
        print("There is no element in Queue")
        
# Graph burada oluşturuldu.
g = Graph() 
g.addEdge('a', 'b') 
g.addEdge('a', 'e') 
g.addEdge('b', 'd') 
g.addEdge('e', 'f')
g.addEdge('b', 'c') 
g.addEdge('d', 'b') 
g.addEdge('c', 'b') 
g.addEdge('c', 'd') 
g.addEdge('d', 'c')

# BFS burada yapılıyor.
searchResult = g.BFS('a') 
print("Result:")
# Graph arama algoritmasının sonucu.       
printList(searchResult)


