from expression import Expression

# Newton-Raphson Method

def choose_x0(f: Expression, interval: list, tolerance: float):
    a, b = interval
    mean = (a + b) / 2
    f_m = f.when(mean)
    if f_m * f.second_derivative_when(mean) > 0:
        return mean
    if abs(a - b) < tolerance:
        raise ValueError()
    if f_m > 0:
        a = mean
    else:
        b = mean
    return choose_x0(f, [a, b], tolerance)


def newton_naive(f: Expression, x_0: float, tolerance: float, loop: float = 0):
    if loop >= 100:
        raise Exception("Nao foi encontrada uma raiz na tolerancia informada")
    x_n = x_0 - (f.when(x_0) / f.derivative_when(x_0))
    error = abs(x_n - x_0)
    print(x_0, " ", x_n, " ", f.when(x_0), " ", f.when(x_n), " ", error)
    if error > tolerance:
        return newton_naive(f, x_n, tolerance, loop + 1)
    else:
        return x_n


def newton(f: Expression, x_n: float, tolerance: float, loop: float = 0):
    if loop >= 1000:
        raise Exception("Nao foi encontrada uma raiz na tolerancia informada")
    if loop == 0:
        newton.table = []
    if loop > 0:
        f_n = newton.table[-1][3]
    else:
        f_n = f.when(x_n)

    df_n = f.derivative_when(x_n)
    if df_n == 0:
        raise Exception("f'(x) nao pode ser nula")

    x_n1 = x_n - (f_n / df_n)
    f_n1 = f.when(x_n1)
    error = abs(x_n1 - x_n)

    newton.table += [[x_n, x_n1, f_n, f_n1, error]]

    if error > tolerance:
        return newton(f, x_n1, tolerance, loop + 1)
    else:
        return newton.table


def newton_print(table: list):
    print(" " + "-" * 59)
    print(f'|{"x_n":^11}|{"x_n1":^11}|{"f_n":^11}|{"f_n1":^11}|{"x_n1 - x_n":^11}|')
    print("|-----------|-----------|-----------|-----------|-----------|")
    for i in range(0, len(table)):
        x_n, x_n1, f_n, f_n1, error = [float(i) for i in table[i]]
        print(
            f"|{x_n:^11.5f}|{x_n1:^11.5f}|"
            + f"{f_n:^11.5f}|{f_n1:^11.5f}|{error:^11.5f}|"
        )

    print(" " + "-" * 59)


newton.table = [
    # x_n, x_n1, f_n, f_n1, error
]


if __name__ == "__main__":
    f = Expression.input("Escreva a função: ")
    x_0 = 2.3
    table = newton(f, x_0, 1e-6)
    newton_print(table)
