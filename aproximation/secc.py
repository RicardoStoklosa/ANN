from sympy import Lambda, diff, lambdify, Symbol
from sympy.abc import x


def secc(f: Lambda, p: [float], n: int = 10, precision=14) -> None:
    for i in range(1, n + 1):
        p.append((p[i - 1] * f(p[i]) - p[i] * f(p[i - 1])) / (f(p[i]) - f(p[i - 1])))
        print("%.*f" % (precision, p[-1]))