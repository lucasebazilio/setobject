import random
import timeit

data = set(random.sample(range(100000),65535))


s = set()

t = timeit.Timer("s.update(data)", "from __main__ import s, data")

# Run the test num_runs times and calculate the average time
num_runs = 500
total_time = sum(t.timeit(number=1) for _ in range(num_runs))
avg_time = total_time / num_runs
print("Average insertion time using set() over {} runs: {:.6f} seconds".format(num_runs, avg_time))

