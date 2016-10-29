import random
cimport cython
from cpython cimport array
import array

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef int partition(int[:] table, int left, int right, int pivotIndex):
    cdef int pivotValue = table[pivotIndex]
    cdef int storeIndex = left
    cdef int i
    # Move pivot to end
    table[pivotIndex], table[right] = table[right], table[pivotIndex]
    for i in range(left, right):
        if table[i] < pivotValue:
            table[storeIndex], table[i] = table[i], table[storeIndex]
            storeIndex += 1
    # Move pivot to its final place
    table[right], table[storeIndex] = table[storeIndex], table[right]
    return storeIndex

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef int select(int[:] table, int left, int right, int n):
    cdef int pivotIndex
    if left == right:
        return table[left]
    pivotIndex = random.randint(left, right)
    pivotIndex = partition(table, left, right, pivotIndex)
    # The pivot is in its final sorted position
    if n == pivotIndex:
        return table[n]
    elif n < pivotIndex:
        return select(table, left, pivotIndex-1, n)
    else:
        return select(table, pivotIndex+1, right, n)


cpdef int quickselect(list liste, int k):
    cdef array.array a = array.array('i', liste)
    cdef int[:] table = a
    return select(table, 0, len(table)-1, k-1)
