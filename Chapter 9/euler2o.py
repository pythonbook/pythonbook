import math

def euler2o(x0,y0,yp0,xmax,dx,ypp):
    # x0 and y0 are initial values
    # yp0 is the initial derivative value
    # we solve for y(x) up to xmax
    # dx is the step size
    # ypp the function y'' = f(x,y) to solve

    # Number of steps
    nmax = math.ceil((xmax - x0 - dx) // dx)

    # Start x at 3rd step since
    # we have y0, and compute y1
    xn = x0 + 2 * dx

    # y(x-dx) for first iteration
    yn0 = y0

    # Use Euler to compute
    # y(x) for 1st iteration
    yn = dx * yp0 + yn0
    
    #Precompute dx^2
    dx2 = dx ** 2

    for i in range(nmax):
        yn1 = dx2*ypp(xn,yn0,yn,dx)+2*yn-yn0
        xn += dx

        yn0 = yn
        yn  = yn1

    return yn1
