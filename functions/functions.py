from input.selecting_parameters import *

def get_q_lambda(lambda_: float) -> float:
    return ((k+1) / 2) ** (1 / (k-1)) * lambda_ * (1 - (k-1) / (k+1) * lambda_ * lambda_) ** (1 / (k-1))
