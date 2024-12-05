import sys


def main():

    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit

    filename = sys.argv[1]
    process_updates = False
    is_pre_req_dict = {}
    error = False
    middles_sum = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if process_updates == True:
                line = line.split(',')
                print(f'Processing update {line}')
                for i, pagenum in enumerate(line):
                    error = False
                    print(f'Index is {i}, pagenum is {pagenum}.')
                    if pagenum in is_pre_req_dict.keys():
                        successors = is_pre_req_dict[pagenum]
                    else:
                        successors = []
                    for p in range(0, i):
                        if line[p] in successors:
                            print('Error detected!')
                            error = True
                            break
                    if error == True:
                        print('Invalid Update! Checking next...')
                        break
                if error == False:
                    middles_sum += int(line[len(line) // 2])
            else:
                if line == "":
                    process_updates = True
                else:
                    print(f'Adding line {line} to hash table')
                    line = line.split('|')
                    if line[0] in is_pre_req_dict.keys():
                        successors = is_pre_req_dict[line[0]]
                    else:
                        successors = []
                    successors.append(line[1])
                    is_pre_req_dict[line[0]] = successors
                    print(f'Successors for page {line[0]} are : {successors}')

    print(f'Update checking concluded. Sum of middles is {middles_sum}.')

    return

if __name__ == "__main__":
    main()