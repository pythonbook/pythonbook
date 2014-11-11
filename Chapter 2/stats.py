def average(start, stop):
    sum = 0
    for i in range(start,stop):
        sum += i
    count = len(range(start,stop))
    return sum/count