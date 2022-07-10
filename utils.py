from sympy import lambdify as lmb, symbols
from sympy.parsing.sympy_parser import parse_expr

def input_expr(q):
    return parse_expr(input(q).replace('^', '**'))

def lambdify(expr):
    return lmb(symbols("x"), expr, "numpy")