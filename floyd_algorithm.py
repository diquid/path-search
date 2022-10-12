def floyd(graph):
    res = [[float('inf') for _ in range(graph.vertex_count)] for _ in range(graph.vertex_count)]
    for i in range(graph.vertex_count):
        res[i][i] = 0
        for j in graph.adjacent_vertices[i]:
            res[i][j[0]] = j[1]
    for k in range(graph.vertex_count):
        for i in range(graph.vertex_count):
            for j in range(graph.vertex_count):
                if res[i][k] != float('inf') and res[k][j] != float('inf') and res[i][j] > res[i][k] + res[k][j]:
                    res[i][j] = res[i][k] + res[k][j]
    return res