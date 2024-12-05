import sys

def sliding_window_xmas_detector(grid):
    xmas_found = 0
    for i in range(0,len(grid[0])-2):
        print(f'Current column is {i}')
        if ((grid[0][i] == 'M' and grid[1][i+1] == 'A' and grid[2][i+2] == 'S') or \
            (grid[0][i] == 'S' and grid[1][i+1] == 'A' and grid[2][i+2] == 'M')) and \
            ((grid[0][i+2] == 'M' and grid[1][i+1] == 'A' and grid[2][i] == 'S') or \
            (grid[0][i+2] == 'S' and grid[1][i+1] == 'A' and grid[2][i] == 'M')):
            xmas_found += 1
    return xmas_found

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    horizontal_window = []
    xmas_count = 0

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        # initialize window
        line = file.readline()
        row = list(line.strip())
        horizontal_window.append(row)
        line = file.readline()
        row = list(line.strip())
        horizontal_window.append(row)

        for line in file:
            row = list(line.strip())
            horizontal_window.append(row)
            print('Calling xmas detector:')
            xmas_count += sliding_window_xmas_detector(horizontal_window)
            horizontal_window.pop(0)

    print(f'Total X-MAS count: {xmas_count}')

if __name__ == "__main__":
    main()