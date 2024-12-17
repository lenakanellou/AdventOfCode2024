import sys
import re
import logging

# sys.setrecursionlimit(3000)

def translate_direction(direction):
    if direction == 0:
        return "UP"
    elif direction == 1:
        return "RIGHT"
    elif direction == 2:
        return "DOWN"
    elif direction == 3:
        return "LEFT"
    else:
        print(f'Invalid direction!!! {direction}')

def next_position(curr_position, direction):
    # 0: up, 1: right, 2: down, 3: left
    nxt_row = curr_position[0]
    nxt_col = curr_position[1]
    if direction == 0:  # up
        nxt_row -= 1
    elif direction == 1:
        nxt_col += 1
    elif direction == 2:
        nxt_row += 1
    elif direction == 3:
        nxt_col -= 1
    else:
        print(f'Invalid direction! {direction}')
    return nxt_row, nxt_col


def pathfinder(curr_position, direction, maze, scores, curr_score, visited, logger):

    visited.add((curr_position[0], curr_position[1]))
    min_score = 0

    # explore path in current direction
    nxt_row, nxt_col = next_position(curr_position, direction)
    if (nxt_row, nxt_col) not in visited:
        dstring = translate_direction(direction)
        logger.debug(f'Pathfinder: direction {dstring}. Next position: {nxt_row}x{nxt_col}')
        nxt_char = maze[nxt_row][nxt_col]
        if nxt_char != '#':
            if nxt_char == 'E':
                curr_score += 1
                scores.append(curr_score)
                logger.debug(f'--->>> EXIT FOUND!!! Current score: {curr_score}')
            else:

                if len(scores) > 0:
                    min_score = min([s for s in scores if s != 0])
                    if curr_score + 1 < min_score:
                        pathfinder([nxt_row, nxt_col], direction, maze, scores, curr_score+1, visited, logger)
                else:
                    pathfinder([nxt_row, nxt_col], direction, maze, scores, curr_score+1, visited, logger)

        # visited.discard((nxt_row, nxt_col))



    # explore path in next clock-wise direction
    d = (direction+1)%4
    nxt_row, nxt_col = next_position(curr_position, d)
    if (nxt_row, nxt_col) not in visited:
        dstring = translate_direction(d)
        logger.debug(f'Pathfinder: direction {dstring}. Next position: {nxt_row}x{nxt_col}')
        nxt_char = maze[nxt_row][nxt_col]
        if nxt_char != '#':
            if nxt_char == 'E':
                curr_score += 1001
                scores.append(curr_score)
                logger.debug(f'--->>> EXIT FOUND!!! Current score: {curr_score}')
            else:
                if len(scores) > 0:
                    min_score = min([s for s in scores if s != 0])
                    if curr_score + 1001 < min_score:
                        pathfinder([nxt_row, nxt_col], d, maze, scores, curr_score+1001, visited, logger)
                else:
                    pathfinder([nxt_row, nxt_col], d, maze, scores, curr_score+1001, visited, logger)
        # visited.discard((nxt_row, nxt_col))


    # explore path in next counter-clockwise direction
    d = (direction+3)%4
    nxt_row, nxt_col = next_position(curr_position, d)
    if (nxt_row, nxt_col) not in visited:
        dstring = translate_direction(d)
        logger.debug(f'Pathfinder: direction {dstring}. Next position: {nxt_row}x{nxt_col}')
        nxt_char = maze[nxt_row][nxt_col]
        if nxt_char != '#':
            if nxt_char == 'E':
                curr_score += 1001
                scores.append(curr_score)
                logger.debug(f'--->>> EXIT FOUND!!! Current score: {curr_score}')
            else:
                if len(scores) > 0:
                    min_score = min([s for s in scores if s != 0])
                    if curr_score + 1001 < min_score:
                        pathfinder([nxt_row, nxt_col], d, maze, scores, curr_score+1001, visited, logger)
                else:
                    pathfinder([nxt_row, nxt_col], d, maze, scores, curr_score+1001, visited, logger)
        # visited.discard((nxt_row, nxt_col))


    visited.discard((curr_position[0], curr_position[1]))
    return

def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # Configure the logging system
    if "debug" in filename:
       logging.basicConfig(level=logging.DEBUG, format='%(funcName)s: %(message)s')  # Set to DEBUG to see debug messages
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)  # Create a logger for your script


    maze = []
    scores = []
    start = [0, 0]
    finish = [0, 0]
    d = 0 # 0: up, 1: right, 2: down, 3: left
    visited = set()
    total_paths = 0

    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            line = list(line.strip())

            if 'S' in line:
                start[0] = row
                start[1] = line.index('S')
            if 'E' in line:
                finish[0] = row
                finish[1] = line.index('E')

            logger.debug(''.join(line))
            maze.append(line)

    print(f'Maze ready! Start point at {start}. End point at {finish}.')

    pathfinder(start, 1, maze, scores, 0, visited, logger)

    # min_score = min([s for s in scores if s != 0])
    if len(scores) > 0:
        min_score = min(scores)
    else:
        min_score = 0
    print(f'Minimum reindeer score for maze is: {min_score}. Total scores compared: {len(scores)}. Total paths traversed: {total_paths}')

    return

if __name__ == "__main__":
    main()