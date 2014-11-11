class Polygon(object):
    
    def __init__(self,points):
        self.points=points
    
    def point_in_p(self,a):
        x = a[0]
        y = a[1]

        nedges = 0
        for i in range(len(self.points)):
            p = self.points[i]
            lp = self.points[(i-1) % len(self.points)]
            rp = self.points[(i+1) % len(self.points)]

            #current edge = p -> rp
            print('***considering current edge: ['+
                  str(p)+'->'+str(rp)+']')

            if p[0] < x and rp[0] < x:
                #ignore the edge
                print('Ignoring. edge ['+
                      str(p)+'->'+str(rp)+
                      '] is to the left of '+
                      str(a))
                continue
            if (p[1] < y and rp[1] < y) or (p[1] > y and rp[1] > y):
                print('Ignoring. edge [' +
                      str(p) +
                      '->' +
                      str(rp) +
                      '] y-range out of range of ' +
                      str(a))
                continue
            if p[1] == y:
                if p[0] < x:
                    #ignore, vertex is to the left
                    continue
                if (lp[1] > p[1] and rp[1] > p[1]) or (lp[1] < p[1] and rp[1] < p[1]):
                    print('Ignoring. vertex '+
                          str(p) +
                          ' neighbors are on same side ')
                    nedges += 2
                else:
                    print('Cannot ignore. vertex '+
                          str(p) +
                          ' neighbors are on different '
                          'sides')
                    nedges += 1
                continue
            print('Edge crossing at edge: edge ['+
                  str(p)+'->'+str(rp)+']')
            nedges += 1

        return nedges % 2 == 1
