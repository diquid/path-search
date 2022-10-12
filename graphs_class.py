class GraphSearchAlgorithms:

    def __init__(self, vertex_count=0, edges=None, oriented=False):
        if edges is None:
            edges = []
        self.vertex_count = vertex_count
        self.adjacent_vertices = []
        for i in range(vertex_count):
            self.adjacent_vertices.append(set())
        for edge in edges:
            self.adjacent_vertices[edge[0]].add(edge[1])
            if not oriented:
                self.adjacent_vertices[edge[1]].add(edge[0])

    def __int__(self, matrix=None):
        if matrix is None:
            matrix = []
        self.vertex_count = len(matrix)
        self.adjacent_vertices = []
        for i in range(self.vertex_count):
            self.adjacent_vertices.append(set())
        for i in range(self.vertex_count):
            for j in range(self.vertex_count):
                self.adjacent_vertices[i].add(matrix[i][j])

    @staticmethod
    def restore_path(parents, start, end):
        path = list()
        if parents[end] == -1:
            return None
        while end != start:
            path.append(end)
            end = parents[end]
        path.append(start)
        path.reverse()
        return path


class WeightedGraphSearchAlgorithms:

    def __init__(self, vertex_count=0, edges=None, oriented=False):
        if edges is None:
            edges = []
        self.negative_edge = False
        self.vertex_count = vertex_count
        self.adjacent_vertices = []
        for i in range(vertex_count):
            self.adjacent_vertices.append(set())
        for edge in edges:
            self.adjacent_vertices[edge[0]].add((edge[1], edge[2]))
            if not oriented:
                self.adjacent_vertices[edge[1]].add((edge[0], edge[2]))
            if edge[2] < 0:
                self.negative_edge = True

    def __int__(self, matrix=None):
        if matrix is None:
            matrix = []
        self.negative_edge = False
        self.vertex_count = len(matrix)
        self.adjacent_vertices = []
        for i in range(self.vertex_count):
            self.adjacent_vertices.append(set())
        for i in range(self.vertex_count):
            for j in range(self.vertex_count):
                self.adjacent_vertices[i].add((matrix[i][j][0], matrix[i][j][1]))
                if matrix[i][j][1] < 0:
                    self.negative_edge = True
