import random
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def quickselect(array, k, pivot="random", return_nb_iterations=False):
    """ 
    Return the k-th smallest element of the array (indices start at 1)
    """
    n = k-1
    nb_iterations = 0
    if pivot == "random":
        pivot_method = lambda left, right : random.randint(left, right)
    elif pivot == "median":
        pivot_method = lambda left, right : int((left+right)/2)
    elif pivot == "first":
        pivot_method = lambda left, right : left
    elif pivot == "last":
        pivot_method = lambda left, right : right

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
        nb_iterations += 1
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
    
results = defaultdict(list)
example_sizes = range(100, 500, 100)
# example_sizes = [50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 9000, 10000]
nb_example_by_size = 1000
pivots = ["random", "median", "first", "last"]
colors = ["b", "r", "g", "y"]

for pivot, color in zip(pivots, colors):
    print(pivot)
    for example_size in example_sizes:
        print(example_size)
        example = list(range(1, example_size+1))
        example_median_index = 1 + int(example_size/2)
        example_median = int(np.median(example))
        for i in range(nb_example_by_size):
            random.shuffle(example)
            median, nb_iteration = quickselect(example, example_median_index, pivot=pivot, return_nb_iterations=True)
            results[example_size].append(nb_iteration)
            if median != example_median_index:
                print("problem")

    confidence_intervals = {}
    for example_size, values in results.items():
        confidence_intervals[example_size] = (
            quickselect(values, int(nb_example_by_size*0.25)),
            quickselect(values, int(nb_example_by_size*0.5)),
            quickselect(values, int(nb_example_by_size*0.25))
        )

    lower_bound = [lower for _, (lower, prediction, upper) in confidence_intervals.items()]
    prediction_bound = [prediction for _, (lower, prediction, upper) in confidence_intervals.items()]
    upper_bound = [upper for _, (lower, prediction, upper) in confidence_intervals.items()]

#    plt.plot(example_sizes, lower_bound, color+":")
    plt.plot(example_sizes, prediction_bound, color, label=pivot)
#    plt.plot(example_sizes, upper_bound, color+":")

plt.legend(loc=0)
plt.show()


#data = [values for example_size, values in results.items()]
#plt.violinplot(data)
#for example_size, values in results.items():
#    plt.violinplot(values)
