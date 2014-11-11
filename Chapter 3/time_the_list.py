import time

L1 = 1000*[0]
L2 = 5000*[0]
L3 = 10000*[0]
L4 = 50000*[0]
L5 = 100000*[0]
L6 = 500000*[]

def time_the_list(L):
    for i in range(5):
        start_time = time.clock()
        l = len(L)
        stop_time = time.clock()
        elapsed = stop_time - start_time
        print(str(l) + ' : ' + str(round(elapsed,7)))

time_the_list(L1)
time_the_list(L2)
time_the_list(L3)
time_the_list(L4)
time_the_list(L5)
time_the_list(L6)

