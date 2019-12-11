def preorder(node):
    print(node.data, end='')
    if node.lC != '.':
        preorder(tree[node.lC])
    if node.rC != '.':
        preorder(tree[node.rC])

def inorder(node):
    if node.lC != '.':
        inorder(tree[node.lC])
    print(node.data, end='')
    if node.rC != '.':
        inorder(tree[node.rC])

def postorder(node):
    if node.lC != '.':
        postorder(tree[node.lC])
    if node.rC != '.':
        postorder(tree[node.rC])
    print(node.data, end='')
    


class Node:
    def __init__(self, data, lC, rC):
        self.data = data
        self.lC = lC
        self.rC = rC

n = int(input())
tree = {}
for i in range(n):
    a = list(map(str, input().split()))
    tree[a[0]] = Node(data = a[0], lC = a[1], rC = a[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

