package io.github.maximerihouey;

import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.*;
import java.io.*;

/**
 * Created by maxime on 30/10/16.
 */
public class Benchmark {

    public static int[] range(int n, int startIndex, int stepSize){
        int[] array = new int[n];
        for(int i=0; i < n; i++){
            array[i] = startIndex + i * stepSize;
        }
        return array;
    }

    public static void fisherYatesShuffle(int[] array){
        for(int i=0; i <= array.length-2; i++){
            int j = ThreadLocalRandom.current().nextInt(array.length - 1);
            Quickselect.switcharoo(array, i, j);
        }
    }

    public static long[] timeExecution(int[] example, int k, int nbExampleBySize){
        long[] times = new long[nbExampleBySize];
        for(int i=0; i < nbExampleBySize; i++){
            fisherYatesShuffle(example);
            long start = System.nanoTime();
            Quickselect.quickselect(example, k);
            times[i] = System.nanoTime() - start;
        }
        return times;
    }

    public static void main(String args[]){
        // FileWriter
        File file = new File("../benchmark_results.txt");
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter(file));

            int[] exampleSizes = {50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 9000, 10000, 15000, 17500, 20000, 25000};
            int nbExampleBySize = 250;

            for(int i=0; i < exampleSizes.length; i++){
                int exampleSize = exampleSizes[i];
                System.out.println(exampleSize);
                int[] example = range(exampleSize, 1, 1);
                int medianIndex = exampleSize/2;
                long[] times = timeExecution(example, medianIndex, nbExampleBySize);
                long sum = LongStream.of(times).sum();
                bw.write(exampleSize + " " + sum/(times.length * Math.pow(10, 9)) + "\n");
            }

            bw.close();
        } catch (IOException exception) {
            System.out.println("Unable to open file");
        }
    }
}
