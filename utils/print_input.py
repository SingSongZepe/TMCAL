import typing

def print_input(values: typing.List[float]):
    print('расход: ', values[0])
    print('степень повышения давления:', values[1])
    print('атмосферное давление:', values[2])
    print('атмосферная температура: ', values[3])
    print('коэффициент сохранения полного давления: ', values[4])
    print('КПД компрессора: ', values[5])
    