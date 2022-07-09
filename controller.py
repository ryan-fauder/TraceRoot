from bissection import *
from lagrange import *
from newton import *

def print_table_roots(bissection_list, newton_list):
    if(bissection_list != []):
        print("\nBisseção: ")
        print_bissection_table(bissection_list)
    if(newton_list != []):
        print("Newton: ")
        nr_method_print(newton_list)