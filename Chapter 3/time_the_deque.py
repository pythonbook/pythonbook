import time
from collections import deque

L1 = deque(1000*[0])
L2 = deque(5000*[0])
L3 = deque(10000*[0])
L4 = deque(50000*[0])
L5 = deque(100000*[0])
L6 = deque(500000*[])

def time_the_list(L,n):
    for i in range(5):
        start_time = time.clock()
        l = L.pop(n)
        stop_time = time.clock()
        elapsed = stop_time - start_time
        print(str(l) + ' : ' + str(round(elapsed,7)))

time_the_list(L1,500)
time_the_list(L2,2500)
time_the_list(L3,5000)
time_the_list(L4,25000)
time_the_list(L5,50000)
time_the_list(L6,250000)

