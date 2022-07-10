from expression import Expression

# Bissection Method

def search_valid_interval(f: Expression, interval: list, tolerance: float):
    a, b = interval
    mean = (a + b) / 2
    if (f.when(a) * f.when(b) < 0):
        return [a, b]
    if (abs(a - b) < tolerance):
        return []
    new_interval = search_valid_interval(f, [mean, b], tolerance)
    if new_interval == []:
        new_interval = search_valid_interval(f, [a, mean], tolerance)
    return new_interval


def bissection(f: Expression, interval: list, tolerance: float):
    a, b = interval
    table = []
    table += [[a, b, (a + b) / 2, f.when((a + b) / 2), abs(a - b)]]
    while table[-1][4] > tolerance:
        if table[-1][3] > 0: 
            a = table[-1][2]
            b = table[-1][1]
        else: 
            b = table[-1][2]
            a = table[-1][0]
        table += [[a, b, (a + b) / 2, f.when((a + b) / 2), abs(a - b)]]
    return table


def bissection_print(table: list):
    print(' ' + '-' * 59)
    print(f'|{"a":^11}|{"x̄":^12}|{"b":^11}|{"f(x̄)":^12}|{"|a - b|":^11}|')
    print('|-----------|-----------|-----------|-----------|-----------|')
    for i in range(0, len(table)):
        a, b, mean, f, abs_error = [float(v) for v in table[i]]
        print(f'|{a:^11.5f}|{mean:^11.5f}|' + 
                f'{b:^11.5f}|{f:^11.5f}|{abs_error:^11.5f}|')

    print(' ' + '-' * 59)


def get_last_root(table: list):
    if (table != []):
        return table[-1][2]
    return None

def get_last_interval(table: list):
    if (table != []):
        return [table[-1][0], table[-1][1]]
    return None