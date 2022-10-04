def check_int_number(number: str) -> int:
    '''
    Поверка на целое число
    '''
    while True:
        try:
            return int(input(number))
        except ValueError:
            print('Ошибка! Должно быть целое число!')


def check_float_number(number: str) -> float:
    '''
    Поверка на дробное число
    '''
    while True:
        try:
            return float(input(number))
        except ValueError:
            print('Ошибка! Должно быть дробное число!')


def check_symbol(symbol: str) -> str:
    '''
    Поверка знака действия
    '''
    while True:
        try:
            sym = input(symbol)
            if sym == '+' or sym =='-' or sym =='*' or sym =='/':
                return sym
            else:
                print('Ошибка! Должен быть знак действия ("+", "-", "*", "/")!')
        except ValueError:
            print('Ошибка! Должен быть знак действия ("+", "-", "*", "/")!')


def check_calc(digit: str) -> int:
    '''
    Поверка выбора калькулятора
    '''
    while True:
        try:
            calc_choice = int(input(digit))
            if calc_choice == 1 or calc_choice == 2:
                return calc_choice
            else:
                print('Ошибка! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2')
        except ValueError:
            print('Ошибка! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2')