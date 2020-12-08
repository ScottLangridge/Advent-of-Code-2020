from GameConsole import GameConsole


def main(raw_input):
    input_program = parse_input(raw_input)

    i = 0
    possible_programs = []
    while i < len(input_program):
        if input_program[i][0] == 'jmp':
            input_program[i][0] = 'nop'
            possible_programs.append([instruction[:] for instruction in input_program])
            input_program[i][0] = 'jmp'
        elif input_program[i][0] == 'nop':
            input_program[i][0] = 'jmp'
            possible_programs.append([instruction[:] for instruction in input_program])
            input_program[i][0] = 'nop'
        i += 1

    for program in possible_programs:
        game_console = GameConsole(program)
        result = game_console.exec()
        if result[0]:
            return result[1]

    return False


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
