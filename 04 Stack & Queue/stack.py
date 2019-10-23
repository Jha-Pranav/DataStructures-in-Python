import random

class Stack():

    def __init__(self):
        self.item = []

    def __str__(self):
        return f'{self.item}'

    def __len__(self):  # return value of len(Stack())
        return self.item.__len__()

    def isempty(self):
        return self.item == []
           

    def push(self,*data):
        for en in data:  # Each entity in input data. It can be any iterrative object
            self.item.append(en)
        return self.item

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self)
    

s = Stack()
for i in range(61):
    s.push(random.randint(0,3000))
print(s)
print(s.peek())
print(s.size())
print(len(s))