package io.github.maximerihouey;

import java.util.concurrent.ThreadLocalRandom;
import java.util.Arrays;

/**
 * Created by maxime on 30/10/16.
 */
public class Test {

    public static void main(String args[]){
        int arraySize = 100000;
        int[] example = new int[arraySize];
        for(int i=0; i < arraySize; i++){
            example[i] = ThreadLocalRandom.current().nextInt(500);
        }
        int[] example1 = example.clone();
        int[] example2 = example.clone();

        // QuickSelect
        long start1 = System.nanoTime();
        int median1 = Quickselect.quickselect(example1, arraySize/2);
        long duration1 = System.nanoTime() - start1;
        System.out.println("Median: " + median1 + " | Duration: " + duration1);

        // Sorting
        long start2 = System.nanoTime();
        Arrays.sort(example2);
        int median2 = example2[arraySize/2-1];
        long duration2 = System.nanoTime() - start2;
        System.out.println("Median: " + median2 + " | Duration: " + duration2);
    }
}
