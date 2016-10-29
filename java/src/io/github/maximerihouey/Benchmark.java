package io.github.maximerihouey;

/**
 * Created by maxime on 30/10/16.
 */
public class Benchmark {

    public static void main(String args[]){
        int example_size = 11;
        int[] example = new int[example_size];
        for(int i=0; i < example_size; i++){
            example[i] = i + 1;
        }
        for(int i=0; i < example_size; i++){
            System.out.println(example[i]);
        }
        System.out.println("Median: "+ Quickselect.quickselect(example, 6));
    }
}
