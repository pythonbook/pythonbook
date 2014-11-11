from euler2o import *
import math

def shooting(yp0,x0,y0,xf,yf,dx,accuracy,max_iter,ypp):
    # yp0 is the initial guess for y'(x)
    # x0 and y0 are initial values for x and y
    # we solve for y(x) up to xf and yf
    # dx is the step size
    # accuracy is the target accuracy
    # max_iter is the max iterations
    # ypp the function y'' = f(x,y) to solve

    f0 = euler2o(x0,y0,yp0,xf,dx,ypp) - yf
    yp1 = -f0 / yp0

    for i in range(max_iter):
        f1 = euler2o(x0,y0,yp1,xf,dx,ypp) - yf
        fp = (f1 - f0) / (yp1 - yp0)
        yp0 = yp1
        yp1 = yp0  - f1/fp

        if abs(f0 / yf) < accuracy:
            print("Iterated " + str(i) + " times")
            print("Achieved req. tolerance")
            break


        if i == max_iter - 1:
            print("Max. iterations reached.")
            break

        f0 = f1
    return yp1

    
