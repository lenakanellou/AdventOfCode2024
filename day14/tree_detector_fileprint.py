import sys
import re
import math

def main():

    if len(sys.argv) != 5:
        print("Usage: python script.py <filename> <width> <height>")
        sys.exit(1)

    filename = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    interval = int(sys.argv[4])

    secs = 0

    # robot_positions = set()
    robot_positions = []
    robot_pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"

    robots_check_sum = 0

    simulate = True



    with open(filename, 'r') as file:
        for line in file:
            match = re.search(robot_pattern, line)

            if match:
                p1, p2, v1, v2 = map(int, match.groups())
                # print(f"p: ({p1}, {p2}), v: ({v1}, {v2})")
                robots_check_sum += 1
            else:
                print("No match found.")

            # p1 = (p1 + (100 * v1)%width)%width
            # p2 = (p2 + (100 * v2)%height)%height

            # robot_positions.add((p1, p2))
            robot_positions.append([p1, p2, v1, v2])

    if robots_check_sum != len(robot_positions):
        print(f'CHECKSUM ERROR!!! Initially {robots_check_sum} robots, currently counting {len(robot_positions)} robots!')

    for h in range(0, height):
        line = []
        for w in range(0, width):
            char = '.'
            for rob in robot_positions:
                if rob[0] == w and rob[1] == h:
                    char = 'R'
                    break
                else:
                    char = '.'
            line.append(char)
        print(''.join(line))
    print('\n\n')



    while simulate == True:

        with open('find_tree.txt', 'w') as file:

            file.write('Starting at configuration: \n')
            for h in range(0, height):
                line = []
                for w in range(0, width):
                    char = '.'
                    for rob in robot_positions:
                        if rob[0] == w and rob[1] == h:
                            char = 'R'
                            break
                        else:
                            char = '.'
                    line.append(char)
                line.append('\n')
                file.write(''.join(line))
            file.write('\n\n')

            for i in range(0, interval):

                # simulate robot system moving forward one second
                for rob in robot_positions:
                    rob[0] = (rob[0] + rob[2])%width
                    rob[1] = (rob[1] + rob[3])%height


                file.write(f'Config after second :\t {secs+i+1}\n')

                for h in range(0, height):
                    line = []
                    for w in range(0, width):
                        char = '.'
                        for rob in robot_positions:
                            if rob[0] == w and rob[1] == h:
                                char = 'R'
                                break
                            else:
                                char = '.'
                        line.append(char)
                    line.append('\n')
                    file.write(''.join(line))
                file.write('\n\n')


        user_input = input(f"Simulate for another {interval} seconds? (yes/no): ").strip().lower()

        # Determine the boolean value based on the input
        if user_input in ('yes', 'y', 'true', '1'):
            simulate = True
        elif user_input in ('no', 'n', 'false', '0'):
            simulate = False
        else:
            print("Invalid input. Defaulting to False.")
            simulate = False

        secs += interval
        print(f'Current elapsed simulation time: {secs} seconds.')



    return


if __name__ == "__main__":
    main()