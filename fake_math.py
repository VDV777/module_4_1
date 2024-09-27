def divide(first: float, second: float) -> str:

    if second == 0:
        return 'Ошибка!'

    return (first / second).__str__()
