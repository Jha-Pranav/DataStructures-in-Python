
class Graph:

    def __init__(self):
        self.adjancency = {}

    def __str__(self):
        return f"{self.adjancency}"

    def addVertex(self,item):
        # Prevent duplicate entry to override value
        if not self.adjancency.get(item):
            self.adjancency[item] = []

    def addEdge(self,vrtx1,vrtx2):
        e = self.adjancency
        e[vrtx1].push(vrtx2)
        e[vrtx2].push(vrtx1)
    
    def removeVertex(self, vrtx):
        e = self.adjancency
        for lst in e['vrtx']:
            e[lst].remove(vrtx)
        del(e[vrtx])
    

    def removeEdge(self,v1,v2):
        e = self.adjancency
        e[v1].remove(v2)
        e[v2].remove(v1)
        





