from collections import defaultdict, deque
import copy


class Node:
    def __init__(self, item):
        self.item = item
        self.child = list()

    def __str__(self):
        return str(self.data)


input_case = list()
case = deque()
answer = list()
while True:
    branch_ = list(map(int, input().rstrip().split()))
    input_case += branch_

    if input_case[-1] < 0:
        input_case.pop()
        input_case.pop()
        break


def tree_pot():
    tmp_case = deque()
    for i in range(0, len(input_case)-1, 2):
        if input_case[i] != 0 and input_case[i+1] != 0:
            tmp_case.append(input_case[i])
            tmp_case.append(input_case[i+1])
        else:
            tmp_case.append(input_case[i])
            tmp_case.append(input_case[i+1])
            case.append(copy.deepcopy(tmp_case))
            tmp_case.clear()


tree_pot()

while case:
    test_case = case.popleft()
    print(test_case)
    if test_case == deque([0, 0]):
        answer.append(True)
        continue
    test_case_set = set(test_case)
    node_arr = dict()
    for i in test_case_set:
        node_arr[i] = Node(i)

    while test_case:
        node_arr[test_case.popleft()].child.append(
            node_arr[test_case.popleft()])

    tmp = list()
    for num in test_case_set:
        flag = 0
        for node_ in node_arr.values():
            if node_arr[num] in node_.child:
                flag += 1
                if flag > 1:
                    tmp.append(False)
                    tmp.append(False)
                    break
        if not flag:
            tmp.append(num)
    if len(tmp) != 1:
        answer.append(False)
    else:
        answer.append(True)


for i in range(len(answer)):
    if answer[i]:
        print("Case", i+1, "is a tree.", sep=" ")
    else:
        print("Case", i+1, "is not a tree.", sep=" ")
