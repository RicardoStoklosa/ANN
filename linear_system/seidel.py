from numpy import array, diag, diagflat, dot, linalg, set_printoptions, tril, triu


def seidel(a: [[float]], b: [float], guess: [float], n: int = 7):
    a = array(a)
    b = array(b)
    guess = array(guess)

    D = diagflat(diag(a))
    L = tril(a, -1)
    U = triu(-a, 1)
    D_L = D + L
    D_L_ = linalg.inv(D_L)

    for _ in range(n):
        guess = dot(D_L_, (dot(U, guess) + b))
    print(guess)