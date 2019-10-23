class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,val):
        node = Node(val)
        if not self.root :
            self.root = node
        else:
            current = self.root
            while True:
                if current.val ==  val:
                    return "Entry alredy exists"
                elif val < current.val:
                    if not current.left:
                        current.left = node
                        break
                    current = current.left

                else:
                    if not current.right:
                        current.right = node
                        break
                    current = current.right

    def find(self,item):
        current = self.root
        if not current :
            return f"Tree is empty"
        if current.val == item:
            return True
        while current :
            if current.val == item:
                return True
            elif item < current.val:
                current = current.left
            else:
                current = current.right 
        return f"Search not found"

    def breadthFirstSearch(self):
        queue = [self.root]
        visited = []
        while queue:
            current = queue.pop(0)
            visited.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return visited

    def dfsPreorder(self):
        result = []
        def traverse(node):
            result.append(node.val)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
        traverse(self.root)
        return result

    def dfsInorder(self):
        result = []

        def traverse(node):
            
            if node.left:
                traverse(node.left)
            result.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return result

    def dfsPostorder(self):
        result = []

        def traverse(node):
            
            if node.left:
                traverse(node.left)
        
            if node.right:
                traverse(node.right)
            result.append(node.val)
        traverse(self.root)
        return result

tree = BinarySearchTree()
tree.insert(41)
tree.insert(20)
tree.insert(11)
tree.insert(29)
tree.insert(65)
tree.insert(50)
tree.insert(91)
tree.insert(72)
tree.insert(99)

print(tree.find(91))
print(tree.find(50))

print("BFS : ",tree.breadthFirstSearch())
print("DFS-Preorder : ",tree.dfsPreorder())
print("DFS-Inorder :", tree.dfsInorder())
print("DFS-Postorder :", tree.dfsPostorder())
