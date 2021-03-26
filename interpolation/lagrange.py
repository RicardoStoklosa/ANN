from matplotlib import pyplot as plt
import numpy as np

def lagrange_func(x: [int], y: [int]):
    n = len(x)

    if n == len(y):
        eq = ''
        for k in range(n):
            numer = '*'.join([f'(x{-xi:+})' for i, xi in enumerate(x) if i != k])
            denon = '*'.join([f'({x[k]}{-xi:+})' for i, xi in enumerate(x) if i != k])
            eq += f'{y[k]:+}*({numer})/({denon})'
        return eq
    else:
        raise TypeError("O tamanho de x é diferente de y")


def lagrange(x: [int, int, int], y: [int, int, int]):
    eq = lagrange_func(x,y)

    def subs(x: int):
        return eval(eq)

    print(eq)
    
    t = np.linspace(min(x), max(x), 100)
    
    plt.plot(t, subs(t))
    plt.scatter(x, y)

    plt.show()

    