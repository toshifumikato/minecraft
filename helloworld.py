from mcpi import minecraft,block
from mazelib import Maze
from mazelib.generate.Prims import Prims

N = 7
M = 10

def put_maze_block(mc, mark, x_pos, z_pos):
    if mark == '#':
        mc.setBlocks(
            x_pos, 0, z_pos,
            x_pos, 3, z_pos,
            block.IRON_BLOCK
        )

def create_ceiling(mc, x_pos, y_pos, z_pos):
    mc.setBlocks(
        -3, y_pos, -3,
        x_pos, y_pos, z_pos,
        block.IRON_BLOCK
    )

def put_torch(mc, x_pos, y_pos, z_pos):
    mc.setBlocks(
        x_pos, y_pos, z_pos,
        x_pos, y_pos, z_pos,
        block.TORCH
    )

def main():
    mc = minecraft.Minecraft.create()
    mc.player.setPos(0, 1, 0)
    mc.setBlocks(
        -3, 0, -3,
        50, 50, 50,
        block.AIR
    )

    mc.setBlocks(
        -3, 0, -3,
        50, 0, 50,
        block.DIAMOND_BLOCK)

    mc.player.setPos(0, 9, 0)

    mz = Maze()
    mz.generator = Prims(N, M)
    mz.generate()

    mz.start = (0, 1)
    mz.end = (N * 2, M * 2 - 10)

    maze_str = str(mz)
    maze_list = maze_str.split('\n')

    for z, mark_list in enumerate(maze_list):
        for x, mark in enumerate(mark_list):
            put_maze_block(mc, mark, x, z)

    create_ceiling(mc, 50, 8, 50)
    mc.setBlocks(
        -3, 8, -3,
        10, 8, -1,
        block.AIR
    )

    mc.setBlocks(
        -3, 3, -3,
        50, 3, 50,
        block.TORCH
    )

if __name__ == '__main__':
    main()


