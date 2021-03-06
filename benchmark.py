import matplotlib.pyplot as plt


def retreiving_benchmarks(file_name):
    benchmarks_file = open(file_name, "r")
    example_sizes, mean_durations = [], []
    for line in benchmarks_file:
        example_size, mean_duration = line.split(" ")
        example_sizes.append(int(example_size))
        mean_durations.append(float(mean_duration))
    benchmarks_file.close()
    return example_sizes, mean_durations


python_benchmarks = retreiving_benchmarks("python/benchmark_results.txt")
cython_benchmarks = retreiving_benchmarks("cython/benchmark_results.txt")
scala_benchmarks = retreiving_benchmarks("scala/benchmark_results.txt")
java_benchmarks = retreiving_benchmarks("java/benchmark_results.txt")
c_benchmarks = retreiving_benchmarks("C/benchmark_results.txt")
r_benchmarks = retreiving_benchmarks("R/benchmark_results.txt")

plt.figure(figsize=(10,8))
plt.plot(python_benchmarks[0], python_benchmarks[1], label="Python")
plt.plot(cython_benchmarks[0], cython_benchmarks[1], label="Cython")
plt.plot(scala_benchmarks[0], scala_benchmarks[1], label="Scala")
plt.plot(java_benchmarks[0], java_benchmarks[1], label="Java")
plt.plot(c_benchmarks[0], c_benchmarks[1], label="C")
plt.plot(r_benchmarks[0][:14], r_benchmarks[1][:14], label="R")

plt.legend(loc=0)
plt.title("Time of execution of QuickSelect")
plt.xlabel("Size of the array")
plt.ylabel("Mean time of execution (seconds)")
plt.yscale('log')
plt.savefig("quickselect_benchmark.png")
