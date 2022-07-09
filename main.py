from Expression import *
from bissection import *
from lagrange import *
from newton import *
from sympy import solve, simplify
from sympy.abc import x

# a)
# 2*x**3 - 5*x**2 - x + 3

# b)
# 5*x**3 - 2*x**2 - 8*x + 10

def print_table_roots(bissection_list, newton_list):
    if(bissection_list != []):
        print("\nBisseção: ")
        print_bissection_table(bissection_list)
    if(newton_list != []):
        print("Newton: ")
        nr_method_print(newton_list)
        
if (__name__ == "__main__"):
    roots = []
    bissection_list = []
    newton_list = []
    f: Expression = Expression.input('Escreva a função: ')

    if (not f.expr.is_polynomial()):
        print(solve(f.expr, x))
        exit(0)
 
    while (f.when(0) == 0):
        roots += [0]
        f = Expression(simplify(f.expr / x))    
    
    while True:
        intervals_list = []
        if (not f.expr.is_polynomial()):
            break
        if (not f.is_rho()):
            break
        try:
            descartes_intervals = []
            lagrange_intervals = lagrange(f)

            np, nn = f.get_descartes()
            if(nn != [0]):
                descartes_intervals += [lagrange_intervals[0]]
            if(np != [0]):
                descartes_intervals += [lagrange_intervals[1]]
            current_intervals = [i for i in descartes_intervals if(i[0] < i[1])]

            if (current_intervals == []):
                break
            for i in current_intervals:
                interval = getValidInterval(f, i)
                if (interval == []):
                    interval = bissection(f, i, 1e-1)
                    if(interval != []):
                        interval = getValidInterval(f, interval)
                if(interval != []):
                    intervals_list += [interval]
        except:
            print("Algum engano ocorreu")

        if (intervals_list == []):
            break
        new_roots = []
        for i in intervals_list:
            a, b = i
            bissection_list = full_bissection(f, a, b, 1e-3)
            if (bissection_list == [] or bissection_list == None):
                pass
            print("O pré-refinamento com método da Bisseção foi realizado com sucesso")
            newton_interval = [bissection_list[-1][0], bissection_list[-1][1]]
            try:
                x_0 = choose_x0(f, newton_interval, 1e-4)
                newton_list += nr_method__(f, x_0, 10**-7)
                new_roots += [newton_list[-1][1]]
                
                print("O refinamento com método de Newton foi realizado com sucesso")
            except:
                print("Os requisitos para o refinamento com o método Newton não foram atendidos.")
                newton_list = []
                bissection_list += full_bissection(f, a, b, 10**-7)
                new_roots += [bissection_list[-1][2]]
                print("O refinamento com método da Bisseção foi realizado com sucesso")
            print_table_roots(bissection_list, newton_list)
        roots += new_roots
        for r in new_roots:
            #f = Expression(div(f.expr, (x - r))[0])
            func = div(f.expr, (x - r))[0]
            f = Expression(func)
    print("\nRaízes: ", roots)