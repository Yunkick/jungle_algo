import sys

sys.setrecursionlimit(10 ** 9)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None :
            self.root = Node(value)
            return
        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value)   


tree = BinaryTree()

# 모든 입력을 한 번에 읽기
input_data = sys.stdin.read().splitlines()

# 입력된 값들로 트리 구성
for line in input_data:
    if line.strip():  # 빈 줄은 제외
        tree.insert(int(line.strip()))

# 후위 순회 출력
tree.post_order(tree.root)