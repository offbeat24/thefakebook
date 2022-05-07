def solution(n, paths, gates, summits):
    answer = [0, 0]

    path_map = dict()
    for path in paths:
        path_map[path[0]].append(path[1] + (path[2]*100000))
        path_map[path[1]].append(path[0] + (path[2]*100000))

    for gate in gates:
        flag = 0
        visited = 0
        need_visit = list()
        need_visit.append(gate)
        intensity = 0
        tmp_answer = float('inf')
        while need_visit:
            node = need_visit.pop()
            if node == gate:
                if visited == 0:
                    visited = 1
                else:
                    tmp_answer = min(intensity, tmp_answer)
                    answer[0] = flag
                    answer[1] = tmp_answer
                    break
            if node in summits:
                if flag == 0:
                    flag = node
                else:
                    continue
            need_visit.extend(path_map[node])
            intensity = max(intensity, path_map[node] // 100000)

    return answer


print(solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [
      3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
