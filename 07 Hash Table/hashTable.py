class HashTable:

    def __init__(self,lstLen=53):
        self.lst = [[] for i in range(lstLen)]

    def __str__(self):
        return f'{self.lst}'

    def _hashFunc(self,string):
        total = 0
        weird_prime = 31
        for i in string[:100]:
            total += ord(i) - 96
            total = (total * weird_prime) % len(self.lst)
        return total

    def setValue(self,key,val):
        indx = self._hashFunc(key)
        if self.lst[indx] == []:
            self.lst[indx].append(key)
            self.lst[indx].append(val)
        else:
            
            if type(self.lst[indx][0]) != list:
                self.lst[indx] = list([self.lst[indx]])
                self.lst[indx].append([key, val])
            else:
                self.lst[indx].append([key, val])

            

            
        return self.lst

    def getValue(self,key):
        indx = self._hashFunc(key)
        for k in self.lst[indx]: 
            if type(k) == list:
                if k[0] == key:
                    return k[1]
                else:
                    return False
            else:
                return k





hash = HashTable()
hash.setValue('Pranav','Jha')
hash.setValue('Yup',123)
hash.setValue('gibberish','1 2 ka 4')

# Generate random word
import random
import string
 

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

for i in range(100):
    hash.setValue(randomString(),randomString())

print(hash)
print(hash.getValue('Pranav'))
print(hash.getValue('gibberish'))



