from bissection import *
from lagrange import *
from newton import *
from sympy import solve, simplify
from sympy.abc import x
from Expression import *

def print_table_roots(bissection_list, newton_list):
    if bissection_list != []:
        print("\nBisseção: ")
        print_bissection_table(bissection_list)
    if newton_list != []:
        print("Newton: ")
        nr_method_print(newton_list)


def deflateEquation(f: Expression, roots: list):
    for r in roots:
        # f = Expression(div(f.expr, (x - r))[0])
        func = div(f.expr, (x - r))[0]
        f = Expression(func)
    return f


def refinement():
    pass


def prerefinement(f: Expression, i: list):
    a, b = i
    bissection_list = full_bissection(f, a, b, 1e-3)
    if bissection_list == [] or bissection_list == None:
        pass
    print("O pré-refinamento com método da Bisseção foi realizado com sucesso")
    return bissection_list


def get_intervals(f: Expression):
    try:
        lagrange_intervals = []
        descartes_intervals = []
        np, nn = 0, 0
        intervals = []
        lagrange_intervals = lagrange(f)

        np, nn = f.get_descartes()
        if nn != [0]:
            descartes_intervals += [lagrange_intervals[0]]
        if np != [0]:
            descartes_intervals += [lagrange_intervals[1]]
        intervals = [i for i in descartes_intervals if (i[0] < i[1])]
        return intervals
    except:
        return None


def filter_intervals(f: Expression, intervals: list):
    interval = ([],)
    intervals_list = []
    try:
        if intervals == []:
            return None
        for i in intervals:
            interval = getValidInterval(f, i)
            if interval == []:
                interval = bissection(f, i, 1e-1)
                if interval != []:
                    interval = getValidInterval(f, interval)
            if interval != []:
                intervals_list += [interval]
    except:
        print("Algum engano ocorreu")

    if intervals_list == []:
        return None
    return intervals_list


def filter_function():
    pass
