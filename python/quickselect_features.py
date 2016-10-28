import random
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def quickselect(array, k, pivot_method, return_nb_iterations=False):
    """ 
    Return the k-th smallest element of the array (indices start at 1)
    """
    n = k-1
    nb_iterations = 0

    def partition(left, right, pivotIndex):
        pivotValue = array[pivotIndex]
        # Move pivot to end
        array[pivotIndex], array[right] = array[right], array[pivotIndex]
        storeIndex = left
        for i in range(left, right):
            if array[i] < pivotValue:
                array[storeIndex], array[i] = array[i], array[storeIndex]
                storeIndex += 1
        # Move pivot to its final place
        array[right], array[storeIndex] = array[storeIndex], array[right]
        return storeIndex

    def select(left, right):
        # Updating number of iterations
        nonlocal nb_iterations
        nb_iterations += right-left
        # actual implementation
        if left == right:
            return array[left]
        pivotIndex = pivot_method(left, right)
        pivotIndex = partition(left, right, pivotIndex)
        # The pivot is in its final sorted position
        if n == pivotIndex:
            return array[n]
        elif n < pivotIndex:
            return select(left, pivotIndex-1)
        else:
            return select(pivotIndex+1, right)

    if return_nb_iterations:
        return select(0, len(array)-1), nb_iterations
    else:
        return select(0, len(array)-1)


# Pivot strategies
pivot_random = lambda left, right : random.randint(left, right)
pivot_median = lambda left, right : int((left+right)/2)
pivot_first = lambda left, right : left
pivot_last = lambda left, right : right
#pivots = [("random", pivot_random), ("median", pivot_median), ("first", pivot_first), ("last", pivot_last)]
pivots = [("random", pivot_random)]

# Computation
example_sizes = range(100, 5000, 100)
example_sizes = [50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 9000, 10000]
nb_example_by_size = 100
colors = ["b", "r", "g", "y"]

confidence_intervals = defaultdict(lambda : defaultdict(list))
for example_size in example_sizes:
    print(example_size)
    results = defaultdict(list)
    example = list(range(1, example_size+1))
    example_median_index = 1 + int(example_size/2)
    example_median = int(np.median(example))
    for i in range(nb_example_by_size):
        random.shuffle(example)
        for pivot_name, pivot_method in pivots:
            median, nb_iteration = quickselect(
                example, example_median_index, pivot_method, return_nb_iterations=True
            )
            results[pivot_name].append(nb_iteration)
    
    for pivot_name, _ in pivots:
        values = results[pivot_name]
        confidence_intervals[pivot_name][example_size] = (
            quickselect(values, int(nb_example_by_size*0.25), pivot_random),
            quickselect(values, int(nb_example_by_size*0.5), pivot_random),
            quickselect(values, int(nb_example_by_size*0.75), pivot_random)
        )

for (pivot_name, _), color in zip(pivots, colors):
    lower_bound = [lower for _, (lower, prediction, upper) in confidence_intervals[pivot_name].items()]
    prediction_bound = [prediction for _, (lower, prediction, upper) in confidence_intervals[pivot_name].items()]
    upper_bound = [upper for _, (lower, prediction, upper) in confidence_intervals[pivot_name].items()]

    #    plt.plot(example_sizes, lower_bound, color+":")
    plt.plot(example_sizes, prediction_bound, color, label=pivot_name)
    #    plt.plot(example_sizes, upper_bound, color+":")

plt.legend(loc=0)
plt.show()


#data = [values for example_size, values in results.items()]
#plt.violinplot(data)
#for example_size, values in results.items():
#    plt.violinplot(values)
