import math

from day20.DecisionTree import DecisionTree
from day20.DecisionTreeNode import DecisionTreeNode
from day20.ImageTile import ImageTile
from day20.State import State


def main(raw_input):
    tiles = parse_input(raw_input)
    root_node = build_root_node(tiles)
    tree = DecisionTree(root_node)
    answer = tree.run()
    return answer.state.corner_product()


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    tile_strings = raw_input.split('\n\n')

    tiles = []
    for tile_string in tile_strings:
        t = ImageTile(tile_string)
        tiles.append(t)

    return tiles


def build_root_node(tiles):
    side_length = int(math.sqrt(len(tiles)))

    initial_tile_matrix = []
    for y in range(side_length):
        row = []
        for x in range(side_length):
            row.append(tiles[y * side_length + x])
        initial_tile_matrix.append(row)

    initial_state = State(initial_tile_matrix)
    return DecisionTreeNode(state=initial_state)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
