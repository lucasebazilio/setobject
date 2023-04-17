import random
import timeit

s = set()

# Run the test num_run times and calculate the average time
num_runs = 500
total_time = 0

data = set(random.sample(range(100000),65535))

for i in range(num_runs):
    data = set(random.sample(range(100000), 65535))
    s.clear()
    t = timeit.Timer("s.update(data)", "from __main__ import s, data")
    total_time += t.timeit(number=1)

avg_time = total_time / num_runs
print("Average insertion time using set() over {} runs: {:.6f} seconds".format(num_runs, avg_time))
