def main(raw_input):
    tree_map = parse_input(raw_input)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    tree_count_product = 1
    for i in slopes:
        tree_count_product *= count_trees(tree_map, i[0], i[1])

    return tree_count_product


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    tree_map = []
    for row in raw_input.splitlines():
        row_map = [x == '#' for x in row]
        tree_map.append(row_map)

    return tree_map


def count_trees(tree_map, x_increment, y_increment):
    pattern_width = len(tree_map[0])
    pos_x = 0
    pos_y = 0

    tree_count = 0
    while pos_y < len(tree_map):
        if tree_map[pos_y][pos_x]:
            tree_count += 1

        pos_x = (pos_x + x_increment) % pattern_width
        pos_y += y_increment

    return tree_count


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
