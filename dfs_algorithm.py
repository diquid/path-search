from graphs_class import *


def _dfs(graph, parents, previous, start, end):
    if previous == end:
        return True
    for current in graph.adjacent_vertices[previous]:
        if parents[current] == -1:
            parents[current] = previous
            if _dfs(graph, parents, current, start, end):
                return True
    return False


def dfs(graph, start, end):
    parents = [-1] * graph.vertex_count
    parents[start] = -2
    _dfs(graph, parents, start, start, end)
    return GraphSearchAlgorithms.restore_path(parents, start, end)
