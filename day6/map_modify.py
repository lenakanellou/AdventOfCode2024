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
    unique_positions = set()
    x_dim = 0
    y_dim = 0
    obstacle_queue = []
    possible_loops = 0

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
    unique_positions.add((guard_position[0], guard_position[1]))

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
            print(f'Guard out of area! Steps required: {guard_steps}. Distinct positions visited: {len(unique_positions)}')
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
                obstacle_queue.append((next_position[0], next_position[1]))
                next_position[0] = guard_position[0]
                next_position[1] = guard_position[1]
            else:
                guard_position[0] = next_position[0]
                guard_position[1] = next_position[1]
                unique_positions.add((guard_position[0], guard_position[1]))
                guard_steps += 1

    loop_positions = []
    for i in range(0, len(obstacle_queue)-2):
        one = obstacle_queue[i]
        two = obstacle_queue[i+1]
        three = obstacle_queue[i+2]
        print(f'Obstacles to be examined: {one}, {two}, and {three}, for obstacles in queue order {i}, {i+1}, {i+2}.')
        # check for clockwise loop
        if one[0] == two[0]-1 and two[1] == three[1]+1:
            print(f'Checking whether ({three[0]-1}, {one[1]-1}) in guard\'s route.')
            if (three[0]-1, one[1]-1) in unique_positions:
                print(f'Loop position found! ({three[0]-1}, {one[1]-1})')
                loop_positions.append((three[0]-1, one[1]-1))
                possible_loops += 1
        elif one[1] == two[1]+1 and two[0] == three[0]+1:
            if (one[0]-1, three[1]+1) in unique_positions:
                print(f'Loop position found! ({one[0]-1}, {three[1]+1})')
                loop_positions.append((one[0]-1, three[1]+1))
                possible_loops += 1
        elif one[0] == two[0]+1 and two[1] == three[1]-1:
            if (three[0]+1, one[1]+1) in unique_positions:
                print(f'Loop position found! ({three[0]+1}, {one[1]+1})')
                loop_positions.append((three[0]+1, one[1]+1))
                possible_loops += 1
        elif one[1] == two[1]-1 and two[0] == three[0]-1:
            if (one[0]+1, three[1]-1) in unique_positions:
                print(f'Loop position found! ({one[0]+1}, {three[1]-1})')
                loop_positions.append((one[0]+1, three[1]-1))
                possible_loops += 1

        # check for counter-clockwise loop not needed, because guard turns to the right at each obstacle


    print(f'Total possible loops detected: {possible_loops}:')
    for l in loop_positions:
        print(l)

    return

if __name__ == "__main__":
    main()