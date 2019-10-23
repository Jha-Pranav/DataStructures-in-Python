import random

class Node():
    def __init__(self,value):
        self.val = value
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = self.head
        self.len  = 0
    
    def  __str__(self):
        return {'Head' : self.head, 'Tail' : self.tail, 'Length':  self.len}

    def __len__(self): 
        return self.len
    
    def __iter__(self):
        return self

    def __next__(self):
        el = self.current
        if not el:  #iterate untill el become None
            raise StopIteration
        self.current = el.next
        return el
    def isEmpty(self):
        if not self.head:
            return True
        return False

    def push(self,item):
        element = Node(item)
        if self.isEmpty() :
            self.head = element
            self.tail = element
            self.current = self.head
        else:
            self.tail.next = element
            self.tail = element
        self.len += 1
        
        # return self.printNodes()
        

    def pop(self):
        el =  self.head
        if not el:
            return f"List is empty"
        print(self.tail.val)
        while el.next != self.tail :
            el = el.next
        popped = el.next
        el.next = None
        self.tail = el
        self.len -= 1
        return popped.val
    
    def seek(self,postion = None):
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

    def remove(self,index=None):
        if index == None:
            return self.pop()
        elif index == 0:
            self.head = self.head.next
        elif index < len(self)-1:
            el = self.seek(index-1)
            el.next = el.next.next
        else:
            raise IndexError(f'Index {index} position out of range {len(self)}')

    def delete(self,value=None):
        pos = self.find(value)
        if value == None:
            self.pop()
        elif not pos and pos != 0:
            return f'{value} not found.'
        else :
            self.remove(pos)


    def find(self, text):
        for pos,i in enumerate(iter(self)):
            if str(i.val) == str(text):
                self.seek(0)
                return pos
        return False

    def reverse(self):
        p = None
        c = self.head
        self.tail = c

        while c:
            old_next = c.next

            c.next = p

            p = c
            c = old_next
           
        self.head = p

        return self.printNodes()

        
        # printlist(self)
 
    def printNodes(self):
        el = self.head
        print('\n')
        while el:
            print(el.val,end= '  ', sep='\n')
            el = el.next
        self.seek(0)
        
    


def printlist(li):
    print('\n')
    for i in li:
        print(i.val, end='  ', sep='\n')
    li.seek(0)
        


li = LinkedList()

for j in range(50):
    li.push(random.randint(10,897))


printlist(li)
# li.printNodes()
print(type(li.reverse()))
printlist(li)