from numpy import array, diag, diagflat, dot, linalg, set_printoptions


def jacobi(a: [[float]], b: [float], guess: [float], n: int = 7, precision=14) -> None:
    set_printoptions(16)
    dg = diagflat(diag(a))
    l = a - dg
    dg = linalg.inv(dg)

    for _ in range(n):
        guess = dot(dot(-dg, l), guess) + dot(dg, b)
        print(guess)
