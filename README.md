# Quickselect playground

The QuickSelect algorithm alloys to find the k-th smallest element of an unordered list, yielding performances on-average better than if we had to previously order the list. This algorithm is particularly usefull when computing the median of an unordered list. For more explanations see the Wikipedia article [Quickselect](https://en.wikipedia.org/wiki/Quickselect).

This repository contains several implementations of the Quickselect algorithm:
- Python
- Cython
- Scala
- Java

## Comparing the mean execution time

The implementations of the algorithm are compared by computing the median of lists of different sizes. For each list size we build the array `[1, ..., list_size]` and time the execution of 250 Quickselect computations, the array is shuffle between each computation, the mean of those computations represent the mean execution time for that algorithm.

![Benchmark](https://github.com/maximerihouey/QuickSelect-playground/blob/master/quickselect_benchmark.png)

## Executing the benchmark

### Python

The code is written in Python 3 (3.5)
<pre>
quickselect-playground/python$ <b>python benchmark.py</b>
<pre>

### Cython

For Cython we first need to build the Cython file of the QuickSelect library (to know more about Cython [Go here](http://docs.cython.org/en/latest/src/tutorial/cython_tutorial.html))
```
quickselect-playground/cython$ python setup.py build_ext --inplace
```

Then we can just call the banchmark python file (which is identical to the python implemention)
```
quickselect-playground/cython$ python benchmark.py
```

### Scala


