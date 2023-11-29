def dfs(node, graph, visited):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)
            
def solution(edges):
    # 그래프 구축 (인접 리스트)
    out_graph = {}
    in_graph = {}
    nom_node = []
    for u, v in edges:
        if u not in out_graph:
            out_graph[u] = []
        if v not in out_graph:
            out_graph[v] = []
        if u not in in_graph:
            in_graph[u] = []
        if v not in in_graph:
            in_graph[v] = []
        out_graph[u].append(v)
        in_graph[v].append(u)

    # 각 정점의 차수 계산
    degree = {node: 0 for node in in_graph}
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    for node in in_graph:
      if len(in_graph[node]) == 0 :
        if len(out_graph[node]) != 1 :
          created_vertex = node
          break
    
    graph = out_graph.copy()
    del graph[created_vertex]

    visited = list()
    visited_graph = list()
    donut_count = bar_count = figure_eight_count = 0
    for node in graph:
        if node not in visited and len(graph[node]) != 0:
            visited_graph.clear()
            dfs(node, graph, visited_graph)
            
            edge = 0
            for n in visited_graph :
              edge += len(out_graph[n])
            if len(visited_graph) == edge :
              donut_count += 1
            elif len(visited_graph)-1 == edge :
              bar_count += 1
            elif len(visited_graph) +1 == edge :
              figure_eight_count += 1
            visited += visited_graph
        if node not in visited and len(graph[node]) == 0 and in_graph[node] == [created_vertex] :
          bar_count += 1
          visited.append(node)
    return [created_vertex, donut_count, bar_count, figure_eight_count]

# 테스트
edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(edges))  # 예상 출력: [2, 1, 1, 0]
