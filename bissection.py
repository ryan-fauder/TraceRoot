from Expression import Expression
from utils import getValidInterval

def bissection(f, interval, tolerance):
    a, b = interval
    mean = (a + b) / 2
    if (f.when(a) * f.when(b) < 0):
        return [a, b]
    if (abs(a - b) < tolerance):
        return []

    lista = bissection(f, [mean, b], tolerance)

    if lista == []:
        lista = bissection(f, [a, mean], tolerance)
    return lista


def full_bissection(f: Expression, interval: list, tolerance: float):
    bis_list = []
    bis_list += [[a, b, (a + b) / 2, f.when((a + b) / 2), abs(a - b)]]
    while bis_list[-1][4] > tolerance:
        if bis_list[-1][3] > 0: 
            a = bis_list[-1][2]
            b = bis_list[-1][1]
        else: 
            b = bis_list[-1][2]
            a = bis_list[-1][0]
        bis_list += [[a, b, (a + b) / 2, f.when((a + b) / 2), abs(a - b)]]
    return bis_list


def print_bissection_table(bis_list: list):
    print(' ' + '-' * 59)
    print(f'|{"a":^11}|{"x̄":^12}|{"b":^11}|{"f(x̄)":^12}|{"|a - b|":^11}|')
    print('|-----------|-----------|-----------|-----------|-----------|')
    for i in range(0, len(bis_list)):
        a, b, mean, f, abs_error = [float(v) for v in bis_list[i]]
        print(f'|{a:^11.5f}|{mean:^11.5f}|' + 
                f'{b:^11.5f}|{f:^11.5f}|{abs_error:^11.5f}|')

    print(' ' + '-' * 59)
