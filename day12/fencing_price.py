import sys
import logging

def find_plots(grid, row, col, logger):

    id = grid[row][col][0]

    # logger.debug(f'Element visited is {([row], [col])} with {id} and flag == {grid[row][col][1]}')

    area = 0
    perimeter = 0
    grid[row][col][1] = True

    left = col - 1
    right = col + 1
    up = row - 1
    down = row + 1

    if left >= 0:
        if grid[row][left][0] == id:
            if grid[row][left][1] == False:

                logger.debug(f'Element to the left is {grid[row][left]}')
                a, p = find_plots(grid, row, left, logger)
                area += a
                perimeter += p
        else:
            perimeter += 1
    else:
        perimeter += 1
    if right < len(grid[0]):
        if grid[row][right][0] == id:
            if grid[row][right][1] == False:

                logger.debug(f'Element to the right is {grid[row][right]}')
                a, p = find_plots(grid, row, right, logger)
                area += a
                perimeter += p
        else:
            perimeter += 1
    else:
        perimeter += 1
    if up >= 0:
        if grid[up][col][0] == id:
            if grid[up][col][1] == False:

                logger.debug(f'Element above is {grid[up][col]}')
                a, p = find_plots(grid, up, col, logger)
                area += a
                perimeter += p
        else:
            perimeter += 1
    else:
        perimeter += 1
    if down < len(grid):
        if grid[down][col][0] == id:
            if grid[down][col][1] == False:

                logger.debug(f'Element below is {grid[down][col]}')
                a, p = find_plots(grid, down, col, logger)
                area += a
                perimeter += p
        else:
            perimeter += 1
    else:
        perimeter += 1

    return area + 1, perimeter


def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    total_price = 0
    grid = []
    counted = []
    plots = []


    # Configure the logging system
    if "debug" in filename:
       logging.basicConfig(level=logging.DEBUG, format='%(funcName)s: %(message)s')  # Set to DEBUG to see debug messages
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)  # Create a logger for your script

    with open(filename, 'r') as file:
        for line in file:
            line = list(line.strip())
            row = []
            for id in line:
                row.append([id, False])
            grid.append(row)

    # logger.debug(grid)

    stride = len(grid[0])
    elementcnt = len(grid) * stride

    logger.debug(f'Dimensions: stride = {stride}, element count = {elementcnt}')

    for i in range(0, elementcnt):
        row = i // stride
        col = i % stride
        # if col == 0:
        #     print()
        # print(f'({row}, {col})', end = ' ')

        element = grid[row][col]
        if element[1] == False:
            logger.debug(f'----> Looking for plot at coordinates {([row],[col])} with ID {element[0]}')
            area, perimenter = find_plots(grid, row, col, logger)
            plots.append([grid[row][col], area, perimenter])


    for plot in plots:
        prod =  plot[1] * plot[2]
        logger.debug(f'Plot with plant {plot[0]} has area {plot[1]} and perimenter {plot[2]}. Price = {prod}.')
        total_price += prod

    print(f'\nTotal fence price for the plot: {total_price}')
    return

if __name__ == "__main__":
    main()