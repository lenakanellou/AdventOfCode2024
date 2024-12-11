import sys
import logging

def trailfinder(logger, point, h, dims, grid, nineset):

    total = 0

    if h == 0:
        logger.debug(f'Checking trailhead coordinates: {point}.')
    else:
        logger.debug(f'Checking paths at point {point} and level {h} with height {grid[point[0]][point[1]]}.')

    # base case
    if h == 9:
        if grid[point[0]][point[1]] == '9':
            logger.debug(f'Found 9 at point {point}')
            nineset.add(point)
            return 1
        else:
            return 0
    else:
        if point[0]-1 >= 0:
            neighbor = (point[0]-1, point[1]) # up
            if int(grid[neighbor[0]][neighbor[1]]) == h+1:
                logger.debug(f'Going up from {point} with level {grid[point[0]][point[1]]}')
                total += trailfinder(logger, neighbor, h+1, dims, grid, nineset)
        # else:
        #     logger.debug(f'Nothing to check in direction up')

        if point[1]+1 < dims[1]:
            neighbor = (point[0], point[1]+1) # right
            if int(grid[neighbor[0]][neighbor[1]]) == h+1:
                logger.debug(f'Going right from {point} with level {grid[point[0]][point[1]]}')
                total += trailfinder(logger, neighbor, h+1, dims, grid, nineset)
        # else:
        #     logger.debug(f'Nothing to check in direction right')

        if point[0]+1 < dims[0]:
            neighbor = (point[0]+1, point[1]) # down
            if int(grid[neighbor[0]][neighbor[1]]) == h+1:
                logger.debug(f'Going down from {point} with level {grid[point[0]][point[1]]}')
                total += trailfinder(logger, neighbor, h+1, dims, grid, nineset)
        # else:
        #     logger.debug(f'Nothing to check in direction down')

        if point[1]-1 >= 0:
            neighbor = (point[0], point[1]-1) # left
            if int(grid[neighbor[0]][neighbor[1]]) == h+1:
                logger.debug(f'Going left from {point} with level {grid[point[0]][point[1]]}')
                total += trailfinder(logger, neighbor, h+1, dims, grid, nineset)
        # else:
        #     logger.debug(f'Nothing to check in direction left')

    return total

def main():

    if len(sys.argv) > 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # Configure the logging system
    if "debug" in filename:
       logging.basicConfig(level=logging.DEBUG, format='%(funcName)s: %(message)s')  # Set to DEBUG to see debug messages
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)  # Create a logger for your script


    possible_trailheads = []
    grid = []
    score_sum = 0
    rating_sum = 0
    R = 0
    C = 0

    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            R += 1
            line = line.strip()
            heights = []
            for col, char in enumerate(line):
                if char == '0':
                    possible_trailheads.append((row, col))
                heights.append(char)
            grid.append(heights)
        logger.debug(possible_trailheads)
    C = len(grid[0])

    logger.debug(grid)

    for th in possible_trailheads:
        nineset = set()
        rating = trailfinder(logger, th, 0, (R, C), grid, nineset)
        logger.debug(f'Possible trails for trailhead {th}: {rating}')
        score_sum += len(nineset)
        rating_sum += rating

    print(f'Sum of trailhead scores is: {score_sum}.\nSum of trailhead ratings is: {rating_sum}')
    return

if __name__ == "__main__":
    main()