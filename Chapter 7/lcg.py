import math
import datetime

class LCG(object):
    def __init__(self,a,c,m,seed=0):

        if seed == 0:
            seed = datetime.datetime.now()
            self.seed = seed.second*(1e6)+seed.microsecond
        else:
            self.seed = seed

        self.a = a
        self.c = c
        self.m = m

    def random(self):
        self.seed = (self.seed*self.a+self.c)%self.m
        return self.seed