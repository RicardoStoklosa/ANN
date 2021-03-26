from .lagrange import lagrange_func
from matplotlib import pyplot as plt
import numpy as np


def f(x):
    return 1 / (1 + 25 * x ** 2)


def runge(f: callable, x, plot: bool):
    num = 5
    y = [f(i) for i in x]
    eq = lagrange_func(x, y)

    if plot:
        def subs(x: int):
            return eval(eq)

        t = np.linspace(min(x), max(x), 100)

        plt.plot(t, subs(t))
        plt.scatter(x, y)

        plt.show()

    return eq


# def subs(x):
