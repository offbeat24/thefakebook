from collections import deque
import copy


class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.child = list()

    def __repr__(self):
        return str(self.item)


class Tree:
    def __init__(self, root):
        self.root = root

    def find_cousin(self, node):
        answer = 0
        try:
            uncles = deque(node.parent.parent.child)
        except:
            return 0
        while uncles:
            uncle = uncles.popleft()
            if uncle == node.parent:
                continue
            else:
                answer += len(uncle.child)
                # print(uncle.child)
        return answer


while True:
    n, k = map(int, input().split())
    if not n and not k:
        exit(0)
    elif n == 1 or n == 2:
        print(0)
        continue
    input_arr = list(map(int, input().split()))
    nodes = list()
    for i in range(n):
        if input_arr[i] == k:
            nk = Node(k)
            nodes.append(nk)
        else:
            nodes.append(Node(input_arr[i]))
    # print(nodes)
    tree = Tree(nodes[input_arr[0]])
    siblings = list()
    parents = deque()
    parents.append(nodes[0])
    siblings.append(nodes[1])
    # print(siblings)
    for i in range(2, n):
        if input_arr[i-1] + 1 == input_arr[i]:
            siblings.append(nodes[i])
            # print(siblings)
        if input_arr[i-1] + 1 < input_arr[i] or i == n-1:
            tmp_parent = parents.popleft()
            for j in siblings:
                j.parent = tmp_parent
                tmp_parent.child.append(j)
            parents += siblings
            siblings.clear()
            try:
                siblings.append(nodes[i])
            except:
                break
    print(tree.find_cousin(nk))
