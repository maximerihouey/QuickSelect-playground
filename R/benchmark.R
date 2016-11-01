source("quickselect.R")


shuffle = function(tableau){
  tableau$value = sample(tableau$value, length(tableau$value))
}

time_execution = function(tableau, k, nbExampleBySize){
  times = rep(0, nbExampleBySize)
  for(i in 1:nbExampleBySize){
    shuffle(tableau)
    start = Sys.time()
    quickselect(tableau, k)
    times[i] = Sys.time() - start
  }
  return(times)
}

f <- file("benchmark_results.txt", open="w")
truncate(f)
close(f)

example_sizes = c(50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 9000, 10000, 15000, 17500, 20000, 25000)
for(example_size in example_sizes){
  example = newPointer(array(c(1:example_size)))
  mean_duration = mean(time_execution(example, ceiling(example_size/2), 100))
  
  print(sprintf("%i %f", example_size, mean_duration))
  cat(sprintf("%i %f", example_size, mean_duration),file="benchmark_results.txt",sep="\n",append=TRUE)
}