import random
import timeit

s = set()

# Run the test num_run times and calculate the average time
num_runs = 50
total_time = 0

data = set(random.sample(range(100000),65529))

for i in range(num_runs):
    data = set(random.sample(range(100000), 65529))
    for x in data: s.add(x)
    s.add(100101)
    s.clear()
