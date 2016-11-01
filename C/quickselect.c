#include <stdio.h>
#include <stdlib.h>
#include "quickselect.h"

void switcharoo(int *array, int index1, int index2) {
    int temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
}

int partition(int *array, int left, int right, int pivotIndex) {
    int pivotValue = array[pivotIndex];
    int storeIndex = left;
    int i;
    /* Move pivot to end */
    switcharoo(array, pivotIndex, right);
    for(i=left; i < right; i = i + 1 ){
        if(array[i] < pivotValue){
            switcharoo(array, storeIndex, i);
            storeIndex += 1;
        }
    }
    /* Move pivot to its final place */
    switcharoo(array, storeIndex, right);

    return storeIndex;
}

int qselect(int *array, int left, int right, int n) {
    int pivotIndex;
    if(left == right){
        return array[n];
    }
    pivotIndex = left + (rand() % (right-left+1)); /* random int left <= x <= right */
    pivotIndex = partition(array, left, right, pivotIndex);
    /* The pivot is in its final sorted position */
    if(n == pivotIndex){
        return array[n];
    }else if(n < pivotIndex){
        return qselect(array, left, pivotIndex-1, n);
    }else{
        return qselect(array, pivotIndex+1, right, n);
    }
}

int quickselect(int *array, int array_size, int k){
    return qselect(array, 0, array_size-1, k-1);
}
