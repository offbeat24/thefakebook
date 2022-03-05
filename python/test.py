class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.child = list()

    def __str__(self):
        return str(self.item)


n = Node(1)
n1 = Node(2)
nodes = list()
nodes.append(n)
nodes.append(n1)

for i in nodes:
    if i == 2:
        print(i)
