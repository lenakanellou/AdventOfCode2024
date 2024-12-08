import sys

def try_op(left, right, result):
    # base case
    print(f'Result is {result}')
    if len(right) == 1:
        res = left * int(right[0])
        print(f'Multiplying {left} by {right[0]}: {res}')
        if res == result:
            return True
        res = left + int(right[0])
        print(f'Adding {left} and {right[0]}: {res}')
        if res == result:
            return True
        else:
            return False
    else:
        print(f'Multiplying {left} by {right[0]}:')
        if try_op((left+int(right[0])), right[1:], result) == True:
            return True
        print(f'Adding {left} to {right[0]}:')
        if try_op((left*int(right[0])), right[1:], result) == True:
            return True
        return False


def main():
    if len(sys.argv) > 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    valid_sum = 0

    with open(filename, 'r') as file:
        print(f'Opening file {filename}')
        for line in file:
            line = line.strip()
            line = list(line.split(' '))
            result = int(line[0].strip(":"))
            print(line)
            res = try_op(int(line[1]), line[2:], result)
            if res == True:
                print('This line is valid!')
                valid_sum += result
            else:
                print('Invalid line!')

    print(f'Valid result sum is {valid_sum}')

if __name__ == "__main__":
    main()