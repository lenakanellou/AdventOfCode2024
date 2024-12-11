import sys

def main():

    if len(sys.argv) > 2:
        print("Usage: python script.py <filename>")

    filename = sys.argv[1]

    spaces = []
    blocks = []
    space = False
    file_id = 0
    desc = 0
    index = 0

    with open(filename, 'r') as file:
        desc = file.read(1)    # block descriptor
        while desc:  # Loop until no more characters
            if desc.isdigit():  # Check if it's a digit
                desc = int(desc)
            else:
                break
            if space == False:
                print(f'File blocks for file {file_id}: {desc}')
                for i in range(0, desc):
                    blocks.append(file_id)
                    index += 1
                file_id += 1
                space = not space
            else:
                print(f'{desc} empty blocks')
                for i in range(0, desc):
                    blocks.append('.')
                    spaces.append(index)
                    index += 1
                space = not space
            # Read the next character
            desc = file.read(1)


    print(f'\nSpaces free at indexes: {spaces}.')

    print('\nBlock array:\n[', end='')
    for i in range(len(blocks)):
        print(f'{blocks[i]}', end='')
    print(']')

    sindex = spaces.pop(0)
    bindex = len(blocks)-1

    while bindex > sindex:
    # while len(spaces) > 0:
        if blocks[bindex] != '.':
            blocks[bindex], blocks[sindex] = blocks[sindex], blocks[bindex]
            sindex = spaces.pop(0)
        bindex -= 1
        # print('[', end='')
        # for i in range(len(blocks)):
        #     print(f'{blocks[i]}', end='')
        # print(']')

    checksum = 0
    for i, b in enumerate(blocks):
        if b == '.':
            continue
            # break
        checksum += i*b
    print(f'\nFinal checksum is: {checksum}.\n')

    return


if __name__ == "__main__":
    main()