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
    corrected_middles_sum = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if process_updates == True:
                line = line.split(',')
                print(f'Processing update {line}')
                # for i, pagenum in enumerate(line):
                i = 0
                error = False
                while i < len(line):
                    print(f'Index is {i}, pagenum is {line[i]}.')
                    if line[i] in is_pre_req_dict.keys():
                        successors = is_pre_req_dict[line[i]]
                    else:
                        successors = []
                    for p in range(0, i):
                        print(f'p is {p}')
                        if line[p] in successors:
                            if error == False:
                                print('Error detected!')
                            error = True
                            line[p], line[i] = line[i], line[p]
                            print(line)
                            # break
                    # if error == True:
                    #     print('Invalid Update! Checking next...')
                    #     break
                    i += 1
                if error == False:
                    middles_sum += int(line[len(line) // 2])
                else:
                    print(f'Corrected update is : {line}')
                    corrected_middles_sum += int(line[len(line) // 2])
            else:
                if line == "":
                    process_updates = True
                else:
                    # print(f'Adding line {line} to hash table')
                    line = line.split('|')
                    if line[0] in is_pre_req_dict.keys():
                        successors = is_pre_req_dict[line[0]]
                    else:
                        successors = []
                    successors.append(line[1])
                    is_pre_req_dict[line[0]] = successors
                    # print(f'Successors for page {line[0]} are : {successors}')

    print(f'Update checking concluded. Sum of middles is {middles_sum}. Sum of corrected is {corrected_middles_sum}')

    return

if __name__ == "__main__":
    main()