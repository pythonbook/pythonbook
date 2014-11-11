def fibonacci(n):
    Fn = 0  # F(n)
    F1 = 0  # F(n-1)
    F2 = 1  # F(n-2)

    for i in range(n):
        Fn = F2 + F1
        F2 = F1
        F1 = Fn

    return Fn

        
