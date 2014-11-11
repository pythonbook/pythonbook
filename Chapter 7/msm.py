import math
import datetime

class MSM(object):
    def __init__(self,seed=0):

        if seed == 0:
            seed = datetime.datetime.now()
            self.seed = seed.second*(1e6)+seed.microsecond
            self.seed = math.floor(self.seed/100)%10000
        else:
            self.seed = seed

    def random(self):
        self.seed**=2
        self.seed = math.floor(self.seed/100)%10000
        return self.seed
        
