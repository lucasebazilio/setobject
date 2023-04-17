import timeit
import random

data = set(random.sample(range(100000),65535))

# test lookup time using built-in set() method
s = set(data)
t = timeit.Timer("for i in range(65535): i in s", "from __main__ import s")

# Run the test num_runs times and calculate the average time
num_runs = 500
total_time = sum(t.timeit(number=1) for _ in range(num_runs))
avg_time = total_time / num_runs
print("Average lookup time using set() over {} runs: {:.6f} seconds".format(num_runs, avg_time))
