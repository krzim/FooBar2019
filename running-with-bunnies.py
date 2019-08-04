"""
Running with Bunnies
====================

You and your rescued bunny prisoners need to get out of this collapsing death trap of a space station - and fast!
Unfortunately, some of the bunnies have been weakened by their long imprisonment and can't run very fast. Their friends
are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have
begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can
and get through the bulkheads before they close.

The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a
square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ...,
last bunny, and the bulkhead in that order. The order of the rows follows the same pattern
(start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at
 the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies
  you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You
  can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave - you
  can move to and from the bulkhead to pick up additional bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with the space station's security
checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and
if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to
reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is
traversed, the same amount of time is used or added.

Write a function of the form answer(times, time_limit) to calculate the most bunnies you can pick up and which bunnies
they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of
bunnies of the same size, return the set of bunnies with the lowest prisoner IDs (as indexes) in sorted order. The
bunnies are represented as a sorted list by prisoner ID, with the first bunny being 0. There are at most 5 bunnies, and
time_limit is a non-negative integer that is at most 999.

For instance, in the case of
[
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the
bulkhead door exit respectively. You could take the path:

Start End Delta Time Status
    -   0     -    1 Bulkhead initially open
    0   4    -1    2
    4   2     2    0
    2   4    -1    1
    4   3     2   -1 Bulkhead closes
    3   4    -1    0 Bulkhead reopens; you and the bunnies exit

With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so
the answer is [1, 2].

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) times = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
    (int) time_limit = 3
Output:
    (int list) [0, 1]

Inputs:
    (int) times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
    (int) time_limit = 1
Output:
    (int list) [1, 2]
"""
import itertools
from collections import defaultdict, deque


def floyd_warshall(graph):
    for k, i, j in itertools.product(range(len(graph)), repeat=3):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


def bfs(graph, start, end):
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
    paths = sorted(bfs(G, 0, n - 1), key=lambda x: len(x), reverse=True)

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


if __name__ == "__main__":
    assert solution([[0, 2, 2, 2, -1],
                     [9, 0, 2, 2, -1],
                     [9, 3, 0, 2, -1],
                     [9, 3, 2, 0, -1],
                     [9, 3, 2, 2, 0]], 1) == [1, 2]

    assert solution([[0, 1, 1, 1, 1],
                     [1, 0, 1, 1, 1],
                     [1, 1, 0, 1, 1],
                     [1, 1, 1, 0, 1],
                     [1, 1, 1, 1, 0]], 3) == [0, 1]
