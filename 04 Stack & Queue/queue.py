from random import randint

class Queue():

    def __init__(self):
        self.item = []

    def __str__(self):
        return f'{self.item}'

    def __len__(self):
        return self.item.__len__()
    
    def isempty(self):
        return self.item == []

    def push(self, *data):
        for en in data:  # Each entity in input data. It can be any iterrative object
            self.item.append(en)
        return self.item

    def pop(self):
        return self.item.pop(0)

    def peek(self):
        return self.item[0]

    def size(self):
        return len(self)

q = Queue()
for qu in range(100):
    q.push(randint(0,5000))

print(q)
print(len(q))
print(q.size())
print(q.peek())
print(q.pop())
print(q)
