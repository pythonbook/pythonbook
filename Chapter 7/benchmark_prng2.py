import matplotlib.pyplot as pyplot

def benchmark_prng(prng_obj):
    # Num bins in histogram
    bins = 50
    
    # Avg num points per bin
    points_per_bin = 1000
    
    # Num calls to rand()
    iterations = points_per_bin * bins
    
    data = [0]*iterations
    
    for i in range(iterations):
        data[i] = prng_obj.random()
    
    # Generate histogram
    pyplot.hist(data,bins)
    pyplot.xlabel("Value")
    pyplot.ylabel("Frequency")
    pyplot.show()