import sys


def main():

    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit

    filename = sys.argv[1]
    process_updates = False
    pre_reqs_dict = {}

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if process_updates == True:
                print(f'Processing update {line}')
                for i, pagenum in enumerate(line):
                    pre_reqs = pre_reqs_dict[pagenum]
                    for p in range(0, i):

            else:
                if line == "":
                    process_updates = True
                else:
                    print(f'Adding line {line} to hash table')
                    line = line.split('|')
                    if line[1] in pre_reqs_dict.keys():
                        pre_reqs = pre_reqs_dict[line[1]]
                    else:
                        pre_reqs = []
                    pre_reqs.append(line[0])
                    pre_reqs_dict[line[1]] = pre_reqs
                    print(f'Pre-requisites for page {line[1]} are : {pre_reqs}')

    return

if __name__ == "__main__":
    main()