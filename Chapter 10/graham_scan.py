import math

def graham_scan(points):
    if len(points) < 3:
        return points
    #first find lowermost and leftmost point
    print('Got points: '+ str(points))
    minpt = 0
    for i in range(len(points)):
        if points[i][1] < points[minpt][1]:
            minpt = i
        elif points[i][1] == points[minpt][1]:
            if points[i][0] < points[minpt][0]:
                minpt = i

    refpt = points[minpt]
    print('minpt: ' + str(refpt))
    points.sort(key=lambda x: \
                math.atan2(x[1]-refpt[1],
                           x[0]-refpt[0]))

    print('SORTED points: ' + str(points))
    convex_hull = [refpt]

    for i in range(len(points)):
        if points[i] == refpt:
            continue
        if len(convex_hull) >=2:
            if is_left(convex_hull[-2],
                       convex_hull[-1],
                       points[i]) > 0:
                convex_hull.append(points[i])
            else:
                while (len(convex_hull) > 1 and
                       is_left(convex_hull[-2],
                              convex_hull[-1],
                              points[i]) <= 0):
                    convex_hull.pop()
                convex_hull.append(points[i])
        else:
            convex_hull.append(points[i])

    return convex_hull
        
def is_left(a,b,c):
    return ((c[1]-a[1])*(b[0]-a[0]) -
            (b[1]-a[1])*(c[0]-a[0]))

    
