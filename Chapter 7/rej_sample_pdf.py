import random
import math

class RejSamplePDF(object):
    
    def __init__(self,PDF,min,max):
        self.min = min
        self.max = max
        self.range = max-min
        self.PDF = PDF

        random.seed()

    def random(self):
        # Set y to be larger than 1
        y = float('inf')
        x = 0
        
        # Evaluate PDF
        while y > self.PDF(x):
            # Generate random sample
            x = random.random() * self.range + self.min

            # Generate random probability
            y = random.random()

        # Random sample within PDF           
        return x
            
