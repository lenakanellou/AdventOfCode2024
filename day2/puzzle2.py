import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

safe_reports = 0


def check_safe_diff(difference, direction):

    if abs(difference) not in (1, 2, 3):
        return 0
    if difference > 0 and direction == False:
        return 0
    if difference < 0 and direction == True:
        return 0

    return 1

def check_report(levels):
    diff = levels[0] - levels[1]
    if diff < 0:
        direction = 'asc'
    elif diff > 0:
        direction = 'des'
    else:
        return 0 # unsafe report

    prev_level = levels[0]

    for level in levels[1:]:
        diff = prev_level - level

        if abs(diff) not in (1, 2, 3):
            return 0
        if  diff > 0 and direction != 'des':
            return 0
        if diff < 0 and direction != 'asc':
            return 0

        prev_level = level
    return 1


with open(filename, 'r') as file:
    for index, line in enumerate(file):
        levels_str = line.split()
        levels = list(map(int, levels_str))
        # print(levels)

        safe = check_report(levels)

        if safe == 1:
            print(f'Report {index} is safe!')

        else:
            for i in range(0, len(levels)):
                pd_levels = [levels[j] for j in range(len(levels)) if j != i]
                safe = check_report(pd_levels)
                if safe == 1:
                    print(f'Problem Dampener: Report {index} is safe after omitting level {i}!')
                    break

        safe_reports = safe_reports + safe

print(f'Reports that are safe: {safe_reports}')