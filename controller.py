from bissection import *
from lagrange import *
from newton import *
from sympy import div
from sympy.abc import x
from expression import *
from utils import *

def deflate_equation(f: Expression, roots: list):
    for r in roots:
        # f = Expression(div(f.expr, (x - r))[0])
        func = div(f.expr, (x - r))[0]
        f = Expression(func)
    return f


def print_table_roots(bissection_table, newton_table):
    if bissection_table != []:
        print("\nBisseção: ")
        bissection_print(bissection_table)
    if newton_table != []:
        print("Newton: ")
        newton_print(newton_table)


def refinement_newton(f: Expression, interval: list, newton_table: list):
    root = 0.0
    x_0 = 0
    try:
        x_0 = choose_x0(f, interval, 10**-4)
        newton_table.extend(newton(f, x_0, 10**-7))
        root = newton_table[-1][1]
        return root
    except:
        return None


def refinement_bissection(f: Expression, interval: list, bissection_table: list, tolerance: float):
    try:
        bissection_table.extend(bissection(f, interval, tolerance))
        return get_last_root(bissection_table)
    except:
        return None
           

def prerefinement(f: Expression, interval: list, bissection_table: list, tolerance: float):
    try:
        bissection_table.extend(bissection(f, interval, tolerance))
        return get_last_interval(bissection_table)
    except:
        return None


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
            interval = f.bolzano(i)
            if interval == []:
                interval = search_valid_interval(f, i, 1e-1)
                if interval != []:
                    interval = f.bolzano(interval)
            if interval != []:
                intervals_list += [interval]
    except:
        return None
    if intervals_list == []:
        return None
    return intervals_list
