def main(raw_input):
    adaptors = parse_input(raw_input)
    adaptors.insert(0, 0)

    i = 1
    differences = []
    while i < len(adaptors):
        differences.append(adaptors[i] - adaptors[i - 1])
        i += 1
    differences.append(3)

    variable_chains = []
    i = 0
    last_fixed = 0
    while i < len(differences):
        if differences[i] == 3:
            variable_chains.append(adaptors[last_fixed:i + 1])
            last_fixed = i + 1
        i += 1

    variable_chains = [chain for chain in variable_chains if len(chain) >= 3]

    variations = 1
    for chain in variable_chains:
        variations *= count_valid_permutations(chain[1:], [chain[0]], max(chain))

    print(variations)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return sorted([int(i) for i in raw_input.splitlines()])


def count_valid_permutations(adaptors, current_chain, target_jolts):
    valid_count = 0
    while True:
        next_adaptor = adaptors.pop(0)
        if next_adaptor > current_chain[-1] + 3:
            return valid_count
        elif next_adaptor == target_jolts:
            return valid_count + 1
        else:
            valid_count += count_valid_permutations(adaptors[:], current_chain[:] + [next_adaptor], target_jolts)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
