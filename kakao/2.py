def solution(queue1, queue2):
    len1 = len(queue1)
    len2 = len(queue2)
    answer = -2
    tp_sum = sum(queue1)
    queue1.extend(queue2)
    sumq = sum(queue1)
    if sumq % 2 != 0:
        return -1
    else:
        target = sumq // 2

        left = 0
        right = len1 - 1

        while left <= right < len1 + len2:
            if tp_sum == target:
                answer = (left + right + 1 - len1)
                break
            if tp_sum < target:
                right += 1
                try:
                    tp_sum += queue1[right]
                except:
                    continue
                continue
            if tp_sum > target:
                tp_sum -= queue1[left]
                left += 1
                continue
        else:
            answer = -1
    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
