import sys

def main():

    if len(sys.argv) > 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    grid = []

    if filename.strip(".\\") == "sample_input.txt":
        debug = True
    else:
        debug = False

    antennas = {}
    antinodes = set()
    newline = False
    x_diff = 0
    y_diff = 0

    X = 0
    Y = 0
    unique_antinodes = 0

    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            # line = list(line.strip())
            # grid.append(line)
            # print(line)
            Y += 1
            for col, char in enumerate(line.strip()):
                if char != '.':
                    newline = True
                    # print(char, end="")
                    positions = antennas.get(char)
                    if debug == True:
                        print(f'Line {row}: Positions to check for {char} at col {col}:')
                    if positions == None:
                        if debug == True:
                            print('None')
                        antennas[char] = [(row, col)]
                    else:
                        for pos in positions:
                            x_diff = col - pos[1]
                            y_diff = row - pos[0]

                            anti1_x = pos[0] - y_diff
                            anti1_y = pos[1] - x_diff

                            anti2_x = row + y_diff
                            anti2_y = col + x_diff

                            if anti1_x >= 0 and anti1_y >= 0:
                                antinodes.add((anti1_x, anti1_y))
                            if anti2_x >= 0 and anti2_y >= 0:
                                antinodes.add((anti2_x, anti2_y))
                            if debug == True:
                                print(f'Possible antinodes for {pos} : ({anti1_x}, {anti1_y}) and ({anti2_x}, {anti2_y}).')

                        antennas[char].append((row, col))
                    # print(f'{row}, {col}: {char}', end="")
            if debug == True:
                if newline:
                    print()
                    newline = False
            X = len(line)

    for pos in antinodes:
        if pos[0] < Y and pos[1] < X:
            unique_antinodes += 1

    print(f'Grid size is {X} x {Y}. Total number of antinodes detected: {unique_antinodes}')
    # print(f'Total antinode positions: {antinodes}')
    return


if __name__ == "__main__":
    main()