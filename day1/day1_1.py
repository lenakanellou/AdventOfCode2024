import bisect
import sys

# Check if a filename was provided
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# Read the filename from the command line
filename = sys.argv[1]

# Initialize empty lists to store the numbers
llist = []
rlist = []
dlist = []
sim_score = []

distance_sum = 0

# Open the file in read mode
with open(filename, 'r') as file:
    for line in file:
        # Split the line into two parts and convert to numbers
        parts = line.split()
        if len(parts) == 2:  # Ensure the line has exactly two parts
            left, right = map(int, parts)  # Convert to int
            print(f'Left is {left}, right is {right}')
            # llist.append(left))
            bisect.insort(llist, left)
            # rlist.append(right))
            bisect.insort(rlist, right)

print(f'Left list ordered is {llist}.\n Right list ordered is {rlist}.')

for l, r in zip(llist, rlist):
    distance_sum = distance_sum + abs(l - r)
    dlist.append(abs(l - r))

print(f"The distance of the lists is {distance_sum}.")


for i, l in enumerate(llist):
    sim_score.append(0)
    for r in rlist:
        if l == r:
            sim_score[i] = sim_score[i] + 1
    sim_score[i] = sim_score[i] * l

print(f"The similarity score list is: {sim_score}. The similarity score is {sum(sim_score)}.")

# Output the results
# print("Left List:", llist)
# print("Right List:", rlist)