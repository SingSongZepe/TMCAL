import typing

from value.strings import *

def read_input() -> typing.List[int]:
    with open(input_file_path, 'r') as pf:
        values = pf.read().split()
    vs = []
    for value in values:
        vs.append(float(value))
    return vs
