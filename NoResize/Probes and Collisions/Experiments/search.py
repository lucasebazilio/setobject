# test lookup time using built-in set() method

# Run the test num_run times and calculate the average time
num_runs = 5
total_time = 0


for i in range(num_runs):
    s = set(random.sample(range(100000),65530))
    t = timeit.Timer("for i in range(100000): i in s", "from __main__ import s")
    total_time += t.timeit(number=1)

avg_time = total_time / num_runs
print("Average insertion time using set() over {} runs: {:.6f} seconds".format(num_runs, avg_time))
