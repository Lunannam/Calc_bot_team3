from curses.ascii import isdigit
import logging
from tokenize import Token
from config import TOKEN
from math import *
from cmath import *

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CHOICE, R_NUMB, C_NUMB, CALC, MATH_OP = range(5)
# функция обратного вызова точки входа в разговор
def start(update, _):
    # Старт бота , запрос выбора числа
    update.message.reply_text(
        'Меня зовут Бот-счетовод. Давайте считать?\n '
        'Команда /exit, чтобы прекратить разговор.\n'
        'Выбери калькулятор: р - рациональные числа или к - комплексные числа ?')
    return CHOICE
def choice(update,_):
# обработка выбора калькулятора
# просим ввести ввести числа :
# if R (введи рац числа)
# if C (введи компл числа)
    text = update.message.text
    if text == 'р':
        logs.logger(' вычисления рациональных чисел')
        update.message.reply_text('Введите два числа через пробел: ')
    if text == 'к':
        logs.logger(' вычисления комплексных чисел ')
        update.message.reply_text('Введите значения a и b для a+bj\n',  
                                '(например: 3 4 8 2 -> 3+4j и 8+2о): ')
    else:
        logs.logger(f'Сделан неверный выбор - {text}. Повторный запрос. ', 'False')
        update.message.reply_text('некорректный ввод. повторите свой выбор ')
        return CHOICE
#   
def ratio(update,_):
    text = update.message.text
    items = text.split()
    if items == 2:
        x = float(items[1])
        y = float(items[2])
        logs.logger(f'Сделан неверный выбор - {text}. Повторный запрос. ', 'False')
        update.message.reply_text('некорректный ввод. повторите ')   
    return R_NUMB
# просим ввести числа  
# проверка на флоат

def compl(update,_):
    text = update.message.text.split(' ')
    items = text.split()
    logs.logger(f'пользователь ввел числа: {x},{y}')
     
    if items.isdigit() and items == 4:
            x = complex(items[1], items[2])
            y = complex(items[3], items[4])
            logs.logger(f'пользователь ввел xbckf: {x},{y}')
            update.message.reply_text('введите знак вычисления: + - / * ')  
    return C_NUMB
# просим ввести числа
# формируем компл числа
# просим ввести знак вычисления
global x
global y

def math_op():
    #global X
    #global Y
    text = update.message.text
    if '+'  in text:
        logs.logger(' вычисления рациональных чисел')
        update.message.reply_text(f'{x} + {y} = {x+y}: ')
    if '-'  in text:
        logs.logger(' вычисления рациональных чисел')
        update.message.reply_text(f'{x} - {y} = {x-y}: ')
    if '/'  in text:
        logs.logger(' вычисления рациональных чисел')
        update.message.reply_text(f'{x} / {y} = {x/y}: ')
    if '*'  in text:
        logs.logger(' вычисления рациональных чисел')
        update.message.reply_text(f'{x} * {y} = {x*y}: ')
    return RES

def exit(update, _):
    update.message.reply_text(
            'ну ты заходи , если что \n ')

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями 
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор CHOICE, R_NUMB, C_NUMB, CALC

        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={

            CHOICE: [MessageHandler(Filters.text, choice)], 
            R_NUMB: [MessageHandler(Filters.ratio, ratio)], 
            C_NUMB: [MessageHandler(Filters.compl, compl)],
            MATH_OP: [MessageHandler(Filters.math_op, math_op)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('exit', exit)])

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

