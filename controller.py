import calculator as calcul
import ui
import logs


def button_click():
    '''
    Функция запрашивает данные, решает и выводит
    '''
    name = ui.choice_calc('')
    if name == 1:
        first_r = ui.rational_number(1)
        sign = ui.operation(' ')
        second_r = ui.rational_number(2)
        second_mn = 0
        calcul.init_ratio(first_r, second_r)
    elif name == 2:
        first_r, first_mn = ui.complex_number(1)
        sign = ui.operation(' ')
        second_r, second_mn = ui.complex_number(2)
        calcul.init_compl(first_r, first_mn, second_r, second_mn)
    
    if sign == '+':
        result = calcul.sum()
    if sign == '-':
        result = calcul.sub()
    if sign == '*':
        result = calcul.mult()
    if sign == '/':
        result = calcul.div()
    if name == 1:
        result = round(result, 15)
    if result == False:
        result = 'Деление на 0 невозможно!'
        print(result)

    data_log = str(calcul.x) + ' ' + sign + ' ' + str(calcul.y)
    ui.output_result(data_log, result)
    logs.logger(data_log, result)