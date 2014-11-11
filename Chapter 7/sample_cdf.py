import random
import math

class SampleCDF(object):
    
    def __init__(self,CDF,min,max,bins):
        self.min = min
        self.max = max
        self.bins = bins
        self.bin_size = (max - min) / self.bins

        # Discretize CDF
        self.disc_CDF = [0] * self.bins
        for i in range(self.bins):
            self.disc_CDF[i] = CDF(min+i*self.bin_size)

        random.seed()

 
    def random(self):
        # Find x for this probability
        target = random.random()

        # Binary search
        min_index = 0
        max_index = self.bins - 1
        pivot_index = (max_index - min_index) // 2

        while (pivot_index != min_index and
               pivot_index != max_index):

            # Adjust indices for next iteration
            if self.disc_CDF[pivot_index] <= target:
                min_index = pivot_index
            else:
                max_index = pivot_index

            pivot_index = (min_index +
                          (max_index - min_index) // 2)

        # Interpolate between the two closest x-values
        slope = (self.disc_CDF[max_index] -
                 self.disc_CDF[min_index])/self.bin_size;
                 
        dx = (target - self.disc_CDF[min_index]) / slope;

        return (dx + self.min +
                min_index * self.bin_size)