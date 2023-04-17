import timeit
import random

data = set(random.sample(range(100000), 65535))

# test deletion time using built-in set() method
s = set(data)
num_elements = len(s)

total_time = 0
num_iterations = 500

for i in range(num_iterations):
    s = set(data)
    t = timeit.Timer("while len(s) > 0: s.discard(s.pop())", "from __main__ import s")
    total_time += t.timeit(number=1)

avg_time = total_time / num_iterations
print("Average deletion time using set():", avg_time)
