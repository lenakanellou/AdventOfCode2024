import sys
import os

def find_dim(filename):
    try:
        with open(filename, 'rb') as file:
            # Count lines efficiently in binary mode
            X = sum(1 for line in file)
            file.seek(0)  # Reset the file pointer to the beginning
            first_line = file.readline()  # Read the first line
            Y = len(first_line.strip())  # Get the length of the first line
        return X, Y
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

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

    X, Y = find_dim(filename)
    unique_antinodes = 0

    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            # line = list(line.strip())
            # grid.append(line)
            # print(line)
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
                        antinodes.add((row, col))
                        for pos in positions:
                            antinodes.add((pos[0], pos[1]))
                            x_diff = col - pos[1]
                            y_diff = row - pos[0]

                            anti1_x = pos[0] - y_diff
                            anti1_y = pos[1] - x_diff

                            anti2_x = row + y_diff
                            anti2_y = col + x_diff

                            while anti1_x < X and anti1_y < Y and anti1_x >= 0 and anti1_y >= 0 :

                                antinodes.add((anti1_x, anti1_y))

                                anti1_x = anti1_x - y_diff
                                anti1_y = anti1_y - x_diff

                            while anti2_x < X and anti2_y < Y and anti2_x >= 0 and anti2_y >= 0 :

                                antinodes.add((anti2_x, anti2_y))

                                anti2_x = anti2_x + y_diff
                                anti2_y = anti2_y + x_diff

                            # if debug == True:
                            #     print(f'Possible antinodes for {pos} : ({anti1_x}, {anti1_y}) and ({anti2_x}, {anti2_y}).')

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