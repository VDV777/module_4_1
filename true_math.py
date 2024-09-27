from math import inf


def divide(first: float, second: float) -> str:
    if second == 0:
        return inf.__str__()

    return (first / second).__str__()
