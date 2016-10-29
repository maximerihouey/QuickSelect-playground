package io.github.maximerihouey
import scala.collection.mutable.ListBuffer;
import java.io._

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

    // FileWriter
    val file = new File("benchmark_results.txt")
    val bw = new BufferedWriter(new FileWriter(file))

    //val exampleSizes = range(10, 100, 100);
    val exampleSizes = Array[Int](50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 9000, 10000, 15000, 17500, 20000, 25000);
    val nbExampleBySize = 250;

    for(exampleSize <- exampleSizes) {
      println("%s".format(exampleSize))
      val example = range(exampleSize, 1, 1);
      val medianIndex = exampleSize/2;
      val times = timeExecution(example, medianIndex, nbExampleBySize);
      bw.write("%s %s\n".format(exampleSize, times.sum.toFloat / (times.length * scala.math.pow(10,9))));
    }

    bw.close()
  }
}
