import sys
import numpy as np
import re


def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    button_pattern = r"Button (\w): X\+(\d+), Y\+(\d+)"
    prize_pattern = r"Prize: X=(\d+), Y=(\d+)"  

    x_a = 0
    x_b = 0

    y_a = 0
    y_b = 0

    c_x = 0
    c_y = 0

    with open(filename, 'r') as file:
        for line in file:
            button_match = re.match(button_pattern, line)
            prize_match = re.match(prize_pattern, line)

            if button_match:
                button, x, y = button_match.groups()
                # print(f"Matched Button pattern. Button: {button}, X: {x}, Y: {y}")
                if button == 'A':
                    x_a = int(x)
                    y_a = int(y)
                elif button == 'B':
                    x_b = int(x)
                    y_b = int(y)
            elif prize_match:
                c_x, c_y = prize_match.groups()
                # print(f"Matched Prize pattern. X: {c_x}, Y: {c_y}")               
            else:
                # print("No match for line:", line) 
                S = np.array([[x_a, x_b],[y_a, y_b]])
                C = np.array([int(c_x), int(c_y)])
                try:
                    pushes = np.linalg.solve(S, C)
                    if pushes[0] > 100  or pushes[0] < 0 or pushes[1] > 100 or pushes[1] < 0:
                        print(f'Pushes needed for prize at {(c_x, c_y)}: {pushes[0]} of button A and {pushes[1]} of button B.')
                except np.linalg.LinAlgError as e:
                    print(f'Prize at {(c_x, x_y)} unreachable!', e)




if __name__ == "__main__":
    main()
