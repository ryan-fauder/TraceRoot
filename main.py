from bissection import *
from lagrange import *
from newton import *
from sympy import solve, simplify
from sympy.abc import x
from controller import *
from expression import Expression

if __name__ == "__main__":
    # Variables
    roots = []
    root = 0
    bissection_table = []
    newton_table = []

    f: Expression = Expression.input("Escreva a função: ")

    if not f.expr.is_polynomial():
        print(solve(f.expr, x))
        exit(0)

    while f.when(0) == 0:
        roots += [0]
        f = Expression(simplify(f.expr / x))
    
    while True:
        intervals_list = []
        new_roots = []
        root: float = 0.0

        if not f.expr.is_polynomial():
            break
        if not f.has_x():
            break
        if f.has_degree(1):       
            c0 = f.get_coeff(0)
            c1 = f.get_coeff(1)
            root = (-1) * c0 / c1
            roots += [root]
            break
        
        intervals_list = get_intervals(f)
        
        if intervals_list == None or intervals_list == []:
            break

        intervals_list = filter_intervals(f, intervals_list)

        if intervals_list == None or intervals_list == []:
            break

        for i in intervals_list:
            interval_refined = []
            bissection_table = []
            newton_table = []
            interval_refined = prerefinement(f, i, bissection_table, 10**-3)
            print("O pré-refinamento com método da Bisseção foi realizado com sucesso.")

            root = refinement_newton(f, interval_refined, newton_table)
            if root != None:
                print("O refinamento com método de Newton foi realizado com sucesso.")
            
            else:
                print("Os requisitos para o refinamento com o método Newton não foram atendidos.")
                
                root = refinement_bissection(f, interval_refined, bissection_table, 10**-7)
                print("O refinamento com método da Bisseção foi realizado com sucesso.")                
            print_table_roots(bissection_table, newton_table)
            new_roots += [root]
        
        f = deflate_equation(f, new_roots)
        roots += new_roots

    print("\nRaízes: ", roots)
