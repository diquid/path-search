import os
import datetime
from memory_profiler import memory_usage
import graph_random_builder
from floyd_algorithm import floyd
from dijkstra_algorithm import dijkstra
from dfs_algorithm import dfs
from bfs_algorithm import bfs

os.environ["PATH"] += os.pathsep + 'D:/Graphviz/bin/'

first_test_graph = graph_random_builder.get_chain(1000000)  # chain
second_test_graph = graph_random_builder.get_dense_graph(10000)  # dense graph
third_test_graph = graph_random_builder.get_random_graph(1000000, False, False)  # random graph
fourth_test_graph = graph_random_builder.get_tree_without_negative_edges(1000000, False)  # tree


if __name__ == '__main__':
    # Dijkstra tests
    d_time_1 = datetime.datetime.now()
    d_path_1 = dijkstra(first_test_graph, 0)
    d_time_1 = datetime.datetime.now() - d_time_1
    d_memory_1 = memory_usage(dijkstra(first_test_graph, 0))

    d_time_2 = datetime.datetime.now()
    d_path_2 = dijkstra(second_test_graph, 0)
    d_time_2 = datetime.datetime.now() - d_time_2
    d_memory_2 = memory_usage(dijkstra(second_test_graph, 0))

    d_time_3 = datetime.datetime.now()
    d_path_3 = dijkstra(third_test_graph, 0)
    d_time_3 = datetime.datetime.now() - d_time_3
    d_memory_3 = memory_usage(dijkstra(third_test_graph, 0))

    d_time_4 = datetime.datetime.now()
    d_path_4 = dijkstra(fourth_test_graph, 0)
    d_time_4 = datetime.datetime.now() - d_time_4
    d_memory_4 = memory_usage(dijkstra(fourth_test_graph, 0))

    # Floyd tests
    f_time_1 = datetime.datetime.now()
    f_path_1 = floyd(first_test_graph)
    f_time_1 = datetime.datetime.now() - f_time_1
    f_memory_1 = memory_usage(floyd(first_test_graph))

    f_time_2 = datetime.datetime.now()
    f_path_2 = floyd(second_test_graph)
    f_time_2 = datetime.datetime.now() - f_time_2
    f_memory_2 = memory_usage(floyd(second_test_graph))

    f_time_3 = datetime.datetime.now()
    f_path_3 = floyd(third_test_graph)
    f_time_3 = datetime.datetime.now() - f_time_3
    f_memory_3 = memory_usage(floyd(third_test_graph))

    f_time_4 = datetime.datetime.now()
    f_path_4 = floyd(third_test_graph)
    f_time_4 = datetime.datetime.now() - f_time_4
    f_memory_4 = memory_usage(floyd(third_test_graph))

    # DFS tests
    dfs_time_1 = datetime.datetime.now()
    dfs_path_1 = dfs(first_test_graph, 0, 999999)
    dfs_time_1 = datetime.datetime.now() - dfs_time_1
    dfs_memory_1 = memory_usage(dfs(first_test_graph, 0, 999999))

    dfs_time_2 = datetime.datetime.now()
    dfs_path_2 = dfs(second_test_graph, 0, 9999)
    dfs_time_2 = datetime.datetime.now() - dfs_time_2
    dfs_memory_2 = memory_usage(dfs(second_test_graph, 0, 9999))

    dfs_time_3 = datetime.datetime.now()
    dfs_path_3 = dfs(third_test_graph, 0, 99999)
    dfs_time_3 = datetime.datetime.now() - dfs_time_3
    dfs_memory_3 = memory_usage(dfs(third_test_graph, 0, 99999))

    dfs_time_4 = datetime.datetime.now()
    dfs_path_4 = dfs(fourth_test_graph, 0, 999999)
    dfs_time_4 = datetime.datetime.now() - dfs_time_4
    dfs_memory_4 = memory_usage(dfs(fourth_test_graph, 0, 999999))

    # BFS tests

    bfs_time_1 = datetime.datetime.now()
    bfs_path_1 = bfs(first_test_graph, 0, 999999)
    bfs_time_1 = datetime.datetime.now() - bfs_time_1
    bfs_memory_1 = memory_usage(bfs(first_test_graph, 0, 999999))

    bfs_time_2 = datetime.datetime.now()
    bfs_path_2 = bfs(second_test_graph, 0, 9999)
    bfs_time_2 = datetime.datetime.now() - bfs_time_2
    bfs_memory_2 = memory_usage(bfs(second_test_graph, 0, 9999))

    bfs_time_3 = datetime.datetime.now()
    bfs_path_3 = bfs(third_test_graph, 0, 99999)
    bfs_time_3 = datetime.datetime.now() - bfs_time_3
    bfs_memory_3 = memory_usage(bfs(third_test_graph, 0, 99999))

    bfs_time_4 = datetime.datetime.now()
    bfs_path_4 = bfs(fourth_test_graph, 0, 999999)
    bfs_time_4 = datetime.datetime.now() - bfs_time_4
    bfs_memory_4 = memory_usage(bfs(fourth_test_graph, 0, 999999))

    print('-' * 100)
    print('First Test')
    print('Dijkstra')
    print('time usage: ', d_time_1)
    print('memory usage: ', d_memory_1)
    print('Floyd')
    print('time usage: ', f_time_1)
    print('memory usage: ', f_memory_1)
    print('BFS')
    print('time usage: ', bfs_time_1)
    print('memory usage: ', bfs_memory_1)
    print('DFS')
    print('time usage: ', dfs_time_1)
    print('memory usage: ', dfs_memory_1)

    print('-' * 100)
    print('Second Test')
    print('Dijkstra')
    print('time usage: ', d_time_2)
    print('memory usage: ', d_memory_2)
    print('Floyd')
    print('time usage: ', f_time_2)
    print('memory usage: ', f_memory_2)
    print('BFS')
    print('time usage: ', bfs_time_2)
    print('memory usage: ', bfs_memory_2)
    print('DFS')
    print('time usage: ', dfs_time_2)
    print('memory usage: ', dfs_memory_2)

    print('-' * 100)
    print('Third Test')
    print('Dijkstra')
    print('time usage: ', d_time_3)
    print('memory usage: ', d_memory_3)
    print('Floyd')
    print('time usage: ', f_time_3)
    print('memory usage: ', f_memory_3)
    print('BFS')
    print('time usage: ', bfs_time_3)
    print('memory usage: ', bfs_memory_3)
    print('DFS')
    print('time usage: ', dfs_time_3)
    print('memory usage: ', dfs_memory_3)
    print('-' * 100)

    print('-' * 100)
    print('Fourth Test')
    print('Dijkstra')
    print('time usage: ', d_time_4)
    print('memory usage: ', d_memory_4)
    print('Floyd')
    print('time usage: ', f_time_4)
    print('memory usage: ', f_memory_4)
    print('BFS')
    print('time usage: ', bfs_time_4)
    print('memory usage: ', bfs_memory_4)
    print('DFS')
    print('time usage: ', dfs_time_4)
    print('memory usage: ', dfs_memory_4)
    print('-' * 100)
