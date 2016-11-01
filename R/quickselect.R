newPointer=function(inputValue){  
  object=new.env(parent=globalenv())  
  object$value=inputValue  
  class(object)='pointer'
  
  return(object)  
}

switcharoo = function(tableau, index1, index2){
  temp = tableau$value[index1]
  tableau$value[index1] = tableau$value[index2]
  tableau$value[index2] = temp
}

partition = function(tableau, left, right, pivotIndex){
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

qselect = function(tableau, left, right, n){
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

quickselect = function(tableau, k){
  return(return(qselect(tableau, 1, length(tableau$value), k)))
}

example_size = 11
example = newPointer(array(c(1:example_size)))
print(quickselect(example, 6))
