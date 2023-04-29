import random
import timeit

s = set()

# Run the test num_run times and calculate the average time
num_runs = 400
total_time = 0


for i in range(num_runs):
    s = set()
    data = set(random.sample(range(100000), 65535))   
    for x in data: s.add(x) # amount = K-1
    s.add(100101)           # amount = K
    
 
# Once size K is reached , total number of linear probes and random probes are displayed
    
 
