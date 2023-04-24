import random
import timeit

s = set()

# Run the test num_run times and calculate the average time
num_runs = 3
total_time = 0

data = set(random.sample(range(100000),65529))

for i in range(num_runs):
    s = set()
    data = set(random.sample(range(100000), 65529))
    for x in data: s.add(x)
    s.add(100101)

    
# Results
# B = 9 -> Linear Probes: 958004  Random Probes: 80549
