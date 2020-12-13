from sympy import Lambda


def bissecao(f: Lambda, a: float, b: float, n: int = 10, precision=14) -> None:
    fa = f(a)
    for _ in range(n):
        p = a + (b - a) / 2
        print("%.*f" % (precision, f(p)))
        fp = f(p)
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p