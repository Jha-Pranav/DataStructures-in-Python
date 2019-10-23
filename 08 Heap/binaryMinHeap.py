class BinaryMinHeap:
    def __init__(self):
        self.val = []

    def bubbleUp(self):
        Indx = len(self.val) - 1
        parentIndx = (Indx - 1) // 2
        while self.val[Indx] < self.val[parentIndx] and Indx != 0:
            self.val[Indx], self.val[parentIndx] = self.val[parentIndx], self.val[Indx]
            Indx = parentIndx
            parentIndx = (Indx - 1) // 2

    def bubbleDown(self):
        e = self.val
        Indx = 0
        leftIndx = 2 * Indx + 1
        rightIndx = leftIndx + 1
        while rightIndx < len(e):
            if e[leftIndx] < e[rightIndx]:
                swpIndx = leftIndx
            else:
                swpIndx = rightIndx
            e[Indx], e[swpIndx] = e[swpIndx], e[Indx]
            Indx = swpIndx
            leftIndx = 2 * Indx + 1
            rightIndx = leftIndx + 1


    def insert(self, en):
        if not self.val:
            self.val.append(en)
        else:
            self.val.append(en)
            self.bubbleUp()
        return self.val

    def extractMin(self):
        self.val[0] = self.val.pop()
        self.bubbleDown()
        return self.val


min_heap = BinaryMinHeap()
min_heap.insert(41)
min_heap.insert(39)
min_heap.insert(33)
min_heap.insert(12)
min_heap.insert(18)
min_heap.insert(27)
print(min_heap.insert(55))
print(min_heap.extractMin())
