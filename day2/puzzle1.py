import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

safe_reports = 0

with open(filename, 'r') as file:
    for index, line in enumerate(file):
        levels_str = line.split()
        levels = list(map(int, levels_str))
        # print(levels)
        diff = levels[0] - levels[1]
        if abs(diff) in (1, 2, 3) :
            if diff > 0 :
                descending = True
            else :
                descending = False

            prev_level = levels[1]

            safe = 1
            for level in levels[2:]:
                diff = prev_level - level
                prev_level = level

                if abs(diff) not in (1, 2, 3):
                    print(f'Incorrect distance range. Report {index} not safe!')
                    safe = 0
                    break
                if diff > 0 and not descending:
                    print(f'Descending levels in ascending report. Report {index} not safe!')
                    safe = 0
                    break
                if diff < 0 and descending:
                    print(f'Ascending levels in descending report. Report {index+1} not safe!')
                    safe = 0
                    break

            safe_reports = safe_reports + safe

print(f'Reports that are safe: {safe_reports}')