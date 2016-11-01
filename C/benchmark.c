#include <stdio.h>
#include <stdlib.h>
#include "quickselect.h"


int main(void)
{
    int i;
    int example_size = 11;
    int *example = (int *)malloc(sizeof(int) * example_size);

    for(i=0; i < example_size; i = i + 1 ){
        example[i] = example_size - i;
    }
    for(i=0; i < example_size; i = i + 1 ){
        printf("%i\n", example[i]);
    }

    printf("%i\n", quickselect(example, example_size, 6));

}
