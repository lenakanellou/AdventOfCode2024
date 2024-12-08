import sys

def main():

    if len(sys.argv) > 2:
        print('Usage: python script.py <filename>')
        sys.exit(1)

    filename = sys.argv[1]
    map = []
    guard_position = [0, 0]
    next_position = [0, 0]
    guard_in_area = True
    guard_steps = 0
    # unique_positions = set()
    possible_loops = 0
    positions = {}
    x_dim = 0
    y_dim = 0

    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            line = list(line.strip())
            matches = [(i,e) for i, e in enumerate(line) if e in ('^', 'v', '>', '<')]
            if len(matches) > 1:
                print('THERE\'S MORE THAN ONE GUARD?!')
                sys.exit(1)
            if matches != []:
                guard_position[0] = row
                guard_position[1], guard_direction = matches[0]
                # print(f'Line {row} contains the guard at index {guard_position[1]}. Guard is facing {guard_direction}')
            map.append(line)

    x_dim = len(map[0])
    y_dim = len(map)

    print(f'Area is {x_dim} by {y_dim} characters.')

    next_position[0] = guard_position[0]
    next_position[1] = guard_position[1]
    print(f'Initially, guard in position {next_position[0]}x{next_position[1]}')
    # unique_positions.add((guard_position[0], guard_position[1]))
    positions[(guard_position[0], guard_position[1])] = guard_direction

    while guard_in_area is True:
        if guard_direction == '^':
            next_position[0] -= 1
        elif guard_direction == '>':
            next_position[1] += 1
        elif guard_direction == 'v':
            next_position[0] += 1
        elif guard_direction == '<':
            next_position[1] -= 1
        else:
            print(f'Illegal guard direction! {guard_direction}')
            sys.exit(1)

        if next_position[0] < 0 or next_position[0] >= x_dim \
            or next_position[1] < 0 or next_position[1] >= y_dim:
            guard_in_area = False
            print(f'Guard out of area! Steps required: {guard_steps}. Distinct positions visited: {len(positions)}')
        else:
            if map[next_position[0]][next_position[1]] == '#':
            #change direction
                if guard_direction == '^':
                    guard_direction = '>'
                elif guard_direction == '>':
                    guard_direction = 'v'
                elif guard_direction == 'v':
                    guard_direction = '<'
                elif guard_direction == '<':
                    guard_direction = '^'
                else:
                    print(f'Illegal guard direction! {guard_direction}')
                    sys.exit(1)

                print(f'Found # at position {next_position[0]}x{next_position[1]}. Current position is {guard_position[0]}x{guard_position[1]}. Changing direction to {guard_direction}')
                next_position[0] = guard_position[0]
                next_position[1] = guard_position[1]
            else:
                guard_position[0] = next_position[0]
                guard_position[1] = next_position[1]
                # unique_positions.add((guard_position[0], guard_position[1]))
                if (guard_position[0], guard_position[1]) not in positions:
                    positions[(guard_position[0], guard_position[1])] = guard_direction

                    if (guard_position[0]-2, guard_position[1]) in positions \
                    and map[guard_position[0]-1][guard_position[1]] != '#':

                        prev_direction = positions[(guard_position[0]-2, guard_position[1])]
                        if (prev_direction == '^' and guard_direction == '<') \
                        or (prev_direction == '<' and guard_direction == 'v') \
                        or (prev_direction == 'v' and guard_direction == '>') \
                        or (prev_direction == '>' and guard_direction == '^'): \
                            possible_loops += 1

                else:
                    prev_direction = positions[(guard_position[0], guard_position[1])]
                    if (prev_direction == '^' and guard_direction == '<') \
                    or (prev_direction == '<' and guard_direction == 'v') \
                    or (prev_direction == 'v' and guard_direction == '>') \
                    or (prev_direction == '>' and guard_direction == '^'): \
                        possible_loops += 1
                guard_steps += 1


    print(f'Possible loops: {possible_loops}')

    return

if __name__ == "__main__":
    main()