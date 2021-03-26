from sympy import Lambda
from . import bolzano


def false_position(f: Lambda, p0: float, p1: float, n: int = 10, precision=14) -> None:
    if bolzano(f, p0, p1):
        p3 = p0 - f(p0) * (p1 - p0) / (f(p1) - f(p0))
        for _ in range(n):
            if bolzano(f, p0, p3):
                p0 = p3
            else:
                p1 = p3
            p3 = p0 - f(p0) * (p1 - p0) / (f(p1) - f(p0))
            print("%.*f" % (precision, p3))
    else:
        print("Reprovado no teorema de Bolzano")