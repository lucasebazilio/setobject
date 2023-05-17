import random

# Create a set with random even elements

num_runs = 400


for i in range(num_runs):
    s = set()

    data = set(random.sample(range(0, 200000, 2),10000))
    # Perform unsuccessful lookups for random odd numbers
    #data1 = set(random.sample(range(1, 131072, 2), 1000))
    times = 0
    while (times <= 10000):
        odd_number = random.randint(1, 20000) * 2 + 1
        c = odd_number in data
        times = times + 1
