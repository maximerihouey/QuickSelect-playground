#include <stdio.h>
#include <stdlib.h>
#include "quickselect.h"
#include <time.h>
#include <unistd.h>

int* range(int n, int startIndex, int stepSize){
    int *array = (int *)malloc(sizeof(int) * n);
    int i;
    for(i=0; i < n; i = i + 1 ){
        array[i] = startIndex + i * stepSize;
    }
    return array;
}

void fisherYatesShuffle(int *array, int array_size){
    int i, j;
    for(i=0; i < array_size-1; i = i + 1 ){
        j = (rand() % (array_size));
        switcharoo(array, i, j);
    }
}

long* timeExecution(int *example, int example_size, int k, int nbExampleBySize){
    long *times = (long *)malloc(sizeof(long) * nbExampleBySize);
    int i;
    struct timespec start, stop;
    for(i=0; i < nbExampleBySize; i = i + 1 ){
        fisherYatesShuffle(example, example_size);
        clock_gettime(CLOCK_REALTIME, &start);
        quickselect(example, example_size, k);
        clock_gettime(CLOCK_REALTIME, &stop);
        times[i] = (stop.tv_nsec - start.tv_nsec);
    }
    return times;
}

double mean(long *array, int array_size){
    int i;
    long somme = 0;
    for(i=0; i < array_size; i = i + 1 ){
        somme += array[i];
    }
    return (double) somme / (double) array_size;
}

int main(void)
{
    int i;
    const int exampleSizes[] = {50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 9000, 10000, 15000, 17500, 20000, 25000};
    int nbExampleBySize = 250;
    int *example;
    long temp_somme;
    int example_size;
    double mean_duration;
    FILE *f = fopen("benchmark_results.txt", "w");

    for(i=0; i < 19; i = i + 1 ){
        example_size = exampleSizes[i];
        example = range(example_size, 1, 1);
        mean_duration = mean(timeExecution(example, example_size, example_size/2, nbExampleBySize), nbExampleBySize);

        printf("%i\n", example_size);
        fprintf(f, "%i %.10f\n", example_size, mean_duration / 1000000000L);
    }
    fclose(f);
}



