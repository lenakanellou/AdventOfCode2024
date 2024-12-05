import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    grid = []
    xmas_count = 0

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        for line in file:
            row = list(line.strip())
            grid.append(row)

    # find all occurrences horizontally, left-to-right and right-to-left
    for rownum, row in enumerate(grid):
        row_string = "".join(row)
        curr_xmas_cnt = row_string.count('XMAS')
        xmas_count += curr_xmas_cnt
        # print(f'XMAS found {curr_xmas_cnt} times in row {rownum}.')
        curr_xmas_cnt = row_string.count('SAMX')
        xmas_count += curr_xmas_cnt
        # print(f'XMAS found {curr_xmas_cnt} times in row {rownum}.')


    # find all occurrences vertically, either direction
    for colnum in range(0, len(grid[0])):
        column_string = "".join(row[colnum] for row in grid)
        curr_xmas_cnt = column_string.count('XMAS')
        xmas_count += curr_xmas_cnt
        # print(f'XMAS found {curr_xmas_cnt} times in column {colnum}.')
        curr_xmas_cnt = column_string.count('SAMX')
        xmas_count += curr_xmas_cnt
        # print(f'XMAS found {curr_xmas_cnt} times in column {colnum}.')


    # find all occurrences diagonally, left up to right down, lower half (:col num will be 0)
    for row in range(1, len(grid)-3):
        diag_string = "".join(grid[row+i][i] for i in range(0, len(grid)-row))
        # print(f'Current diagonal gives string {diag_string}.')
        curr_xmas_cnt = diag_string.count('XMAS')
        xmas_count += curr_xmas_cnt
        # print(f'XMAS found {curr_xmas_cnt} times in {diag_string}.')
        curr_xmas_cnt = diag_string.count('SAMX')
        xmas_count += curr_xmas_cnt
        # print(f'SAMX found {curr_xmas_cnt} times in {diag_string}.')

    # find all occurrences diagonally, right up to left down, lower half (:col num will be len(grid[0]-1))
    for row in range(1, len(grid)-3):
        diag_string = "".join(grid[row+i][len(grid[0])-1-i] for i in range(0, len(grid)-row))
        # print(f'Current diagonal gives string {diag_string}.')
        curr_xmas_cnt = diag_string.count('XMAS')
        xmas_count += curr_xmas_cnt
        # print(f'XMAS found {curr_xmas_cnt} times in {diag_string}.')
        curr_xmas_cnt = diag_string.count('SAMX')
        xmas_count += curr_xmas_cnt
        # print(f'SAMX found {curr_xmas_cnt} times in {diag_string}.')

    # find all occurrences diagonally, left up to right down, upper half
    for col in range(0, len(grid)-3):
        diag_string = "".join(grid[i][col+i] for i in range(0, len(grid)-col))
        # print(f'Current diagonal gives string {diag_string}.')
        curr_xmas_cnt = diag_string.count('XMAS')
        xmas_count += curr_xmas_cnt
        # print(f'XMAS found {curr_xmas_cnt} times in {diag_string}.')
        curr_xmas_cnt = diag_string.count('SAMX')
        xmas_count += curr_xmas_cnt
        # print(f'SAMX found {curr_xmas_cnt} times in {diag_string}.')

    # find all occurrences diagonally, right up to left down, upper half
    for col in range(0, len(grid)-3):
        diag_string = "".join(grid[i][len(grid)-1-col-i] for i in range(0, len(grid)-col))
        # print(f'Current diagonal gives string {diag_string}.')
        curr_xmas_cnt = diag_string.count('XMAS')
        xmas_count += curr_xmas_cnt
        # print(f'XMAS found {curr_xmas_cnt} times in {diag_string}.')
        curr_xmas_cnt = diag_string.count('SAMX')
        xmas_count += curr_xmas_cnt
        # print(f'SAMX found {curr_xmas_cnt} times in {diag_string}.')

    print(f'Total XMAS count: {xmas_count}')

if __name__ == "__main__":
    main()