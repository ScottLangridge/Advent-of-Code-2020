def main(raw_input):
    instructions = parse_input(raw_input)
    memory = {}
    original_mask = ''
    masks = []

    for i in instructions:
        if i[0] == 'mask':
            original_mask = i[1][0]
            masks = i[1][1:]
        else:
            for mask in masks:
                memory[apply_mask(original_mask, mask, i[0])] = i[1]

    return sum(memory.values())


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    instructions = raw_input.splitlines()
    for i in range(len(instructions)):
        if 'mem' in instructions[i]:
            instructions[i] = parse_address_instruction(instructions[i])
        else:
            instructions[i] = parse_mask_instruction(instructions[i])

    return instructions


def parse_address_instruction(instruction):
    address, value = instruction.split(' = ')
    address = address[4:-1]
    return [int(address), int(value)]


def parse_mask_instruction(instruction):
    str_mask = instruction[-36:]
    variables = str_mask.count('X')
    masks = [str_mask]
    for i in range(2 ** variables):
        bin_i = list(('{0:0' + str(variables) + 'b}').format(i))
        new_mask = ''
        for j in str_mask:
            if j == 'X':
                new_mask = new_mask + bin_i.pop(0)
            else:
                new_mask = new_mask + j
        masks.append(new_mask)
    return 'mask', masks


def apply_mask(original_mask, mask, dev_val):
    bin_val = list(dec_to_binary(dev_val))

    for i in range(len(mask)):
        if original_mask[i] == 'X':
            bin_val[i] = mask[i]
        elif original_mask[i] == '1':
            bin_val[i] = '1'
    return int(''.join(bin_val), 2)


def dec_to_binary(value):
    return '{0:036b}'.format(value)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
