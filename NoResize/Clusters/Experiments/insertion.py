import random
import timeit

s = set()


num_runs = 500

for i in range(num_runs):
    s = set()
    data = set(random.sample(range(100000),39999))  # Second argument is the amount S of filled entries
    for x in data: s.add(x)
    s.add(100102)
