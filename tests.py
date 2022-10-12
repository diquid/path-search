import unittest
import graph_random_builder
from graphs_class import GraphSearchAlgorithms, WeightedGraphSearchAlgorithms
import queue
from dfs_algorithm import dfs
from bfs_algorithm import bfs
from dijkstra_algorithm import dijkstra
from floyd_algorithm import floyd


def is_graph_connected(vertex_count, edges):
    q = queue.Queue()
    adjacent_vertices = []
    for visit in range(vertex_count):
        adjacent_vertices.append(set())
    for visit in edges:
        adjacent_vertices[visit[0]].add(visit[1])
        adjacent_vertices[visit[1]].add(visit[0])
    visited = [False] * vertex_count
    q.put(0)
    visited[0] = True
    while not q.empty():
        vertex = q.get()
        for neighbour in adjacent_vertices[vertex]:
            if not visited[neighbour]:
                q.put(neighbour)
                visited[neighbour] = True
    for visit in visited:
        if not visit:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_undirected_graph(self):
        g = GraphSearchAlgorithms(vertex_count=6, edges=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], oriented=False)
        path_dfs1 = dfs(g, 0, 5)
        path_bfs1 = bfs(g, 0, 5)
        path_dfs2 = dfs(g, 2, 5)
        path_bfs2 = bfs(g, 2, 5)
        path_dfs3 = dfs(g, 2, 1)
        path_bfs3 = bfs(g, 2, 1)
        path_dfs4 = dfs(g, 1, 1)
        path_bfs4 = bfs(g, 1, 1)
        self.assertEqual(path_dfs1, [0, 1, 2, 3, 4, 5])
        self.assertEqual(path_bfs1, [0, 1, 2, 3, 4, 5])
        self.assertEqual(path_dfs2, [2, 3, 4, 5])
        self.assertEqual(path_bfs2, [2, 3, 4, 5])
        self.assertEqual(path_dfs3, [2, 1])
        self.assertEqual(path_bfs3, [2, 1])
        self.assertEqual(path_dfs4, [1])
        self.assertEqual(path_bfs4, [1])

    def test_directed_graph(self):
        g = GraphSearchAlgorithms(vertex_count=6, edges=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], oriented=True)
        path_dfs1 = dfs(g, 0, 5)
        path_bfs1 = bfs(g, 0, 5)
        path_dfs2 = dfs(g, 5, 2)
        path_bfs2 = bfs(g, 5, 2)
        path_dfs3 = dfs(g, 2, 1)
        path_bfs3 = bfs(g, 2, 1)
        path_dfs4 = dfs(g, 1, 1)
        path_bfs4 = bfs(g, 1, 1)
        self.assertEqual(path_dfs1, [0, 1, 2, 3, 4, 5])
        self.assertEqual(path_bfs1, [0, 1, 2, 3, 4, 5])
        self.assertEqual(path_dfs2, None)
        self.assertEqual(path_bfs2, None)
        self.assertEqual(path_dfs3, None)
        self.assertEqual(path_bfs3, None)
        self.assertEqual(path_dfs4, [1])
        self.assertEqual(path_bfs4, [1])

    def test_dijkstra_not_work_with_negative_weight(self):
        g = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 2, -2), (0, 1, -1), (2, 1, 1)], oriented=True)
        self.assertEqual(dijkstra(g, 0), None)

    def test_floyd_work_with_negative_weight(self):
        g = WeightedGraphSearchAlgorithms(vertex_count=4, edges=[(0, 1, -10), (0, 2, 9), (2, 3, -1)], oriented=True)
        self.assertEqual(floyd(g)[0][1], -10)
        self.assertEqual(floyd(g)[0][2], 9)
        self.assertEqual(floyd(g)[0][3], 8)

    def test_weighted_graph_search_algorithms(self):
        g1 = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 2, 1), (0, 1, 5), (2, 1, 1)], oriented=True)
        self.assertEqual(floyd(g1)[0][0], 0)
        self.assertEqual(floyd(g1)[0][1], 2)
        self.assertEqual(floyd(g1)[0][2], 1)
        self.assertEqual(dijkstra(g1, 0)[1], 2)
        self.assertEqual(dijkstra(g1, 0)[2], 1)

        g2 = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 1, 1000), (1, 0, 5), (1, 2, 1)], oriented=False)
        self.assertEqual(dijkstra(g2, 0)[1], 5)
        self.assertEqual(dijkstra(g2, 0)[2], 6)
        self.assertEqual(floyd(g2)[0][1], 5)
        self.assertEqual(floyd(g2)[0][2], 6)

        g3 = WeightedGraphSearchAlgorithms(vertex_count=3, edges=[(0, 1, 1000), (1, 0, 5), (1, 2, 1)], oriented=True)
        self.assertEqual(dijkstra(g3, 0)[1], 1000)
        self.assertEqual(dijkstra(g3, 0)[2], 1001)
        self.assertEqual(floyd(g3)[0][1], 1000)
        self.assertEqual(floyd(g3)[0][2], 1001)

    def test_tree_builder(self):
        for i in range(1, 100):
            graphs = [graph_random_builder.get_tree_without_negative_edges(i * 2, False),
                      graph_random_builder.get_tree_without_negative_edges(i * 2, True),
                      graph_random_builder.get_tree_with_negative_edges(i * 2)]
            for j in graphs:
                self.assertEqual(len(j), i * 2 - 1)
                self.assertEqual(is_graph_connected(i * 2, j), True)


if __name__ == '__main__':
    unittest.main()
