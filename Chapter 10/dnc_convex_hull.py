def dnc_convex_hull(points, srted=False):
    if not srted:
        points.sort()

    print('dnc_convex_hull: got points ' +
          str(points))
    
    if len(points) <= 3 and len(points) > 0:
        return clockwise(points)
    elif (len(points) == 0):
        input('Error: empty points')
        return []
    
    left = len(points) // 2

    print('about to recurse on left side' +
          str(points[0:left]))
    left_hull = dnc_convex_hull(points[0:left],True)
    print('got left_hull: ' + str(left_hull))

    print('about to recurse on right side' +
          str(points[left:]))
    right_hull = dnc_convex_hull(points[left:],True)
    print('got right_hull: ' + str(right_hull))

    print('going to merge')
    return merge(left_hull,right_hull)

def clockwise(points):
    if len(points) == 1:
        return points
    i = 0
    minx = 0
    for i in range(len(points)):
        if points[i][0] < points[minx][0]:
            minx = i

    if len(points) == 2:
        return [points[minx],points[(minx+1) % 2]]

    # points = 3
    islft = is_left(points[minx],
                    points[(minx+1) % 3],
                    points[(minx + 2) % 3])
    if  islft > 0:
        pts = [points[minx],points[(minx+2) % 3],
               points[(minx+1) % 3]]
    elif islft < 0:
        pts = [points[minx],points[(minx+1) % 3],
               points[(minx+2) % 3]]
    else:
        # points are collinear so only
        # keep first and last
        pts = sorted(points)
        pts = [pts[0],pts[-1]]
    return pts


def is_left(a,b,c):
    return ((c[1]-a[1])*(b[0]-a[0]) -
            (b[1]-a[1])*(c[0]-a[0]))

def get_dir_lara(a,b,la,ra):
    dirla = is_left(a,b,la)
    dirra = is_left(a,b,ra)
    return (dirla, dirra)

def check_left_tangent(a,b, la, ra):
    dirla, dirra = get_dir_lara(a,b,la,ra)
    if dirra == 0 and dirla == 0:
        input('degenerate left tangent: a: ' +
              str(a) + ' b: ' +
              str(b) + ' la: ' +
              str(la)+ ' ra: ' +
              str(ra))
        
    if dirra >= 0 and dirla >= 0:
        return True
    else:
        return False


def check_right_tangent(a,b,la,ra):
    dirla, dirra = get_dir_lara(a,b,la,ra)
    if dirra == 0 and dirla == 0:
        input('degenerate rightangent: a: ' +
              str(a) + ' b: ' +
              str(b) + ' la: ' +
              str(la)+ ' ra: ' +
              str(ra))
        
    return dirla <= 0 and dirra <= 0

def get_lower_tangent(left_hull,
                      right_hull,a,b):
    #lower tangent
    la = (a-1)%len(left_hull)
    ra = (a+1)%len(left_hull)
    lb = (b-1)%len(right_hull)
    rb = (b+1)%len(right_hull)

    is_tangent=False
    while is_tangent==False:
        count=0
        while check_left_tangent(left_hull[a],
                                 right_hull[b],
                                 left_hull[la],
                                 left_hull[ra])==False:
            a =  (a+1) % len(left_hull)
            la = (a-1) % len(left_hull)
            ra = (a+1) % len(left_hull)
            
            count = count + 1
            if count == len(left_hull):
                print('get_lower_tangent: '
                      'Infinite loop in left hull')
    
        count=0
        while check_left_tangent(left_hull[a],
                                 right_hull[b],
                                 right_hull[lb],
                                 right_hull[rb])==False:
            b  = (b-1) % len(right_hull)
            lb = (b-1) % len(right_hull)
            rb = (b+1) % len(right_hull)
            count=count+1
            if count==len(right_hull):
                print('get_lower_tangent: '
                      'Infinite loop in right hull')
        
        if check_left_tangent(left_hull[a],
                              right_hull[b],
                              left_hull[la],
                              left_hull[ra]):
            return [a,b]

def get_upper_tangent(left_hull, right_hull,a,b):
    #lower tangent
    la = (a - 1) % len(left_hull)
    ra = (a + 1) % len(left_hull)
    lb = (b - 1) % len(right_hull)
    rb = (b + 1) % len(right_hull)

    is_tangent=False
    while not is_tangent:
        count = 0
        while check_right_tangent(left_hull[a],
                                  right_hull[b],
                                  left_hull[la],
                                  left_hull[ra])== False:
            
            a  = (a-1) % len(left_hull)
            la = (a-1) % len(left_hull)
            ra = (a+1) % len(left_hull)
            count = count + 1
            if count == len(left_hull):
                print('get_upper_tangent: '
                      'Infinite loop in left hull')

        count = 0
        while check_right_tangent(left_hull[a],
                                  right_hull[b],
                                  right_hull[lb],
                                  right_hull[rb])== False:
            
            b  = (b+1) % len(right_hull)
            lb = (b-1) % len(right_hull)
            rb = (b+1) % len(right_hull)
            count = count + 1
            if count == len(right_hull):
                print('get uppertangent: '
                      'Infinite loop in right hull')
        
        if check_right_tangent(left_hull[a],
                               right_hull[b],
                               left_hull[la],
                               left_hull[ra]):
            return [a,b]

           
def merge(left_hull,right_hull):
    print('merge: got left_hull: ' + str(left_hull))
    print('merge: got right_hull: ' + str(right_hull))

    if len(left_hull) == 2 and len(right_hull) == 2:
        left_hull.sort(key = lambda x: (x[1],x[0]))
        right_hull.sort(key = lambda x: (x[1],x[0]))

        print('merge: before getting '
              'lower tangent of two lines')
        la, lb = get_lower_tangent(left_hull,
                                   right_hull,0,0)
        
        print('merge: after lower tangent. la: ' +
              str(left_hull[la]) + ' lb: ' +
              str(right_hull[lb]))
              
        ua, ub = get_upper_tangent(left_hull,
                                   right_hull,1,1)
        print('merge: after upper tangent. ua: ' +
              str(left_hull[ua]) +' ub: ' +
              str(right_hull[ub]))
    else:
        #assume left_hull and right_hull
        #are in clockwise order
        left_min = 0
        left_max = 0
        for i in range(len(left_hull)):
            if left_hull[i][0] < left_hull[left_min][0]:
                left_min = i
            if left_hull[i][0] > left_hull[left_max][0]:
                left_max = i

        right_min = 0
        right_max = 0
        for i in range(len(right_hull)):
            if right_hull[i][0] < right_hull[right_min][0]:
                right_min = i
            if right_hull[i][0] > right_hull[right_max][0]:
                right_max = i

        a = left_max
        b = right_min

        print('left_min: ' + str(left_hull[left_min]) +
              ' left_max: ' + str(left_hull[left_max]) +
              ' right_min: ' + str(right_hull[right_min]) +
              ' right_max: ' + str(right_hull[right_max]))
              
        print('merge: before getting lower tangent')
        
        la, lb =get_lower_tangent(left_hull,right_hull,a,b)
        
        print('merge: after lower tangent. la: ' +
              str(left_hull[la]) + ' lb: ' +
              str(right_hull[lb]))
              
        ua, ub = get_upper_tangent(left_hull,right_hull,a,b)
        
        print('merge: after upper tangent. ua: '+
              str(left_hull[ua]) + ' ub: ' +
              str(right_hull[ub]))

    max_points = len(left_hull) + len(right_hull)
    convex_hull = []
    
    i = la
    while i != ua:
        if len(convex_hull) > 2:
            if is_left(convex_hull[-2],
                       convex_hull[-1],
                       left_hull[i]) == 0:
                convex_hull[-1] = left_hull[i]
            else:    
                convex_hull.append(left_hull[i])
        else:
            convex_hull.append(left_hull[i])
        i = (i + 1) % len(left_hull)

    if len(convex_hull) > 2:
            if is_left(convex_hull[-2],
                       convex_hull[-1],
                       left_hull[ua]) == 0:
                convex_hull[-1] = left_hull[ua]
            else:    
                convex_hull.append(left_hull[ua])
    else:
        convex_hull.append(left_hull[ua])

    i = ub
    while i != lb:
        if len(convex_hull) > 2:
            if is_left(convex_hull[-2],
                       convex_hull[-1],
                       right_hull[i]) == 0:
                convex_hull[-1] = right_hull[i]
            else:    
                convex_hull.append(right_hull[i])
        else:
            convex_hull.append(right_hull[i])
        i = (i + 1) % len(right_hull)

    if len(convex_hull) > 2:
            if is_left(convex_hull[-2],
                       convex_hull[-1],
                       right_hull[lb]) == 0:
                convex_hull[i]=right_hull[lb]
            else:    
                convex_hull.append(right_hull[lb])
    else:
        convex_hull.append(right_hull[lb])
    
    print('merge.  constructed convex hull.  '+
          str(convex_hull))
    return convex_hull