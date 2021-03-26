import math

NMAX = 15
TOL = 0.000000000000001

# funcao inicial
def Q1F1(x):
    return x * x * x - 5


# derivada da fucao
def dQ1F1(x):
    return 3 * x * x


def posicao_falsa(f, p0, p1, TOL, MAXIT):
    q0, q1 = f(p0), f(p1)
    for i in range(1, MAXIT):
        p = p1 - (q1 * (p1 - p0) / (q1 - q0))
        if abs(p - p1) < TOL:
            print("     ", i, p)
            return p
        q = f(p)
        if q * q1 < 0:
            p0, q0 = p1, q1
        p1, q1 = p, q
        print("     ", i, p)
    return p


posicao_falsa(Q1F1, 0.13828, 2.09264, TOL, NMAX)
