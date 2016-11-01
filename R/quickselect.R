library(compiler)

newPointer=function(inputValue){  
  object=new.env(parent=globalenv())  
  object$value=inputValue  
  class(object)='pointer'
  
  return(object)  
}

switcharoo_u = function(tableau, index1, index2){
  temp = tableau$value[index1]
  tableau$value[index1] = tableau$value[index2]
  tableau$value[index2] = temp
}
switcharoo = cmpfun(switcharoo_u)

partition_u = function(tableau, left, right, pivotIndex){
  pivotValue = tableau$value[pivotIndex]
  storeIndex = left
  switcharoo(tableau, pivotIndex, right)
  for(i in left:right){
    if(tableau$value[i] < pivotValue){
      switcharoo(tableau, storeIndex, i)
      storeIndex = storeIndex + 1
    }
  }
  switcharoo(tableau, storeIndex, right)
  return(storeIndex)
}
partition = cmpfun(partition_u)

qselect_u = function(tableau, left, right, n){
  if(left == right){
    return(tableau$value[left])
  }
  pivotIndex = round(runif(1, left, right))
  pivotIndex = partition(tableau, left, right, pivotIndex)
  if(n == pivotIndex){
    return(tableau$value[n])
  }else if(n < pivotIndex){
    return(qselect(tableau, left, pivotIndex-1, n))
  }else{
    return(qselect(tableau, pivotIndex+1, right, n))
  }
}
qselect = cmpfun(qselect_u)

quickselect_u = function(tableau, k){
  return(return(qselect(tableau, 1, length(tableau$value), k)))
}
quickselect = cmpfun(quickselect_u)
