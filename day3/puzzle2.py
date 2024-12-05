import sys
import re



class stateMachine:

    def __init__(self):
        self.state = 0
        self.nxt_state = 0
        self.curr_mult = []
        self.product_sum = 0
        self.enable = True


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
        if input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 1 :
    # how to get here: previous state was 0, found an m
    # next possible: state 2
    def state1(self, input):
        if input == 'u':
            self.curr_mult.append('u')
            return 2
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 2 :
    # how to get here: previous state was m, found an u
    # next possible: state 3
    def state2(self, input):
        if input == 'l':
            self.curr_mult.append('l')
            return 3
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 3 :
    # how to get here: previous state was mu, found an l
    # next possible: state 4
    def state3(self, input):
        if input == '(':
            self.curr_mult.append('(')
            return 4
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 4 :
    # how to get here: previous state was mul, found a (
    # next possible: state 5
    def state4(self, input):
        if input.isdigit():
            self.curr_mult.append(input)
            return 5
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 5 :
    # how to get here: previous state was mul( , found a number
    # next possible: states 6 or 8
    def state5(self, input):
        if input.isdigit():
            self.curr_mult.append(input)
            return 6
        elif input == ',':
            self.curr_mult.append(input)
            return 8
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 6 :
    # how to get here: previous state was mul(X, found a number
    # next possible: states 7 or 8
    def state6(self, input):
        if input.isdigit():
            self.curr_mult.append(input)
            return 7
        elif input == ',':
            self.curr_mult.append(input)
            return 8
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 7 :
    # how to get here: previous state was mul(XY, found a number
    # next possible: state 8
    def state7(self, input):
        if input == ',':
            self.curr_mult.append(input)
            return 8
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 8 :
    # how to get here: previous state was mul(XYZ, found a comma
    # next possible: state 9
    def state8(self, input):
        if input.isdigit():
            self.curr_mult.append(input)
            return 9
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 9 :
    # how to get here: previous state was mul(XYZ, , found a number
    def state9(self, input):
        if input.isdigit():
            self.curr_mult.append(input)
            return 10
        elif input == ')':
            self.curr_mult.append(input)
            return 12
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 10 :
    # how to get here: previous state was mul(XYZ,A, found a number
    def state10(self, input):
        if input.isdigit():
            self.curr_mult.append(input)
            return 11
        elif input == ')':
            print('in state 10 going to 12')
            self.curr_mult.append(input)
            return 12
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 11 :
    # how to get here: previous state was mul(XYZ,AB , found a number
    def state11(self, input):
        if input == ')':
            self.curr_mult.append(input)
            return 12
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 12 :
    # how to get here: previous state was mul(XYZ,ABC, found a )
    def state12(self, input):

        def get_multipliers(string_exression):
            pattern = r'\d+'
            matches = re.findall(pattern, string_exression)
            # Flatten the pairs into a single list
            numbers = [int(num) for pair in matches for num in pair]

            return matches

        if self.enable:
            product = 0
            expression_string = "".join(self.curr_mult)
            print(f'Full multiplication found! Statement is {expression_string}')
            mults = get_multipliers(expression_string)
            product = int(mults[0])*int(mults[1])
            self.product_sum = self.product_sum + product
            print(f'Current product sum is : {self.product_sum}')
        if input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            self.curr_mult = []
            if input == 'd':
                return 13
            else:
                return 0

    # state == 13 :
    # how to get here: a 'd' was detected at any point
    def state13(self, input):
        self.curr_mult = []
        if input == 'o':
            self.enable = True
            print('Found a do!')
            return 14
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            if input == 'd':
                return 13
            else:
                return 0

    # state == 14 :
    # how to get here: a 'o' was detected at state 13
    def state14(self, input):
        if input == 'n':
            return 15
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            if input == 'd':
                return 13
            else:
                return 0

    # state == 15 :
    # how to get here: a 'n' was detected at state 14
    def state15(self, input):
        if input == '\'':
            return 16
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            if input == 'd':
                return 13
            else:
                return 0

    # state == 16 :
    # how to get here: a '\'' was detected at state 15
    def state16(self, input):
        if input == 't':
            print('Found a dont!')
            return 17
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            if input == 'd':
                return 13
            else:
                return 0

    # state == 17 :
    # how to get here: a 't' was detected at state 16
    def state17(self, input):
        self.enable = False
        if input == 'd':
            return 13
        elif input == 'm':
            self.curr_mult = ['m']
            return 1
        else:
            return 0

    def state_transitions(self, input_char):
        state_machine = {
            0: self.state0,
            1: self.state1,
            2: self.state2,
            3: self.state3,
            4: self.state4,
            5: self.state5,
            6: self.state6,
            7: self.state7,
            8: self.state8,
            9: self.state9,
            10: self.state10,
            11: self.state11,
            12: self.state12,
            13: self.state13,
            14: self.state14,
            15: self.state15,
            16: self.state16,
            17: self.state17
        }
        self.state = self.nxt_state
        self.nxt_state = state_machine[self.state](input_char)



def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    sm = stateMachine()

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        for char in iter(lambda: file.read(1), ''):
            sm.state_transitions(char)

if __name__ == "__main__":
    main()