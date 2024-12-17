import sys
import re
import math

def main():

    if len(sys.argv) != 4:
        print("Usage: python script.py <filename> <width> <height>")
        sys.exit(1)

    filename = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    # robot_positions = set()
    robot_positions = []
    robot_pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"

    robots_check_sum = 0


    with open(filename, 'r') as file:
        for line in file:
            match = re.search(robot_pattern, line)

            if match:
                p1, p2, v1, v2 = map(int, match.groups())
                # print(f"p: ({p1}, {p2}), v: ({v1}, {v2})")
                robots_check_sum += 1
            else:
                print("No match found.")

            p1 = (p1 + (100 * v1)%width)%width
            p2 = (p2 + (100 * v2)%height)%height

            # robot_positions.add((p1, p2))
            robot_positions.append((p1, p2))

    print(f'After 100 seconds, occupied positions are the following {len(robot_positions)}:\n{robot_positions}')

    if robots_check_sum != len(robot_positions):
        print(f'CHECKSUM ERROR!!! Initially {robots_check_sum} robots, currently counting {len(robot_positions)} robots!')


    quadrant_robot_count = [0, 0, 0, 0]
    width_middle = width // 2
    height_middle = height // 2
    # rob[0] is the column, rob[1] the row
    for rob in robot_positions:
        if rob[0] < width_middle and rob[1] < height_middle:
            quadrant_robot_count[0] += 1
        elif rob[0] > width_middle and rob[1] < height_middle:
            quadrant_robot_count[1] += 1
        elif rob[0] < width_middle and rob[1] > height_middle:
            quadrant_robot_count[2] += 1
        elif rob[0] > width_middle and rob[1] > height_middle:
            quadrant_robot_count[3] += 1


    print(f'\nTotal robots detected: {robots_check_sum}\n'+
          f'Robots per quadrant:\nUpper left: {quadrant_robot_count[0]}\tUpper right: {quadrant_robot_count[1]}\n'+
          f'Lower left: {quadrant_robot_count[2]}\tLower right: {quadrant_robot_count[3]}'+
          f'\n\nSafety factor: {math.prod(quadrant_robot_count)}')

    return


if __name__ == "__main__":
    main()