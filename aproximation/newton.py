from sympy import Lambda, diff, lambdify, Symbol
from sympy.abc import x


def newton(f: Lambda, p: float, n: int = 10, precision=14) -> None:
    f_ = Lambda(x, diff(f(x), x))
    for _ in range(n):
        p = p - (f(p) / f_(p))
        print("%.*f" % (precision, p))
