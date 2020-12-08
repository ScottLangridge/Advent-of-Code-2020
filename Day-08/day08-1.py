from GameConsole import GameConsole


def main(raw_input):
    input_program = parse_input(raw_input)
    game_console = GameConsole(input_program)
    result = game_console.exec()

    return result[1]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    instructions = [i.split(' ') for i in raw_input.splitlines()]
    return [[i[0], int(i[1])] for i in instructions]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
