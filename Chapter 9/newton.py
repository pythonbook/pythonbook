
def newton(x0,accuracy,max_iter,f,fp=0):
    # x0 is initial value
    # accuracy is target accuracy
    # max_iter is max iterations
    # f is the function f(x) = 0 to solve
    # fp is just f'(x)
    
    x1 = 0.0
    
    for i in range(max_iter):
        # try-except used to handle fp=0
        try:
            x1 = x0 - f(x0)/fp(x0)
        except:
            dx = accuracy*x0
            x1 = x0 - f(x0) / ((f(x0) - f(x0-dx))/dx)

        # quit if we met target accuracy
        if abs(x1-x0)/x0 < accuracy:
            print("Iterated " + str(i) + " times")
            print("Achieved req. tolerance")
            break

        x0 = x1
        
        # quit if we exceed max iterations
        if i == max_iter - 1:
            print("Max. iterations reached.")
            break

    return x1
