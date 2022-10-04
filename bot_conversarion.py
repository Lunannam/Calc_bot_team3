import logging
from tokenize import Token
from config import TOKEN

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
CHOICE, R_NUMB, C_NUMB, CALC,RES = range(5)
# функция обратного вызова точки входа в разговор
def start(update, _):
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Меня зовут Бот-счетовод. Давайте считать?\n '
        'Команда /exit, чтобы прекратить разговор.\n'
        'Выбери калькулятор: R - рациональные числа или C - комплексные числа ?')
    return CHOICE
def choice(update,_)
# обработка выбора калькулятора
# просим ввести ввести числа :
# if R (введи рац числа)
# if C (введи компл числа)
    return  R_NUMB, C_NUMB
#   
def ratio(update,_)
# просим ввести числа  
# проверка на флоат
# просим ввести знак вычисления
    return CALC
def compl(update,_)
# просим ввести числа
# проверка на флоат
# просим ввести знак вычисления
    return CALC

def calc(update,_)
# обработка знака вычисления
# if + == sum res
# if - == minus res
# if * == mult res
# if / == div res
    return RES

def exit(update, _)
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

            CHOICE: [CommandHandler(Filters.), calc)], #надо заменить логируемые данные
            R_NUMB: [MessageHandler(Filters.photo, r_numb), #надо заменить логируемые данные
            C_NUMB: [
                MessageHandler(Filters.location, c_numb), #надо заменить логируемые данные
                CommandHandler('skip', skip_location),], #надо заменить логируемые данные
            
            CALC: [MessageHandler(Filters.text?????, )], #надо заменить логируемые данные
            RES: [MessageHandler(Filters.text?????, )], #надо заменить логируемые данные
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('exit', exit)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

