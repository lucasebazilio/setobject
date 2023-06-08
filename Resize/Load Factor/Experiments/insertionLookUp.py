import random
import timeit

data = set(random.sample(range(1000000), 1000000))

# Test insertion and lookup time using built-in set() method
s = set()
lookup_elements = random.sample(range(1000000), 1000000)  # Select 100000 random elements for lookup

def test_insert_lookup():
    s.update(data)
    for x in lookup_elements:
        x in s

# Run the insertion and lookup test num_runs times and calculate the average time
num_runs = 100
total_insert_lookup_time = timeit.timeit(test_insert_lookup, number=num_runs)
avg_insert_lookup_time = total_insert_lookup_time / num_runs
print("Average insertion and lookup time using set() over {} runs: {:.6f} seconds".format(num_runs, avg_insert_lookup_time))



