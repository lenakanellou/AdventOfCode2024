import sys
import logging

def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    total_price = 0
    prev_line_plots = []
    curr_line_plots = []
    plots = []  # the total plots, by number id, not by character id
    active_plots = {} # will store key: the character id, and value: current area and perimeter
    active_ids = set()


    # Configure the logging system
    if "debug" in filename:
       logging.basicConfig(level=logging.DEBUG, format='%(funcName)s: %(message)s')  # Set to DEBUG to see debug messages
    else:
        logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)  # Create a logger for your script

    with open(filename, 'r') as file:
        for line in file:
            line = list(line.strip())

            for i, id in enumerate(line):
                if i != 0:
                    if len(curr_line_plots) == 0:
                        start = 0
                    if id != line[i-1]:
                        curr_line_plots.append([line[i-1], i-start])
                        start = i
                    if i == len(line)-1:
                        curr_line_plots.append([id, i-start+1])

            prev_line_plots = curr_line_plots
            curr_line_plots = []
            logger.debug(prev_line_plots)



    for plot in plots:
        logger.debug(f'Plot with plant {plot[0]} has area {plot[1]} and perimenter {plot[2]}.')

    print(f'\nTotal fence price for the plot: {total_price}')
    return

if __name__ == "__main__":
    main()