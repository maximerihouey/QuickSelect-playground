import random
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def quickselect(liste, k):
    n = k-1
    nb_iterations = 0

    def partition(array, left, right, pivotIndex):
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

    def select(array, left, right, n):
        nonlocal nb_iterations
        nb_iterations += 1
        if left == right:
            return array[left]
        pivotIndex = random.randint(left, right)
        pivotIndex = partition(array, left, right, pivotIndex)
        # The pivot is in its final sorted position
        if n == pivotIndex:
            return array[n]
        elif n < pivotIndex:
            return select(array, left, pivotIndex-1, n)
        else:
            return select(array, pivotIndex+1, right, n)
        
    selection = select(liste, 0, len(liste)-1, n)
    return selection, nb_iterations 
    
results = defaultdict(list)    
example_sizes = range(100, 5000, 200)
nb_example_by_size = 500
for example_size in example_sizes:
    print(example_size)
    example = list(range(1, example_size+1))
    example_median_index = 1 + int(example_size/2)
    example_median = int(np.median(example))
    for i in range(nb_example_by_size):
        random.shuffle(example)
        median, nb_iteration = quickselect(example, example_median_index)
        results[example_size].append(nb_iteration)
        if median != example_median_index:
            print("problem")
        
data = [values for example_size, values in results.items()]
plt.violinplot(data)

#for example_size, values in results.items():
#    plt.violinplot(values)

plt.legend(loc=0)
plt.show()
