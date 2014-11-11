import graham_scan
import random
import sys

def random_points(numpoints,length):
    points = []
    for i in range(numpoints):
        randx = random.random()*length
        randy = random.random()*length
        if (randx,randy) not in points:
            points.append((randx,randy))
    return points

points = random_points(int(sys.argv[1]),100)
hull = graham_scan.graham_scan(points)

fp = open(sys.argv[2],'w')
for i in range(len(hull)):
    fp.write(str(hull[i][0])+','+str(hull[i][1])+'\n')
fp.write('\n')
for i in range(len(points)):
    fp.write(str(points[i][0])+','+str(points[i][1])+'\n')
