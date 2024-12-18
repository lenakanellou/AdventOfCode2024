import sys
import re
import logging



def get_op_val(literal, regs):

    if literal >= 0 and literal < 4:
        return literal
    elif literal < 7:
        return regs[literal%4]
    else:
        print(f'Illegal operand for combo! {literal}\nReturning literal.')
        # sys.exit(1)


def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # Configure the logging system
    if "debug" in filename:
       logging.basicConfig(level=logging.DEBUG, format='%(funcName)s: %(message)s')  # Set to DEBUG to see debug messages
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)  # Create a logger for your script



    regs = [0, 0, 0]    # registers A, B, C

    ip = 0      # instruction pointer
    inc = 2     # what to add to instruction pointer; by default ==2, unless a jump instruction modifies it

    opcode = 0
    literal = 0

    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            line = line.strip()

            if match := re.search(r"Register\s+([ABC]):\s+(\d+)", line):
                register = match.group(1)
                value = int(match.group(2))  # The integer value
                if register == 'A':
                    regs[0] = value
                elif register == 'B':
                    regs[1] = value
                elif register == 'C':
                    regs[2] = value
                else:
                    print(f'Error! Invalid register ID! {register}')
                    sys.exit(1)
                logger.debug(f"Register: {register}, Value: {value}")
            elif match := re.search(r"Program:\s*([\d,]+)", line):
                numbers = match.group(1)  # Extracts the entire string of numbers
                program = [int(num) for num in numbers.split(',')]  # Splits into individual integers
                logger.debug(f'Running program: {program}')



    output = ""


    while ip < len(program):                 # emulate computer

        logger.debug(f'Instruction pointer is {ip}')
        opcode = program[ip]
        literal = program[ip+1]
        combo = get_op_val(literal, regs)
        result = 0

        if opcode == 0:     # adv
            logger.debug(f'Executing opcode ADV with operand: {combo}')
            result = regs[0] / (2**combo)
            regs[0] = int(result)
            logger.debug(f'Result is {regs[0]}')
            print(f'A = A / 2**{combo}')

        elif opcode == 1:   # bxl
            logger.debug(f'Executing opcode BXL with operand: {literal}')
            regs[1] = regs[1] ^ literal
            logger.debug(f'Result is {regs[1]}')
            print(f'B = B XOR {literal}')

        elif opcode == 2:   # bst
            logger.debug(f'Executing opcode BST with operand: {combo}')
            regs[1] = combo % 8
            logger.debug(f'Result is {regs[1]}')
            print(f'B = {combo} % 8')

        elif opcode == 3:   # jnz
            logger.debug(f'Executing opcode JNZ with operand: {literal}')
            if regs[0] != 0:
                ip = literal
                logger.debug(f'Jumping to Instruction {ip}: {program[ip]}')
                continue

        elif opcode == 4:   # bxc
            logger.debug(f'Executing opcode BXC with operand: {literal}')
            regs[1] = regs[1] ^ regs[2]
            logger.debug(f'Result is {regs[1]}')
            print('B = B XOR C')

        elif opcode == 5:   # out
            logger.debug(f'Executing opcode OUT with operand: {combo}')
            result = combo % 8
            if len(output) > 0:
                output += ','
            output += str(result)
            print(f'OUT result is {result}')

        elif opcode == 6:   # bdv
            logger.debug(f'Executing opcode BDV with operand: {combo}')
            result = regs[0] / (2**combo)
            regs[1] = int(result)
            logger.debug(f'Result is {regs[1]}')
            print(f'B = A / 2**{combo}')

        elif opcode == 7:   # cdv
            logger.debug(f'Executing opcode CDV with operand: {combo}')
            result = regs[0] / (2**combo)
            regs[2] = int(result)
            logger.debug(f'Result is {regs[2]}')
            print(f'C = A / 2**{combo}')

        else:
            print(f'Error! Invalid opcode! {opcode}')
            sys.exit(1)

        # finally, update instruction pointer
        ip += inc
        if ip > len(program):
            # print('Program halting.')
            break


    print(f'Program halting.\nFinal register file state is {regs}.\nFinal output of program is : {output}')


    return

if __name__ == "__main__":
    main()
