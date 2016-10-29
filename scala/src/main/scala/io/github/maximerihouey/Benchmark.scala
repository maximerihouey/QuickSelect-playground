package io.github.maximerihouey

/**
  * Created by maxime on 29/10/16.
  */
object Benchmark {

  def main(args: Array[String]) {
    val example_size: Int = 21
    val example = new Array[Int](example_size)
    for (i <- 0 to (example.length - 1)) {
      example(i) = i + 1;
      println(example(i));
    }
    println("Length: %s".format(example.length))
    val median = Quickselect.quickselect(example, 11)
    println("Median: %s".format(median))
  }
}
