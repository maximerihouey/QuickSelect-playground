package io.github.maximerihouey
import scala.collection.mutable.ListBuffer;

/**
  * Created by maxime on 29/10/16.
  */
object Benchmark {

  def range(n: Int, startIndex: Int, stepSize: Int): Array[Int] = {
    val array = new Array[Int](n);
    for (i <- 0 to (n - 1)) {
      array(i) = startIndex + i * stepSize;
    }
    return array;
  }

  def fisherYatesShuffle(array: Array[Int]) = {
    //    -- To shuffle an array a of n elements (indices 0..n-1):
    //    for i from 0 to n−2 do
    //      j ← random integer such that i ≤ j < n
    //    exchange a[i] and a[j]
    for(i <- 0 to array.length-2) {
      val j = i + scala.util.Random.nextInt(array.length - i);
      Quickselect.switch(array, i, j);
    }
  }

  def timeExecution(example: Array[Int], k: Int, nbExampleBySize: Int): ListBuffer[Long] = {
    var times = new ListBuffer[Long]();
    for(i <- 1 to nbExampleBySize) {
      fisherYatesShuffle(example)
      val start = System.nanoTime();
      Quickselect.quickselect(example, k);
      times += System.nanoTime() - start;
    }
    return times;
  }

  def main(args: Array[String]) {

    val exampleSizes = range(10, 100, 100);
    val nbExampleBySize = 10;

    for(exampleSize <- exampleSizes) {
      println("%s".format(exampleSize))
      val example = range(exampleSize, 1, 1);
      val medianIndex = exampleSize/2;
      val times = timeExecution(example, medianIndex, nbExampleBySize);
      println("> %s".format(times.length));
    }
  }
}
