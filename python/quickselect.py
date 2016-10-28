import random

def quickselect(array, k):
    """ 
    Return the k-th smallest element of the array (indices start at 1)
    """
    n = k-1

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
        if left == right:
            return array[left]
        pivotIndex = random.randint(left, right)
        pivotIndex = partition(left, right, pivotIndex)
        # The pivot is in its final sorted position
        if n == pivotIndex:
            return array[n]
        elif n < pivotIndex:
            return select(left, pivotIndex-1)
        else:
            return select(pivotIndex+1, right)
        
    return select(0, len(array)-1)
    
# Main example
def main():
    example_array = list(range(1, 11+1))
    print("Initial array:  %s" % str(example_array))
    random.shuffle(example_array)
    print("Shuffled array: %s" % str(example_array))
    print("Median: %d" % quickselect(example_array, 6))
    print("Smallest: %d" % quickselect(example_array, 1))
    print("Biggest: %d" % quickselect(example_array, 11))

if __name__ == "__main__":
    main()
