def main(raw_input):
    input = [int(x) for x in raw_input.splitlines()]

    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    return i * j * k

    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
