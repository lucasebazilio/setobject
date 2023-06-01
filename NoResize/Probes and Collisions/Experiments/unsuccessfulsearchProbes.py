import random

num_runs = 400

for i in range(num_runs):
    # Create a set with random even elements
    data = set(random.sample(range(0, 200000, 2),2000))

    times = 0
    while (times < 2000):   # Perform S searches
        odd_number = random.randint(1, 200000) * 2 + 1
        c = odd_number in data
        times = times + 1
    data.add(200001)





