import sys
import re
import logging


def find_next_position(direction, curr_position):
    next_row = curr_position[0]
    next_col = curr_position[1]
    if direction == '>':
        next_col += 1
    if direction == 'v':
        next_row += 1
    if direction == '<':
        next_col -= 1
    if direction == '^':
        next_row -= 1

    return next_row, next_col

def move_along_direction(direction, curr_position, grid):

    char = grid[curr_position[0]][curr_position[1]]

    if direction == '>':
        next_row, next_col = move_right(curr_position, grid)
    if direction == 'v':
        next_row, next_col = move_down(curr_position, grid)
    if direction == '<':
       next_row, next_col = move_left(curr_position, grid)
    if direction == '^':
        next_row, next_col = move_up(curr_position, grid)

    return next_row, next_col

def move_right(curr_position, grid):

    char = grid[curr_position[0]][curr_position[1]]

    if curr_position[1]+1 < len(grid[0])-1:
        if grid[curr_position[0]][curr_position[1]+1] == '.':
            grid[curr_position[0]][curr_position[1]+1] = char
            grid[curr_position[0]][curr_position[1]] = '.'
            return curr_position[0], curr_position[1]+1
        elif grid[curr_position[0]][curr_position[1]+1] == '#':
            return curr_position[0], curr_position[1]
        else:
            nxt_char = grid[curr_position[0]][curr_position[1]+1]
            r, c = move_right([curr_position[0], curr_position[1]+1], grid)
            if c != curr_position[1]+1:
                nxt_char = grid[curr_position[0]][curr_position[1]+1]
                grid[curr_position[0]][curr_position[1]+1] = char
                grid[curr_position[0]][curr_position[1]] = nxt_char
                return curr_position[0], curr_position[1]+1
            else:
                return curr_position[0], curr_position[1]

    else:
        return curr_position[0], curr_position[1]


def move_down(curr_position, grid):

    char = grid[curr_position[0]][curr_position[1]]

    if curr_position[0]+1 < len(grid)-1:
        if grid[curr_position[0]+1][curr_position[1]] == '.':
            grid[curr_position[0]+1][curr_position[1]] = char
            grid[curr_position[0]][curr_position[1]] = '.'
            return curr_position[0]+1, curr_position[1]
        elif grid[curr_position[0]+1][curr_position[1]] == '#':
            return curr_position[0], curr_position[1]
        else:
            nxt_char = grid[curr_position[0]+1][curr_position[1]]
            r, c = move_down([curr_position[0]+1, curr_position[1]], grid)
            if r != curr_position[0]+1:
                nxt_char = grid[curr_position[0]+1][curr_position[1]]
                grid[curr_position[0]+1][curr_position[1]] = char
                grid[curr_position[0]][curr_position[1]] = nxt_char
                return curr_position[0]+1, curr_position[1]
            else:
                return curr_position[0], curr_position[1]

    else:
        return curr_position[0], curr_position[1]

def move_left(curr_position, grid):

    char = grid[curr_position[0]][curr_position[1]]

    if curr_position[1]-1 > 0:
        if grid[curr_position[0]][curr_position[1]-1] == '.':
            grid[curr_position[0]][curr_position[1]-1] = char
            grid[curr_position[0]][curr_position[1]] = '.'
            return curr_position[0], curr_position[1]-1
        elif grid[curr_position[0]][curr_position[1]-1] == '#':
            return curr_position[0], curr_position[1]
        else:
            nxt_char = grid[curr_position[0]][curr_position[1]-1]
            r, c = move_left([curr_position[0], curr_position[1]-1], grid)
            if c != curr_position[1]-1:
                nxt_char = grid[curr_position[0]][curr_position[1]-1]
                grid[curr_position[0]][curr_position[1]-1] = char
                grid[curr_position[0]][curr_position[1]] = nxt_char
                return curr_position[0], curr_position[1]-1
            else:
                return curr_position[0], curr_position[1]

    else:
        return curr_position[0], curr_position[1]


def move_up(curr_position, grid):

    char = grid[curr_position[0]][curr_position[1]]

    if curr_position[0] - 1 > 0:
        if grid[curr_position[0]-1][curr_position[1]] == '.':
            grid[curr_position[0]-1][curr_position[1]] = char
            grid[curr_position[0]][curr_position[1]] = '.'
            return curr_position[0]-1, curr_position[1]
        elif grid[curr_position[0]-1][curr_position[1]] == '#':
            return curr_position[0], curr_position[1]
        else:
            nxt_char = grid[curr_position[0]-1][curr_position[1]]
            r, c = move_up([curr_position[0]-1, curr_position[1]], grid)
            if r != curr_position[0]-1:
                nxt_char = grid[curr_position[0]-1][curr_position[1]]
                grid[curr_position[0]-1][curr_position[1]] = char
                grid[curr_position[0]][curr_position[1]] = nxt_char
                return curr_position[0]-1, curr_position[1]
            else:
                return curr_position[0], curr_position[1]

    else:
        return curr_position[0], curr_position[1]



def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    grid = []
    moves = []
    robot_position = [0, 0]

    # Configure the logging system
    if "debug" in filename:
       logging.basicConfig(level=logging.DEBUG, format='%(funcName)s: %(message)s')  # Set to DEBUG to see debug messages
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)  # Create a logger for your script


    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            logger.debug(line)
            line = line.strip()
            if '#' in line:
                doubled_line = []
                for char in line:
                    if char == '#':
                        doubled_line += ['#', '#']
                    elif char == 'O':
                        doubled_line += ['[', ']']
                    elif char == '.':
                        doubled_line += ['.', '.']
                    elif char == '@':
                        doubled_line += ['@', '.']
                grid.append(doubled_line)
                if '@' in line:
                    robot_position[0] = i
                    robot_position[1] = 2*line.index('@')
            elif line != []:
                moves = moves + list(line)

    for line in grid:
        logger.debug(line)
    logger.debug(f'--> {len(moves)} items in list moves: {moves}')

    print(f'Initial robot position : {robot_position}')


    # simulate robot movements and box shifts

    # for m in moves:
    #     logger.debug(f'\nAfter move {m}:')

    #     next_row = 0
    #     next_col = 0

    #     # next_row, next_col = find_next_position(m, robot_position)

    #     # if grid[next_row][next_col] != '#':
    #     #     if grid[next_row][next_col] == '.':
    #     #         grid[next_row][next_col] = '@'
    #     #         grid[robot_position[0]][robot_position[1]] = '.'
    #     #         robot_position[0] = next_row
    #     #         robot_position[1] = next_col

    #     if m == '>':
    #         next_row, next_col = move_right(robot_position, grid)
    #     if m == 'v':
    #         next_row, next_col = move_down(robot_position, grid)
    #     if m == '<':
    #         next_row, next_col = move_left(robot_position, grid)
    #     if m == '^':
    #         next_row, next_col = move_up(robot_position, grid)

    #     robot_position[0] = next_row
    #     robot_position[1] = next_col
    #     logger.debug(f'New robot position after moving {m}: {robot_position}')

    #     for line in grid:
    #         logger.debug(''.join(line))


    print(f'Final robot position : {robot_position}')

    # calculate final checksum

    checksum = 0

    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            e = grid[row][col]
            if e =='O':
                checksum += (100*row + col)

    print(f'Final GPS coordinates sum: {checksum}')




    return

if __name__ == "__main__":
    main()