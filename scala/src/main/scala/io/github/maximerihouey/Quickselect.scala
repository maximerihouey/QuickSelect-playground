package io.github.maximerihouey

/**
  * Created by maxime on 28/10/16.
  */
object Quickselect {

  def partition(array:Array[Int]) = {
    array(0) = 100;
  }

  def main(args: Array[String]) {
    val example_size: Int = 11
    var example = new Array[Int](example_size)
    for (i <- 0 to (example.length - 1)) {
      example(i) = i + 1;
    }

    println("Length: %s".format(example.length))
    for (i <- 0 to (example.length - 1)) {
      println(example(i));
    }
    partition(example)
    println("Length: %s".format(example.length))
    for (i <- 0 to (example.length - 1)) {
      println(example(i));
    }
  }
}
