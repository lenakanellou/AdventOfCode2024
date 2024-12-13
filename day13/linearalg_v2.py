import sys
import re

from sympy import symbols, Eq, linsolve


def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    button_pattern = r"Button (\w): X\+(\d+), Y\+(\d+)"
    prize_pattern = r"Prize: X=(\d+), Y=(\d+)"  

    
    A, B = symbols('A B')

    x_a = 0
    x_b = 0

    y_a = 0
    y_b = 0

    c_x = 0
    c_y = 0

    total_tokens = 0
   
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
                # S = np.array([[x_a, x_b],[y_a, y_b]])
                # C = np.array([int(c_x), int(c_y)])

                c_x = int(c_x)+10000000000000
                c_y = int(c_y)+10000000000000

                eq1 = Eq(x_a*A + x_b*B, c_x)
                eq2 = Eq(y_a*A + y_b*B, c_y)


                # Solve the system
                solutions = linsolve([eq1, eq2], A, B)
                solutions_list = list(solutions)

                if len(solutions_list)>1:
                    print(f'No single solution found for prize {(c_x, c_y)}.')
                else:

                    push_a = round(solutions_list[0][0])
                    push_b = round(solutions_list[0][1])

                    if x_a*push_a + x_b*push_b == int(c_x) and y_a*push_a + y_b*push_b == int(c_y):
                        print(f'Solutions for prize {(c_x, c_y)} : A: {push_a}, B: {push_b}') 
                        total_tokens += push_a*3 + push_b
                    else:
                        print(f'No solution found for prize {(c_x, c_y)}.')
                    # Check if the solutions are integers
                    # for solution in solutions:
                    #    if all(isinstance(i, int) for i in solution):
                    #        print(f"Integer solutions for prize {(c_x, c_y)}: {solution}")
                    #    else:
                    #        print(f"Non-integer solution for prize {(c_x, c_y)}: {solution}")

            # else:
                # print("No match for line:", line) 



    print(f'Min tokens required to win all possible prizes are: {total_tokens}.')


if __name__ == "__main__":
    main()
