package io.github.maximerihouey;

import java.util.concurrent.ThreadLocalRandom;

/**
 * Created by maxime on 30/10/16.
 */
public class Quickselect {

    public static void switcharoo(int[] array, int index1, int index2){
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    public static int partition(int[] array, int left, int right, int pivotIndex){
        int pivotValue = array[pivotIndex];
        int storeIndex = left;
        switcharoo(array, pivotIndex, right);
        for(int i=left; i <= right; i++){
            if(array[i] < pivotValue){
                switcharoo(array, storeIndex, i);
                storeIndex += 1;
            }
        }
        switcharoo(array, storeIndex, right);
        return storeIndex;
    }

    public static int select(int[] array, int left, int right, int n){
        if(left == right){
            return array[left];
        }
        int pivotIndex = ThreadLocalRandom.current().nextInt(left, right+1);
        pivotIndex = partition(array, left, right, pivotIndex);
        if(n == pivotIndex){
            return array[n];
        }else if(n < pivotIndex){
            return select(array, left, pivotIndex-1, n);
        }else{
            return select(array, pivotIndex+1, right, n);
        }
    }

    public static int quickselect(int[] array, int k){
        return select(array, 0, array.length-1, k-1);
    }
}
