def main(raw_input):
    group_responses = parse_input(raw_input)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    total_yes_count = 0
    for i in group_responses:
        group_yes_count = 0
        for char in alphabet:
            if char in i:
                group_yes_count += 1
        total_yes_count += group_yes_count

    return total_yes_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split('\n\n')



if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
