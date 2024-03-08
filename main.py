import typing
import math

from utils.read_input import read_input
from utils.print_input import print_input

from input.selecting_parameters import *

def main():
    values = read_input()
    print_input(values)
    
    # 4
    u_cp1 = u_k1 * math.sqrt((1+o_d_bt1*o_d_bt1)/2)

    # 5
    H_th1 = o_H_th1 * u_cp1 * u_cp1

    # 6
    c_1a = o_c_1a * u_cp1
    ctgalpha_1 = (2 * (1-rho_k1) - o_H_th1) / 2 / o_c_1a
    
    





if __name__ == '__main__':
    main()
