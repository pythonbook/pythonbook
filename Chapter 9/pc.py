import math

def pc(x0,y0,xmax,dx,yp):

    nmax = math.ceil(xmax // dx)
    yn = y0
    xn = x0

    for i in range(nmax):
        #Prediction
        yn1 = dx * yp(xn,yn) + yn

        #Correction
        yn1 = yn + 0.5 * dx *
              (yp(xn,yn) + yp(xn+dx,yn1))

        yn = yn1
        xn += dx

    return yn
