class Deque():

    def __init__(self):
        self.item = []

    def __str__(self):
        return f'{self.item}'

    def __len__(self):
        return self.item.__len__()

    def isempty(self):
        return self.item == []

    def push_front(self, *data):
        for en in data:  # Each entity in input data. It can be any iterrative object
            self.item.append(en)
        return self.item
    
    def push_rear(self, *data):
        for en in data:  # Each entity in input data. It can be any iterrative object
            self.item.insert(0,en)
        return self.item

    def pop_front(self):
        return self.item.pop()

    def pop_rear(self):
        return self.item.pop(0)

    def peek(self):
        return self.item[0]

    def size(self):
        return len(self)
