package io.github.maximerihouey

/**
  * Created by maxime on 28/10/16.
  */
object Quickselect {

  def switch(array: Array[Int], index1: Int, index2: Int) = {
    val temp = array(index1);
    array(index1) = array(index2);
    array(index2) = temp;
  }

  def partition(array: Array[Int], left: Int, right: Int, pivotIndex: Int): Int = {
    val pivotValue: Int = array(pivotIndex);
    var storeIndex: Int = left;
    switch(array, pivotIndex, right);
    for(i <- left to right) {
      if(array(i) < pivotValue) {
        switch(array, storeIndex, i);
        storeIndex += 1;
      }
    }
    switch(array, storeIndex, right);
    return storeIndex;
  }

  def select(array: Array[Int], left: Int, right: Int, n: Int): Int = {
    if(left == right) {
      return array(left);
    }
    var pivotIndex = left + scala.util.Random.nextInt(right-left+1);
    pivotIndex = partition(array, left, right, pivotIndex);
    if(n == pivotIndex) {
      return array(n);
    } else if(n < pivotIndex) {
      return select(array, left, pivotIndex-1, n);
    }else{
      return select(array, pivotIndex+1, right, n);
    }
  }

  def quickselect(array: Array[Int], k: Int): Int = {
    return select(array, 0, array.length-1, k-1);
  }
}
