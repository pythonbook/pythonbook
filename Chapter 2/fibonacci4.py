fibonacci_list = [0, 1]

def fibonacci(n):
    Fn = 0  # F(n)

    start = len(fibonacci_list)

    for i in range(start,n+1):
        Fn = fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(Fn)

    return fibonacci_list[n]
