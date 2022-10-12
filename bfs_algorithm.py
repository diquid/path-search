import queue
from graphs_class import *


def bfs(graph, start, end):
    vertex_queue = queue.Queue()
    vertex_queue.put(start)

    parents = [-1] * graph.vertex_count
    parents[start] = -2

    while not vertex_queue.empty():
        vertex = vertex_queue.get()
        if vertex == end:
            return GraphSearchAlgorithms.restore_path(parents, start, end)

        for next_vertex in graph.adjacent_vertices[vertex]:
            if parents[next_vertex] == -1:
                parents[next_vertex] = vertex
                vertex_queue.put(next_vertex)
    return None
