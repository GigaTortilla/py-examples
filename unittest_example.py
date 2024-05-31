def math_addition(number_1: float, number_2: float) -> float:
    '''
    Mathematische Addition
    number_1: Erste Zahl
    number_2: Zweite Zahl
    return: Addition der beiden Zahlen
    '''
    result = number_1 + number_2
    return result


def math_division(number_1: float, number_2: float) -> float:
    '''
    Mathematische Division
    number_1: Erste Zahl
    number_2: Zweite Zahl
    return: Subtraktion erste Zahl minus zweite Zahl
    '''
    if number_2 == 0:
        raise ValueError('you cannot divide by 0')
    
    result = number_1 / number_2
    return result
