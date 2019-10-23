class Node:
    def __init__(self,val,priority):
        self.entity = val
        self.priority = priority

class BinaryMinHeap:
    def __init__(self):
        self.val = []

    def __str__(self):
        return f"{[i.entity for i in self.val]}"

    def bubbleUp(self):
        Indx = len(self.val) - 1
        parentIndx = (Indx - 1) // 2
        while self.val[Indx].priority < self.val[parentIndx].priority and Indx != 0:
            self.val[Indx], self.val[parentIndx] = self.val[parentIndx], self.val[Indx]
            Indx = parentIndx
            parentIndx = (Indx - 1) // 2

    def bubbleDown(self):
        e = self.val
        Indx = 0
        leftIndx = 2 * Indx + 1
        rightIndx = leftIndx + 1
        while rightIndx < len(e):
            if e[leftIndx].priority < e[rightIndx].priority:
                swpIndx = leftIndx
            else:
                swpIndx = rightIndx
            e[Indx], e[swpIndx] = e[swpIndx], e[Indx]
            Indx = swpIndx
            leftIndx = 2 * Indx + 1
            rightIndx = leftIndx + 1

    def enqueue(self, val, priority):
        node = Node(val,priority)
        if not self.val:
            self.val.append(node)
        else:
            self.val.append(node)
            self.bubbleUp()
        return [i.entity for i in self.val]

    def dequeue(self):
        self.val[0] = self.val.pop()
        self.bubbleDown()
        return [i.entity for i in self.val]


pqueue = BinaryMinHeap()
pqueue.enqueue('A',1)
pqueue.enqueue('B',5)
pqueue.enqueue('C',4)
pqueue.enqueue('D',3)
pqueue.enqueue('E',2)
pqueue.enqueue('F',0)
print(pqueue)
print(pqueue.dequeue())
