import os
import datetime
import statistics
from graphs_class import GraphSearchAlgorithms, WeightedGraphSearchAlgorithms
#from memory_profiler import memory_usage
import graph_random_builder
from floyd_algorithm import floyd
from dijkstra_algorithm import dijkstra
from dfs_algorithm import dfs
from bfs_algorithm import bfs

os.environ["PATH"] += os.pathsep + 'D:/Graphviz/bin/'

# weighted graphs
# w_first_test_graph = WeightedGraphSearchAlgorithms(vertex_count=500,
#                                                    edges=graph_random_builder.get_random_graph(500, True, False),
#                                                    oriented=False)  # random oriented
# w_second_test_graph = WeightedGraphSearchAlgorithms(vertex_count=500,
#                                                     edges=graph_random_builder.get_random_graph(500, True, False),
#                                                     oriented=True)  # random non-oriented
# w_third_test_graph = WeightedGraphSearchAlgorithms(vertex_count=500,
#                                                    edges=graph_random_builder.get_weighted_chain(500),
#                                                    oriented=False)  # chain
w_fourth_test_graph = WeightedGraphSearchAlgorithms(vertex_count=100,
                                                    edges=graph_random_builder.get_dense_weighted_graph(100),
                                                    oriented=True)  # dense

# non-weighted graphs
# first_test_graph = GraphSearchAlgorithms(vertex_count=500,
#                                          edges=graph_random_builder.get_random_graph(500, False, False),
#                                          oriented=False)  # random oriented
# second_test_graph = GraphSearchAlgorithms(vertex_count=500,
#                                           edges=graph_random_builder.get_random_graph(500, False, False),
#                                           oriented=True)  # random non-oriented
# third_test_graph = GraphSearchAlgorithms(vertex_count=500,
#                                          edges=graph_random_builder.get_chain(500),
#                                          oriented=False)  # chain
fourth_test_graph = GraphSearchAlgorithms(vertex_count=100,
                                          edges=graph_random_builder.get_dense_graph(100),
                                          oriented=True)  # dense
start_count = 100

if __name__ == '__main__':
    # Dijkstra tests
    # d_time_1 = datetime.datetime.now()
    # d_path_1 = dijkstra(w_first_test_graph, 0)
    # d_time_1 = datetime.datetime.now() - d_time_1
    # #d_memory_1 = memory_usage(dijkstra(w_first_test_graph, 0))
    #
    # d_time_2 = datetime.datetime.now()
    # d_path_2 = dijkstra(w_second_test_graph, 0)
    # d_time_2 = datetime.datetime.now() - d_time_2
    # #d_memory_2 = memory_usage(dijkstra(w_second_test_graph, 0))
    #
    # d_time_3 = datetime.datetime.now()
    # d_path_3 = dijkstra(w_third_test_graph, 0)
    # d_time_3 = datetime.datetime.now() - d_time_3
    # #d_memory_3 = memory_usage(dijkstra(w_third_test_graph, 0))

    d_array = []
    d_sum = 0
    for _ in range(start_count):
        d_time_4 = datetime.datetime.now()
        d_path_4 = dijkstra(w_fourth_test_graph, 0)
        d_time_4 = datetime.datetime.now() - d_time_4
        d_array.append(d_time_4.total_seconds())
    for i in range(len(d_array)):
        d_sum += d_array[i]
    d_average = d_sum / len(d_array)

    d_std = statistics.stdev(d_array)
    #d_memory_4 = memory_usage(dijkstra(w_fourth_test_graph, 0))

    # Floyd tests
    # f_time_1 = datetime.datetime.now()
    # f_path_1 = floyd(w_first_test_graph)
    # f_time_1 = datetime.datetime.now() - f_time_1
    # #f_memory_1 = memory_usage(floyd(w_first_test_graph))
    #
    # f_time_2 = datetime.datetime.now()
    # f_path_2 = floyd(w_second_test_graph)
    # f_time_2 = datetime.datetime.now() - f_time_2
    # #f_memory_2 = memory_usage(floyd(w_second_test_graph))
    #
    # f_time_3 = datetime.datetime.now()
    # f_path_3 = floyd(w_third_test_graph)
    # f_time_3 = datetime.datetime.now() - f_time_3
    # #f_memory_3 = memory_usage(floyd(w_third_test_graph))

    f_array = []
    f_sum = 0
    for _ in range(start_count):
        f_time_4 = datetime.datetime.now()
        f_path_4 = floyd(w_fourth_test_graph)
        f_time_4 = datetime.datetime.now() - f_time_4
        f_array.append(f_time_4.total_seconds())
    for i in range(len(f_array)):
        f_sum += f_array[i]
    f_average = f_sum / len(f_array)
    f_std = statistics.stdev(f_array)
    #f_memory_4 = memory_usage(floyd(w_fourth_test_graph))

    # DFS tests
    # dfs_time_1 = datetime.datetime.now()
    # dfs_path_1 = dfs(first_test_graph, 0, 499)
    # dfs_time_1 = datetime.datetime.now() - dfs_time_1
    # #dfs_memory_1 = memory_usage(dfs(first_test_graph, 0, 499))
    #
    # dfs_time_2 = datetime.datetime.now()
    # dfs_path_2 = dfs(second_test_graph, 0, 499)
    # dfs_time_2 = datetime.datetime.now() - dfs_time_2
    # #dfs_memory_2 = memory_usage(dfs(second_test_graph, 0, 499))
    #
    # dfs_time_3 = datetime.datetime.now()
    # dfs_path_3 = dfs(third_test_graph, 0, 499)
    # dfs_time_3 = datetime.datetime.now() - dfs_time_3
    # #dfs_memory_3 = memory_usage(dfs(third_test_graph, 0, 499))

    dfs_array = []
    dfs_sum = 0
    for _ in range(start_count):
        dfs_time_4 = datetime.datetime.now()
        dfs_path_4 = dfs(fourth_test_graph, 0, 99)
        dfs_time_4 = datetime.datetime.now() - dfs_time_4
        dfs_array.append(dfs_time_4.total_seconds())
    for i in range(len(dfs_array)):
        dfs_sum += dfs_array[i]
    dfs_average = dfs_sum / len(dfs_array)
    dfs_std = statistics.stdev(dfs_array)
    #dfs_memory_4 = memory_usage(dfs(fourth_test_graph, 0, 99))

    # BFS tests

    # bfs_time_1 = datetime.datetime.now()
    # bfs_path_1 = bfs(first_test_graph, 0, 499)
    # bfs_time_1 = datetime.datetime.now() - bfs_time_1
    # #bfs_memory_1 = memory_usage(bfs(first_test_graph, 0, 499))
    #
    # bfs_time_2 = datetime.datetime.now()
    # bfs_path_2 = bfs(second_test_graph, 0, 499)
    # bfs_time_2 = datetime.datetime.now() - bfs_time_2
    # #bfs_memory_2 = memory_usage(bfs(second_test_graph, 0, 499))
    #
    # bfs_time_3 = datetime.datetime.now()
    # bfs_path_3 = bfs(third_test_graph, 0, 499)
    # bfs_time_3 = datetime.datetime.now() - bfs_time_3
    # #bfs_memory_3 = memory_usage(bfs(third_test_graph, 0, 499))

    bfs_array = []
    bfs_sum = 0
    for _ in range(start_count):
        bfs_time_4 = datetime.datetime.now()
        bfs_path_4 = bfs(fourth_test_graph, 0, 99)
        bfs_time_4 = datetime.datetime.now() - bfs_time_4
        bfs_array.append(bfs_time_4.total_seconds())
    for i in range(len(bfs_array)):
        bfs_sum += bfs_array[i]
    bfs_average = bfs_sum / len(bfs_array)
    bfs_std = statistics.stdev(bfs_array)
    #bfs_memory_4 = memory_usage(bfs(fourth_test_graph, 0, 99))

    # print('-' * 100)
    # print('First Test')
    # print('Dijkstra')
    # print('time usage: ', d_time_1)
    # #print('memory usage: ', d_memory_1)
    # print('Floyd')
    # print('time usage: ', f_time_1)
    # #print('memory usage: ', f_memory_1)
    # print('BFS')
    # print('time usage: ', bfs_time_1)
    # #print('memory usage: ', bfs_memory_1)
    # print('DFS')
    # print('time usage: ', dfs_time_1)
    # #print('memory usage: ', dfs_memory_1)
    #
    # print('-' * 100)
    # print('Second Test')
    # print('Dijkstra')
    # print('time usage: ', d_time_2)
    # #print('memory usage: ', d_memory_2)
    # print('Floyd')
    # print('time usage: ', f_time_2)
    # #print('memory usage: ', f_memory_2)
    # print('BFS')
    # print('time usage: ', bfs_time_2)
    # #print('memory usage: ', bfs_memory_2)
    # print('DFS')
    # print('time usage: ', dfs_time_2)
    # #print('memory usage: ', dfs_memory_2)
    #
    # print('-' * 100)
    # print('Third Test')
    # print('Dijkstra')
    # print('time usage: ', d_time_3)
    # #print('memory usage: ', d_memory_3)
    # print('Floyd')
    # print('time usage: ', f_time_3)
    # #print('memory usage: ', f_memory_3)
    # print('BFS')
    # print('time usage: ', bfs_time_3)
    # #print('memory usage: ', bfs_memory_3)
    # print('DFS')
    # print('time usage: ', dfs_time_3)
    # #print('memory usage: ', dfs_memory_3)
    # print('-' * 100)

    print('Fourth Test')
    print('Dijkstra')
    print('time usage of every test: ', d_array)
    print('average time: ', d_average)
    print('std: ', d_std)
    #print('memory usage: ', d_memory_4)
    print('Floyd')
    print('time usage of every test: ', f_array)
    print('average time: ', f_average)
    print('std: ', f_std)
    #print('memory usage: ', f_memory_4)
    print('BFS')
    print('time usage of every test: ', bfs_array)
    print('average time: ', bfs_average)
    print('std: ', bfs_std)
    #print('memory usage: ', bfs_memory_4)
    print('DFS')
    print('time usage of every test: ', dfs_array)
    print('average time: ', dfs_average)
    print('std: ', dfs_std)
    #print('memory usage: ', dfs_memory_4)
    print('-' * 100)
