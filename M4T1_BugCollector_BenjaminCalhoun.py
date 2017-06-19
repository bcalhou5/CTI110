# Bug Collector
# 06/18/17
# CTI-110 M4T1 - Bug Collector
# Benjamin Calhoun

# Initialize the accumulator.

total = 0

# Get the bugs collected for each day.

for day in range(1, 6):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total = total + bugs

# Display the total bugs.
print('You have collected a total of', total, 'bugs.')
