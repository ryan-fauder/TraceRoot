from sympy import diff, Poly, symbols, print_python
from sympy.polys.polytools import div
from utils import lambdify, input_expr
import numpy as np

class Expression:
    expr = None

    def __init__(self, f):
        self.expr = f
        
    @classmethod
    def input(cls, q):
        return cls(input_expr(q))
    

    def output(self):
        print_python(self.expr)
        

    def when(self, x):
        return lambdify(self.expr)(x)
    

    def derivative_when(self, x):
        return lambdify(diff(self.expr))(x)


    def second_derivative_when(self, x):
        return lambdify(diff(diff(self.expr)))(x)


    def get_coeffs(self, n = 0):
        if (not self.expr.is_polynomial()): raise Exception('Expressão deve ser um polinômio')
        if (n < 0 or n > 3): raise Exception('n deve ser estar no intervalo [0, 3]')
        # Função para inverter coeficientes de grau ímpar
        invert_odd_degree_coeffs = lambda l: list(map(lambda x: x[1] if x[0] % 2 == 0 else -x[1], enumerate(l)))
        
        # Coeficientes do polinômio
        coeffs_list = list(Poly(self.expr).all_coeffs())

        if n == 1:
          coeffs_list = coeffs_list[::-1]
        elif n == 2:
          coeffs_list = invert_odd_degree_coeffs(coeffs_list)
        elif n == 3:
          coeffs_list = invert_odd_degree_coeffs(coeffs_list[::-1])

        return coeffs_list if coeffs_list[0] > 0 else list(map(lambda x: -x, coeffs_list))
    

    def get_lowest_degree(self):
        if (not self.expr.is_polynomial()): raise Exception('Expressão deve ser um polinômio')

        coeffs_list = self.get_coeffs()
        return len(coeffs_list) - len(np.trim_zeros(coeffs_list))


    def get_highest_degree(self):
        if (not self.expr.is_polynomial()): raise Exception('Expressão deve ser um polinômio')

        return len(self.get_coeffs())


    def has_x(self):
        return symbols('x') in self.expr.free_symbols
    

    def deflate_root_zero(self):
        return Expression(div(self.expr, symbols('x') ** self.get_lowest_degree())[0].as_expr())
    

    def get_descartes(self):
        sign_list_p = [x/abs(x) for x in self.get_coeffs() if x != 0]
        transitions_list_p = [[x, sign_list_p[i + 1]] for (i, x) in enumerate(sign_list_p[:-1])]
        np = len([x for x in transitions_list_p if x[0] * x[1] < 0])

        sign_list_n = [x/abs(x) for x in self.get_coeffs(n = 2) if x != 0]
        transitions_list_n = [[x, sign_list_n[i + 1]] for (i, x) in enumerate(sign_list_n[:-1])]
        nn = len([x for x in transitions_list_n if x[0] * x[1] < 0])
        
        # print([i for i in range(np, -1, -2)])
        return [i for i in range(np, -1, -2)], [i for i in range(nn, -1, -2)]


    def has_real_roots(self):
        np, nn = self.get_descartes()
        return (np != [0] or nn != [0])
