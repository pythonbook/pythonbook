fibonacci_list = [0,1]

def fibonacci(n):

    if n <= 1:
        return n
    else:
        try:
            a = fibonacci_list[n-2]
        except:
            a = fibonacci(n-2)
            fibonacci_list.append(a)

        try:
            b = fibonacci_list[n-1]
        except:
            b = fibonacci(n-1)
            fibonacci_list.append(b)

        return a + b

