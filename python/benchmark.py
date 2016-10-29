import random
import quickselect
import time
import numpy as np
import matplotlib.pyplot as plt

def time_execution(example_array, k, nb_example_by_size):
    times = []
    for _ in range(nb_example_by_size):
        random.shuffle(example_array)
        start = time.time()
        quickselect.quickselect(example_array, k)
        times.append(time.time()-start)
    return times

benchmark_file = open("benchmark_results.txt", "w")
mean_durations = []
example_sizes = [50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 9000, 10000, 15000, 17500, 20000, 25000]
for example_size in example_sizes:
    print(example_size)
    example_array = list(range(example_size))
    mean_duration = np.mean(time_execution(example_array, int(example_size/2), 250))
    benchmark_file.write("%d %f\n" % (example_size, mean_duration))
benchmark_file.close()
