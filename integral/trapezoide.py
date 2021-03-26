def func(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1,n):
        soma += f(a+k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2)*soma

def trapezoide(f, interval, subinterval):
    for i in subinterval:
        print(func(f, interval[0], interval[1], i))