import sys
import logging

def main():

    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <blinks>")
        sys.exit(1)

    filename = sys.argv[1]
    blinks = int(sys.argv[2])

    # Configure the logging system
    if "debug" in filename:
       logging.basicConfig(level=logging.DEBUG, format='%(funcName)s: %(message)s')  # Set to DEBUG to see debug messages
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)  # Create a logger for your script

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            stones = list(line.split(' '))

    logger.debug(f'Initially, stones is:\n{stones}')

    for j in range(0, blinks):
        # stoneslength = len(stones)
        i = 0
        while i < len(stones):
            s = stones[i]
            if int(s) == 0:
                stones[i] = '1'
            elif len(stones[i])%2 == 0:
                sstring = stones[i]
                middle = len(sstring.strip())//2
                left = sstring[0:middle]
                right = sstring[middle:].lstrip('0')
                stones[i] = left
                if right != "":
                    stones.insert(i+1, right)
                else:
                    stones.insert(i+1, '0')
                i += 1
            else:
                stones[i] = str(int(stones[i])*2024)
            i += 1
        logger.debug(f'After blinking {j+1} times:\n{stones}')



    print(f'\nAfter blinking a total of {blinks} times, there are {len(stones)} stones!')
    return

if __name__ == "__main__":
    main()