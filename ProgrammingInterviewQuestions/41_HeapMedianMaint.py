class HeapMin():
    def __init__(self):
        self.start = 0
        self.array = [None] * 100000
        self.end = 0
        
    def heapRoot(self):
        return self.array[0]
        
    def getSize(self):
        return self.end
        
    def insert(self, val):
        self.array[self.end] = val
        self.end += 1
        currIndex = self.end
        parentIndex = currIndex / 2
        #print "out", currIndex, parentIndex
        parent = self.array[parentIndex - 1]
        #print val, parent
        while val < parent and parentIndex > 0:
            #print "parent", "child", parentIndex - 1, currIndex - 1
            #print self.array[parentIndex - 1], self.array[currIndex - 1]
            self.array[parentIndex - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[parentIndex - 1]
            currIndex = parentIndex
            parentIndex = currIndex / 2
            parent = self.array[parentIndex - 1]
        return
        
    def checkHeapProperty(self):
        currIndex = self.end
        parentIndex = currIndex / 2
        while parentIndex > 0:
            if self.array[parentIndex - 1] > self.array[currIndex - 1]:
                print "not equal at", parentIndex - 1, currIndex - 1, "values", self.array[parentIndex - 1], self.array[currIndex - 1]
            currIndex -= 1
            parentIndex = currIndex / 2
        return
        
    def extractMin(self):
        if self.end == 0:
            return None
            
        toRemove = self.array[0]
        
        self.end -= 1
        self.array[0] = self.array[self.end]
        self.array[self.end] = None
        
        currIndex = 1
        child1Index = currIndex * 2
        child2Index = currIndex * 2 + 1
        
        while child1Index <= self.end:
        #while child1Index <= self.end and (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
            if child2Index > self.end:
                child2Index = child1Index
            if (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
                if self.array[child1Index - 1] <= self.array[child2Index - 1]:
                    self.array[child1Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child1Index - 1] 
                    currIndex = child1Index
                    child1Index = currIndex * 2
                    child2Index = currIndex * 2 + 1
                else:
                    self.array[child2Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child2Index - 1] 
                    currIndex = child2Index
                    child1Index = currIndex * 2
                    child2Index = currIndex * 2 + 1
            else:
                child1Index = self.end + 1
        
        #self.checkHeapProperty()
        return toRemove

class HeapMax():
    def __init__(self):
        self.start = 0
        self.array = [None] * 100000
        self.end = 0
        
        
    def heapRoot(self):
        return self.array[0]
        
    def getSize(self):
        return self.end
        
    def insert(self, val):
        self.array[self.end] = val
        self.end += 1
        currIndex = self.end
        parentIndex = currIndex / 2
        #print "out", currIndex, parentIndex
        parent = self.array[parentIndex - 1]
        #print val, parent
        while val > parent and parentIndex > 0:
            #print "parent", "child", parentIndex - 1, currIndex - 1
            #print self.array[parentIndex - 1], self.array[currIndex - 1]
            self.array[parentIndex - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[parentIndex - 1]
            currIndex = parentIndex
            parentIndex = currIndex / 2
            parent = self.array[parentIndex - 1]
        return
        
    def checkHeapProperty(self):
        currIndex = self.end
        parentIndex = currIndex / 2
        while parentIndex > 0:
            if self.array[parentIndex - 1] < self.array[currIndex - 1]:
                print "not equal at", parentIndex - 1, currIndex - 1, "values", self.array[parentIndex - 1], self.array[currIndex - 1]
            currIndex -= 1
            parentIndex = currIndex / 2
        return
        
    def extractMax(self):
        if self.end == 0:
            return None
            
        toRemove = self.array[0]
        
        self.end -= 1
        self.array[0] = self.array[self.end]
        self.array[self.end] = None
        
        currIndex = 1
        child1Index = currIndex * 2
        child2Index = currIndex * 2 + 1
        
        while child1Index <= self.end:
        #while child1Index <= self.end and (self.array[currIndex - 1] > self.array[child1Index - 1] or self.array[currIndex - 1] > self.array[child2Index - 1]):
            if child2Index > self.end:
                child2Index = child1Index
            if (self.array[currIndex - 1] < self.array[child1Index - 1] or self.array[currIndex - 1] < self.array[child2Index - 1]):
                if self.array[child1Index - 1] >= self.array[child2Index - 1]:
                    self.array[child1Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child1Index - 1] 
                    currIndex = child1Index
                    child1Index = currIndex * 2
                    child2Index = currIndex * 2 + 1
                else:
                    self.array[child2Index - 1], self.array[currIndex - 1] = self.array[currIndex - 1], self.array[child2Index - 1] 
                    currIndex = child2Index
                    child1Index = currIndex * 2
                    child2Index = currIndex * 2 + 1
            else:
                child1Index = self.end + 1
        
        #self.checkHeapProperty()
        return toRemove
    

def medianMaint(n):
    heapMin = HeapMin()
    heapMax = HeapMax()
    for i in range(0, n):
        val = map(int, raw_input().strip().split(' '))
        val = val[0]
        
        if n == 0:
            heapMax.insert(val)
            print val / 1.0
        elif n == 1:
            maxp = heapMax.extractMax()
            if maxp > val:
                heapMin.insert(maxp)
                heapMax.insert(val)
            else:
                heapMin.insert(val)
                heapMax.insert(maxp)
            print (maxp + val) / 2.0
        else:
            if val <= heapMax.heapRoot():
                heapMax.insert(val)
            else:
                heapMin.insert(val)
            if heapMax.getSize() >= heapMin.getSize() + 2:
                heapMin.insert(heapMax.extractMax())
            elif heapMin.getSize() >= heapMax.getSize() + 2:
                heapMax.insert(heapMin.extractMin())
            if heapMax.getSize() == heapMin.getSize():
                mid = (heapMin.heapRoot() + heapMax.heapRoot()) / 2.0
            else:
                if heapMax.getSize() > heapMin.getSize():
                    mid = heapMax.heapRoot() / 1.0
                else:
                    mid = heapMin.heapRoot() / 1.0
                    
            print mid
            
        

def main():
    n = int(raw_input().strip())
    
    medianMaint(n)
        
    
    
main()


