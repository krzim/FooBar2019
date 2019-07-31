import itertools
from collections import defaultdict, deque


def floyd_warshall(graph):
    for k, i, j in itertools.product(range(len(graph)), repeat=3):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


def BFS(graph, start, end):
    paths = []
    q = deque([[start]])
    while len(q) > 0:
        tmp_path = q.pop()
        last_node = tmp_path[len(tmp_path)-1]
        if last_node == end:
            paths.append(tmp_path)
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                new_path = tmp_path + [link_node]
                q.appendleft(new_path)
    return paths


def solution(times, time_limit):
    n = len(times)

    # Build a graph for BFS traversal
    G = defaultdict(set)
    for edge in list(itertools.product(range(n), range(n))):
        G[edge[0]].add(edge[1])

    # Get the all pairs shortest paths
    min_dists = floyd_warshall(times)

    # Checks to see if we found a negative cycle. If a node can get to itself in less than 0 time then we hit a cycle
    if any([min_dists[i][i] < 0 for i in range(n)]):
        return list(range(n - 2))

    # Find all simple paths between the start and bulkhead
    paths = sorted(BFS(G, 0, n - 1), key=lambda x: len(x), reverse=True)

    # Check the paths from longest to shortest for one that works and then return it
    for path in paths:
        time = 0
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            time += min_dists[u][v]
        if time <= time_limit:
            return sorted([n - 1 for n in path[1:-1]])

    return []  # guess we didn't find any valid paths...poor bun buns




# out = solution([[0, 2, 2, 2, -1],
#                 [9, 0, 2, 2, -1],
#                 [9, 3, 0, 2, -1],
#                 [9, 3, 2, 0, -1],
#                 [9, 3, 2, 2, 0]], 1)
# assert out == [1, 2]
#
# out = solution([[0, 1, 1, 1, 1],
#                 [1, 0, 1, 1, 1],
#                 [1, 1, 0, 1, 1],
#                 [1, 1, 1, 0, 1],
#                 [1, 1, 1, 1, 0]], 3)
# assert out == [0, 1]
#
# out = solution([[0, 2, 2, 2, -1],
#                 [9, 0, 2, 2, -1],
#                 [9, 3, 0, 2, -1],
#                 [9, 3, 2, 0, -1],
#                 [9, 3, 2, 0, 0]], 1)
#
# assert out == [0, 1, 2]

# def solution(time, time_limit):
#     N = len(time[0])
#     d = [[10000 for y in range(N)] for x in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if i == j:
#                 d[i][j] = 0
#
#     for m in range(N):
#         for k in range(N-1):
#             for i in range(N):
#                 for j in range(N):
#                     d[m][i] = min(d[m][i], d[m][j] + time[j][i])
#     from itertools import combinations, permutations
#     input = range(1, N-1)
#     subsets = sum([map(list, combinations(input, i)) for i in range(N)], [])
#
#     def getSum(subset):
#         prev, add = 0, 0
#         for s in subset:
#             add += d[prev][s]
#             prev = s
#         return add + d[prev][N-1]
#
#     print d
#     result = []
#     for subset in subsets:
#         for ssubset in permutations(subset):
#             time_taken = getSum(ssubset)
#             if len(ssubset) > 0 and time_taken < 0 :
#                 return range(0, N-2)
#             if time_taken <= time_limit and len(subset) > len(result):
#                 result = subset
#     return sorted([r-1 for r in result])

res = solution([
    [0, 2, 9, 9, 1],
    [9, 0, 9, 2, 1],
    [9, 9, 0, 9, -1],
    [9, 9, 9, 0, -4],
    [9, 9, 9, 9, 0]], -20)
assert res == []

res = solution([
    [0, 2, 2, 2, -1],
    [9, 0, 2, 2, -1],
    [9, 3, 0, 2, -1],
    [9, 3, 2, 0, -1],
    [9, 3, 2, 2, 0]], 1)
assert res == [1, 2], res

res = solution([
    [0 , 15, 19, 10, -1, 12,  4],
    [7 ,  0, 19,  4, 19, 17,  7],
    [15,  8,  0, 14,  8,  4,  3],
    [10, 14,  6,  0,  0,  5,  9],
    [18,  8,  4,  0,  0, 12, 16],
    [0 , 13,  1, -1, 12,  0,  4],
    [8 ,  5,  2, 11, 12, 16,  0]], 7)
assert res == [1, 2, 3]

res = solution([ # Fail
    [0 ,  0, 19, 19, 19, 19, 19],
    [7 ,  0,  0, 19, 19, 17, 19],
    [19, 19,  0,  0,  0,  5, 19],
    [10,  0, 19,  0, 19, 19, 19],
    [19,  0, 19, 19,  0, 19, 19],
    [19, 19, 19, 19, 19,  0,  2],
    [8 ,  6,  6, 11, 12, 16,  0]], 7)
assert res == [0, 1, 2, 3, 4]

res = solution([
    [0, 19, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 19, 0, 1, 1],
    [1, 19, 1, 0, 1],
    [1, 19, 1, 1, 0]], 3)
assert res == [1, 2]

res = solution([
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]], 3)
assert res == [0, 1]

res =  solution([
    [ 0,  3, 82, 91, 15, 24, 77],
    [ 8,  0,  7, 32,  6, 33, 14],
    [66, 98,  0, 62, 59,  5, 39],
    [64, 97,  5,  0, 45, 84, 21],
    [ 3, 33, 81, 24,  0, 53,  5],
    [73, 93, 29,  9, 78,  0, 44],
    [70, 76, 15,  0, 43, 58,  0]], 999)
assert res == [0, 1, 2, 3, 4]

# res = solution([ # Fail
#     [ 0,  1, -2,  3,  2, -1,  0],
#     [-1,  0, -3,  2,  1, -2, -1],
#     [ 2,  3,  0,  5,  4,  1,  2],
#     [-3, -2, -5,  0, -1, -4, -3],
#     [-2, -1, -4,  1,  0, -3, -2],
#     [ 1,  2, -1,  4,  3,  0,  1],
#     [ 0,  1, -2,  3,  2, -1,  0]], 0)
# assert res == [0, 1, 2, 3, 4]

res = solution([
    [0 ,  0, 19, 19, 19, 19, 19],
    [7 ,  0,  0, 19,  0, 17, 19],
    [19, 19,  0,  0, 19,  5, 19],
    [10,  0, 19,  0, 19, 19, 19],
    [19, 19, 19, 19,  0,  0, 19],
    [19,  0, 19, 19, 19, 19,  2],
    [8 ,  6,  6, 11, 12, 16,  0]], 7)
assert res == [0, 1, 2, 3, 4]

res = solution([
    [0, 99, 99, 99, 99, 99, -1],
    [99, 0, 99, 99, 99, 99, 99],
    [99, 99, 0, 99, 99, 99, 99],
    [99, 99, 99, 0, 99, 99, 99],
    [99, 99, 99, 99, 0, 99, 99],
    [99, 99, 99, 99, 0, 0, 99],
    [0, 99, 99, 99, 99, 99, 0]], 1)
assert res == [0, 1, 2, 3, 4], res