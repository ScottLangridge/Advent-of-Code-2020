def main(raw_input):
    seats = parse_input(raw_input)

    new_seats = update_ferry(seats)

    while seats != new_seats:
        seats = new_seats
        new_seats = update_ferry(seats)

    occupied_count = 0
    for row in new_seats:
        for seat in row:
            if seat == '#':
                occupied_count += 1

    return occupied_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    grid = []

    rows = raw_input.splitlines()
    for i in range(len(rows)):
        rows[i] = '.' + rows[i] + '.'
    empty_row = ['.' for i in range(len(rows[0]))]

    grid.append(empty_row)
    grid.extend([list(i) for i in rows])
    grid.append(empty_row)

    return grid


def update_ferry(seats):
    empty_row = ['.' for i in range(len(seats[0]))]
    new_seats = [empty_row]
    for y in range(1, len(seats) - 1):
        row = ['.']
        for x in range(1, len(seats[0]) - 1):
            row.append(update_seat(seats, y, x))
        new_seats.append(row)
        row.append('.')
    new_seats.append(empty_row)
    return new_seats


def update_seat(seats, seat_y, seat_x):
    seat_state = seats[seat_y][seat_x]
    if seat_state == '#':
        occupied = -1
    elif seat_state == 'L':
        occupied = 0
    else:
        return '.'

    for y in range(seat_y - 1, seat_y + 2):
        for x in range(seat_x - 1, seat_x + 2):
            if seats[y][x] == '#':
                occupied += 1

    if seat_state == '#' and occupied >= 4:
        return 'L'
    elif seat_state == 'L' and occupied == 0:
        return '#'
    else:
        return seat_state


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
