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

Schematically each implementation consist in a file "Quickselect" (with the implementation of the algorithm) and a file "Benchmark" that uses "Quickselect" as a library to conduct the benchmark.

For each implementation executing the "Benchmark" will output a file "benchmark_results.txt" in the implementation's directory. Those results are then aggregated by the "benchmark.py" script at the root of the repositiory in order to produce the graph.

<b>Caution:</b> The methods detailed below might not be the best way of compiling/executing thoses type of scripts, those are just indications of how those files were tested during their writing

### Python

The code is written in Python 3.5 (3.5.2)
<pre>
quickselect-playground/python$ <b>python benchmark.py</b>
</pre>

### Cython

For Cython we first need to build the Cython file of the QuickSelect library (to know more about Cython [Go here](http://docs.cython.org/en/latest/src/tutorial/cython_tutorial.html))
<pre>
quickselect-playground/cython$ <b>python setup.py build_ext --inplace</b>
</pre>

Then we can just call the benchmark python file (which is identical to the python implemention)
<pre>
quickselect-playground/cython$ <b>python benchmark.py</b>
</pre>

### Scala

The code is written in Scala 2.11 (2.11.8) and SBT 0.13 (0.13.8).

We need first to compile the source code
<pre>
quickselect-playground/scala$ <b>sbt clean package</b>
</pre>

Then to execute the benchmark,
<pre>
quickselect-playground/scala$ <b>$SPARK_HOME/bin/spark-submit --class "io.github.maximerihouey.Benchmark" target/scala-2.11/scala_2.11-1.0.jar</b>
</pre>

### Java

The code is written in Java 1.8 (1.8.0_101).

We need first to compile the source code. <b>Caution:</b> this is executed from java/src folder
<pre>
quickselect-playground/java/src$ <b>javac io/github/maximerihouey/Quickselect.java io/github/maximerihouey/Benchmark.java</b>
</pre>

Then to execute the benchmark,
<pre>
quickselect-playground/java/src$ <b>java io.github.maximerihouey.Benchmark</b>
</pre>

