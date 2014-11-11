import math
    
def euler(x0,y0,xmax,dx,yp):
    # x0 and y0 are initial values
    # we solve for y(x) up to xmax
    # dx is the step size
    # yp is the function y'(x,y)
    
    # max number of steps
    nmax = math.ceil(xmax // dx)
    yn = y0
    xn = x0

    # step through and compute
    # yn for each step
    for i in range(nmax):
        yn = dx * yp(xn,yn) + yn
        xn += dx

    return yn
