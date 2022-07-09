from sympy import lambdify as lmb, symbols
from sympy.parsing.sympy_parser import parse_expr

def input_expr(q):
    return parse_expr(input(q).replace('^', '**'))

def lambdify(expr):
    return lmb(symbols("x"), expr, "numpy")

def getValidInterval(f, interval: list):
    a = interval[0]
    b = interval[1]
    f_a = f.when(a)
    f_b = f.when(b)
    if f_a >= 0 and f_b <= 0:
        return [a, b]
    elif f_a <= 0 and f_b >= 0:
        return [b, a]
    else:
        return []