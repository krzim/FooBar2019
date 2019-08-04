"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once
they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as
quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a
deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that
will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just
remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both
to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The
 map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of
 the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod,
where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes
you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0).
The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be
 from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) maze = [[0, 1, 1, 0],
                  [0, 0, 0, 1],
                  [1, 1, 0, 0],
                  [1, 1, 1, 0]]
Output:
    (int) 7

Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 1],
                  [0, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11
"""
from collections import deque


def bfs(src, dest, map_):
    w = len(map_[0])
    h = len(map_)
    src += (1, )
    q = deque([src])
    dist = [[[float("inf"), float("inf")] for i in xrange(w)] for j in xrange(h)]
    dist[0][0][1] = 0
    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while len(q) > 0:
        x, y, wall_flag = q.pop()
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]

            if new_x < 0 or new_x >= h:
                continue
            if new_y < 0 or new_y >= w:
                continue

            if map_[new_x][new_y] == 1:
                if wall_flag and dist[new_x][new_y][wall_flag - 1] == float("inf"):
                    q.appendleft((new_x, new_y, wall_flag - 1))
                    dist[new_x][new_y][wall_flag - 1] = dist[x][y][1] + 1
            else:
                if dist[new_x][new_y][wall_flag] == float("inf"):
                    q.appendleft((new_x, new_y, wall_flag))
                    dist[new_x][new_y][wall_flag] = dist[x][y][wall_flag] + 1

            if (new_x, new_y) == dest:
                return min(dist[h - 1][w - 1])


def solution(map_):
    return bfs((0, 0), (len(map_) - 1, len(map_[0]) - 1), map_) + 1


if __name__ == "__main__":
    assert solution([[0, 1, 1, 0],
                     [0, 0, 0, 1],
                     [1, 1, 0, 0],
                     [1, 1, 1, 0]]) == 7

    assert solution([[0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 1, 1],
                     [0, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0]]) == 11
