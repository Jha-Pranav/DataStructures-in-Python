import random

class Node():
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None


class DoublyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = self.head
        self.len = 0

    def __str__(self):
        return {'Head': self.head, 'Tail': self.tail, 'Length':  self.len}

    def __len__(self):
        return self.len

    def __iter__(self):
        return self

    def __next__(self):
        el = self.current
        if not el:  # iterate untill el become None
            raise StopIteration
        self.current = el.next
        return el

    def isEmpty(self):
        if not self.head:
            return True
        return False

    def push(self, item):
        element = Node(item)
        if self.isEmpty():
            self.head = element
            self.tail = element
            self.head.prev = None
            self.current = self.head

        else:
            self.tail.next = element
            self.tail.next.prev = self.tail
            self.tail = element
        self.len += 1
        
        # return self.printNodes()

    def pop(self):
        el = self.head
        if not el:
            return f"List is empty"
        popping = self.tail
        popping.prev.next = None
        self.tail = popping.prev
        self.len -= 1
        return popping.val

    def seek(self, postion=None):
        if not postion and postion != 0:
            return self.tail
        elif postion > len(self)-1:
            raise IndexError('Linked-list index is out of range.')
        el = self.head
        pos = 0
        while pos != postion:
            el = el.next
            pos += 1
        self.current = self.head
        return el.val

    def insert(self, value, position):
        newEl = Node(value)
        for pos, el in enumerate(iter(self)):
            if position == 0:
                newEl.next = self.head
                self.head = newEl
                self.len += 1
                break
            elif pos == position - 1:
                newEl.next = el.next
                el.next = newEl
                self.len += 1
                break
            elif pos == position:
                self.push(value)
                break
            else:
                raise IndexError('Insertion postion index is out of range.')
        self.seek(0)
        return self.printNodes()

    def remove(self, index=None):
        if index == None:
            return self.pop()
        elif index == 0:
            self.head = self.head.next
            self.len -= 1
        elif index < len(self)-1:
            el = self.seek(index-1)
            el.next = el.next.next
            self.len -= 1
        else:
            raise IndexError(
                f'Index {index} position out of range {len(self)}')

    def delete(self, value=None):
        pos = self.find(value)
        if value == None:  # value is not provided; remove last item.
            self.pop()
        # make sure the item should be at 0th index.
        elif not pos and pos != 0: # item is not present in the link-list.
            return f'{value} not found.'
        else:  # otherwise remove it by using it's index postion value
            self.remove(pos)

    def find(self, text):
        for pos, i in enumerate(iter(self)):
            if str(i.val) == str(text):
                self.seek(0)  # make sure to reset it's cursor
                return pos
        return False  # found : return it's postion; else simply return false

    def reverse(self):
        el = self.tail
        self.head = el
        # self.head.prev = None
        new_next = el.prev
        while new_next:
            el.next = new_next
            new_next = el.next.prev  # new next is our old previous
            el.next.prev = el
            el = el.next

        self.tail = el
        el.next = None
        return self.printNodes() 

    def printNodes(self):
        el = self.head
        print('\n')
        while el:
            print(el.val, end='  ', sep='\n')
            el = el.next
        self.seek(0)


def printlist(li):
    print('\n')
    for i in li:
        print(i.val, end='  ', sep='\n')
    li.seek(0)


li = DoublyLinkedList()

for j in range(1000):
    li.push(j)


printlist(li)
# li.printNodes()
# print(li.seek(0))
li.reverse()

