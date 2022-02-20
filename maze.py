from mazelib import Maze
from mazelib.generate.Prims import Prims

N = 7
M = 10

mz = Maze()
mz.generator = Prims(N, M)
mz.generate()

mz.start = (0, 1)
mz.end = (N * 2, M * 2 - 10)

maze_str = str(mz)
maze_list = maze_str.split('\n')

for z, mark_list in enumerate(maze_list):
    for x, mark in enumerate(mark_list):
        print(x, z, mark)
