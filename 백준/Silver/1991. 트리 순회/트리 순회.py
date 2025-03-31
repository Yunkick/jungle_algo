class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self,root,left,right):
        if root not in self.nodes:
            self.nodes[root] = Node(root)
        

        if left != ".":
            self.nodes[left] = Node(left)
            self.nodes[root].left = self.nodes[left]
            
        
        if right != ".":
            self.nodes[right] = Node(right)
            self.nodes[root].right = self.nodes[right]
            

    def pre_order(self, node):
        if node:
            print(node.value, end="")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end="")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end="")   

n = int(input())
tree = BinaryTree()

for _ in range(n):
    root, left, right = input().split()
    tree.add_node(root,left,right)

root_node = tree.nodes['A']

tree.pre_order(root_node)
print()
tree.in_order(root_node)
print()
tree.post_order(root_node)
print()