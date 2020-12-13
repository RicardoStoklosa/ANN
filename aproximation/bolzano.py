from sympy import Lambda


def bolzano(f: Lambda, a: float, b: float) -> bool:
    if (f(a) * f(b)) < 0:
        return True
    return False