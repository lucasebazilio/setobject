import random
import timeit

s = set()

# Run the test num_run times (Number of linear probes and random probes will be displayed)
num_runs = 5
total_time = 0

data = set(random.sample(range(100000),65530))

for i in range(num_runs):
    for x in data: s.add(x)
    s.clear()
