import sys
import re

if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
start_sequence = 0
state = 0
nxt_state = 0
curr_mult = []
product_sum = 0

def get_multipliers(string_exression):
    pattern = r'\d+'
    matches = re.findall(pattern, string_exression)
    # Flatten the pairs into a single list
    numbers = [int(num) for pair in matches for num in pair]

    return matches


# state == 0 :
# how to get here: no multiplication detected
# next possible: state 1
def state0(self, input):
    global curr_mult
    if input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 1 :
# how to get here: previous state was 0, found an m
# next possible: state 2
def state1(self, input):
    global curr_mult
    if input == 'u':
        curr_mult.append('u')
        return 2
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 2 :
# how to get here: previous state was m, found an u
# next possible: state 3
def state2(self, input):
    global curr_mult
    if input == 'l':
        curr_mult.append('l')
        return 3
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 3 :
# how to get here: previous state was mu, found an l
# next possible: state 4
def state3(self, input):
    global curr_mult
    if input == '(':
        curr_mult.append('(')
        return 4
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 4 :
# how to get here: previous state was mul, found a (
# next possible: state 5
def state4(self, input):
    global curr_mult
    if input.isdigit():
        curr_mult.append(self, input)
        return 5
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 5 :
# how to get here: previous state was mul( , found a number
# next possible: states 6 or 8
def state5(self, input):
    global curr_mult
    if input.isdigit():
        curr_mult.append(self, input)
        return 6
    elif input == ',':
        curr_mult.append(input)
        return 8
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 6 :
# how to get here: previous state was mul(X, found a number
# next possible: states 7 or 8
def state6(self, input):
    global curr_mult
    if input.isdigit():
        curr_mult.append(input)
        return 7
    elif input == ',':
        curr_mult.append(input)
        return 8
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 7 :
# how to get here: previous state was mul(XY, found a number
# next possible: state 8
def state7(self, input):
    global curr_mult
    if input == ',':
        curr_mult.append(input)
        return 8
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 8 :
# how to get here: previous state was mul(XYZ, found a comma
# next possible: state 9
def state8(self, input):
    global curr_mult
    if input.isdigit():
        curr_mult.append(input)
        return 9
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 9 :
# how to get here: previous state was mul(XYZ, , found a number
def state9(self, input):
    global curr_mult
    if input.isdigit():
        curr_mult.append(input)
        return 10
    elif input == ')':
        curr_mult.append(input)
        return 12
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 10 :
# how to get here: previous state was mul(XYZ,A, found a number
def state10(self, input):
    global curr_mult
    if input.isdigit():
        curr_mult.append(input)
        return 11
    elif input == ')':
        print('in state 10 going to 12')
        curr_mult.append(input)
        return 12
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:

        curr_mult = []
        return 0

# state == 11 :
# how to get here: previous state was mul(XYZ,AB , found a number
def state11(self, input):
    global curr_mult
    if input == ')':
        curr_mult.append(input)
        return 12
    elif input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0

# state == 12 :
# how to get here: previous state was mul(XYZ,ABC, found a )
def state12(self, input):
    global curr_mult
    global product_sum
    expression_string = "".join(curr_mult)
    print(f'Full multiplication found! Statement is {expression_string}')
    mults = get_multipliers(expression_string)
    product = int(mults[0])*int(mults[1])
    product_sum = product_sum + product
    print(f'Current product sum is : {product_sum}')
    if input == 'm':
        curr_mult = ['m']
        return 1
    else:
        curr_mult = []
        return 0


state_machine = {
    0: state0,
    1: state1,
    2: state2,
    3: state3,
    4: state4,
    5: state5,
    6: state6,
    7: state7,
    8: state8,
    9: state9,
    10: state10,
    11: state11,
    12: state12
}

with open(filename, 'r') as file:
    for char in iter(lambda: file.read(1), ''):
        state = nxt_state
        nxt_state = state_machine[state](char)