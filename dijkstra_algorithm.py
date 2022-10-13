import queue
from graphs_class import *


def dijkstra(graph, start=0):
    # if graph.negative_edge:
    #     return None
    matrix = [[float('inf') for _ in range(graph.vertex_count)]
              for _ in range(graph.vertex_count)]
    for i in range(graph.vertex_count):
        matrix[i][i] = 0
        for j in graph.adjacent_vertices[i]:
            matrix[i][j[0]] = j[1]
    min_dist = 0
    min_vertex = start
    distance = [float('inf')] * graph.vertex_count
    distance[start] = 0
    visited = [False] * graph.vertex_count
    while min_dist < float('inf'):
        i = min_vertex
        visited[i] = True
        for j in range(graph.vertex_count):
            if distance[i] + matrix[i][j] < distance[j]:
                distance[j] = distance[i] + matrix[i][j]
        min_dist = float('inf')
        for j in range(graph.vertex_count):
            if not visited[j] and distance[j] < min_dist:
                min_dist = distance[j]
                min_vertex = j
    return distance


def dijkstra_with_path(graph, start, end):
    # if graph.negative_edge:
    #     return None
    parents = [-1] * graph.vertex_count
    parents[start] = -2
    distance = [float('inf')] * graph.vertex_count
    distance[start] = 0
    q = queue.PriorityQueue()
    q.put((0, start))
    while not q.empty():
        dist, vertex = q.get()
        if dist > distance[vertex]:
            continue
        if vertex == end:
            break
        for next in graph.adjacent_vertices[vertex]:
            if distance[next[0]] > distance[vertex] + next[1]:
                parents[next[0]] = vertex
                distance[next[0]] = distance[vertex] + next[1]
                q.put((distance[next[0]], next[0]))
    return distance[end], GraphSearchAlgorithms.restore_path(
                                                parents, start, end)
