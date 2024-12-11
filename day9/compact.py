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
                spaces.append((index, desc))
                for i in range(0, desc):
                    blocks.append('.')
                    index += 1
                space = not space
            # Read the next character
            desc = file.read(1)


    print(f'\nSpaces free at indexes: {spaces}.')

    print('\nBlock array:\n[', end='')
    for i in range(len(blocks)):
        print(f'{blocks[i]}', end='')
    print(']')

    # sindex = spaces.pop(0)
    sindex = 0
    bindex = len(blocks)-1
    id = '.'
    blocksize = 0
    blockstart = 0
    blockend = 0

    while bindex >= 0:
        if blocks[bindex] != id: # block id change
            if blocksize != 0: # can only be non-zero if previous block had IDs
                print(f'Blocksize is {blocksize}.')
                # time to find a suitable space
                for s, space in enumerate(spaces):
                    if space[1] >= blocksize and space[0] < bindex:
                        chosenspace = s
                        print(f'Space to use: {space} at index {s} in spaces.')
                        for i in range(0, blocksize):
                            print(f'Moving block with ID {blocks[bindex+blocksize-i]} from position {bindex+blocksize-i} to position {space[0]+i}.')
                            blocks[space[0]+i] = blocks[bindex+blocksize-i]
                            blocks[bindex+blocksize-i] = '.'
                        if space[1] == blocksize:
                            spaces.pop(chosenspace)
                            print(f'Space {s} is now deleted from list.')
                        else:
                            spaces[chosenspace] = (space[0]+blocksize, space[1]-blocksize)
                            print(f'Space at index {chosenspace} is now {spaces[chosenspace]}')
                        print('[', end='')
                        for i in range(len(blocks)):
                            print(f'{blocks[i]}', end='')
                        print(']')
                        break
            if blocks[bindex] != '.':
                print(f'Found new block with id {blocks[bindex]}')
                blockstart = bindex
            #     print(f'Total block size is {blocksize}')
                blocksize = 1
            # # print(blocks[bindex])
            else:
                blocksize = 0
        else:   # parsing same id or sequence of spaces
            if blocks[bindex] != '.':
                blocksize += 1
        id = blocks[bindex]

        bindex -= 1



    if blocksize != 0:
        print(f'Blocksize is {blocksize}.')

    print('[', end='')
    for i in range(len(blocks)):
        print(f'{blocks[i]}', end='')
    print(']')



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