import telebot
from telebot import types
import datetime
import psycopg2


def get_week_number():
    now = datetime.datetime.now()
    year_start = datetime.datetime(now.year, 1, 1)
    week_number = (now - year_start).days // 7 + 1
    return week_number

def get_schedule():
    week_number = get_week_number()
    if week_number % 2 == 0:
        # Четная неделя
        current_week = "Четная"
        next_week = "Нечетная"
        # Здесь можно добавить код для вывода расписания на четную неделю
        schedule = "Расписание на четную неделю"
    else:
        # Нечетная неделя
        current_week = "Нечетная"
        next_week = "Четная"
        # Здесь можно добавить код для вывода расписания на нечетную неделю
        schedule = "Расписание на нечетную неделю"
    return f"<b>Текущая неделя:</b> {current_week}\n\n<b>Следующая неделя:</b> {next_week}\n\n{schedule}"


token = "6022427458:AAFdbxi_QSgMzuYL1s-fS8_Sc2FY0Xr7_QE"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    murkup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Хочу')
    murkup.row(btn1)
    btn2 = types.KeyboardButton('/help')
    murkup.row(btn2)
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=murkup)

@bot.message_handler(commands=['help'])
def start_message(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='/Monday', callback_data='btn1')
    kb.row(btn1)
    btn2 = types.InlineKeyboardButton(text='/Tuesday', callback_data='btn2')
    kb.row(btn2)
    btn3 = types.InlineKeyboardButton(text='/Wednesday', callback_data='btn3')
    kb.row(btn3)
    btn4 = types.InlineKeyboardButton(text='/Thursday', callback_data='btn4')
    kb.row(btn4)
    btn5 = types.InlineKeyboardButton(text='/Friday', callback_data='btn5')
    kb.row(btn5)
    btn6 = types.InlineKeyboardButton(text='/Saturday', callback_data='btn6')
    kb.row(btn6)
    btn7 = types.InlineKeyboardButton(text='/week', callback_data='btn7')
    kb.row(btn7)
    btn8 = types.InlineKeyboardButton(text='/nextweek', callback_data='btn8')
    kb.row(btn8)
    bot.send_message(message.chat.id, 'Выберите на какой день либо неделю вы хотите получить расписание', reply_markup=kb)

@bot.callback_query_handler(func = lambda callback: callback.data)
def check_callback_data(callback):
    conn = psycopg2.connect(database="Raspisanie",
                            user="postgres",
                            password="grecha99",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM service.bot')
    rec = cursor.fetchall()
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id,f' {rec[0][2]}\n'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<b>{rec[0][3]}\n</b>'
                                                  f'{rec[0][4]}\n'
                                                  f'Практика (до 18 нед.) в 332а (ОП)\n'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<b>{rec[1][3]}\n</b>'
                                                  f'{rec[1][4]}\n'
                                                  f'Практика (до 16 нед.) в 404 (ОП)\n'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<b>{rec[2][3]}\n</b>'
                                                  f'{rec[2][4]}\n'
                                                  f'Практика (до 16 нед.) в спортзале (ОП)\n'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>', parse_mode='html')

    elif callback.data == 'btn2':
        bot.send_message(callback.message.chat.id,f' {rec[1][2]}\n'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<b>{rec[3][3]}\n</b>'
                                                  f'{rec[3][4]}\n'
                                                  f'Практика (до 16 нед.) в 314 (ОП)\n'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<b>{rec[3][3]}\n</b>'
                                                  f'{rec[3][4]}\n'
                                                  f'Лекция (до 16 нед.) в 514 (ОП)\n'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<b>{rec[8][3]}\n</b>'
                                                  f'{rec[8][4]}\n'
                                                  f'Лекция (до 18 нед.) в 227 (ОП)\n'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<b>{rec[2][3]}\n</b>'
                                                  f'{rec[2][4]}\n'
                                                  f'Практика (до 16 нед.) в спортзале (ОП)\n'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>', parse_mode='html')
    elif callback.data == 'btn3':
        bot.send_message(callback.message.chat.id,f' {rec[2][2]}\n'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<b>{rec[0][3]}\n</b>'
                                                  f'{rec[9][4]}\n'
                                                  f'Лекция (до 18 нед.) в 226 (ОП)\n'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<b>{rec[8][3]}\n</b>'
                                                  f'{rec[8][4]}\n'
                                                  f'Практика (до 18 нед.) в 318 (ОП)\n'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<b>{rec[4][3]}\n</b>'
                                                  f'{rec[4][4]}\n'
                                                  f'Практика (до 12 нед.) в 322 (ОП)\n'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<b>{rec[1][3]}\n</b>'
                                                  f'{rec[10][4]}\n'
                                                  f'Лаб. занятие(3-17 нед.) в 509 (ОП)', parse_mode='html')
    elif callback.data == 'btn4':
        bot.send_message(callback.message.chat.id,f'{rec[3][2]}\n'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<b>{rec[5][3]}\n</b>'
                                                  f'{rec[5][4]}\n'
                                                  f'Лаб. занятие (до 16 нед.) в ВЦ-302 (А)\n'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<b>{rec[7][3]}\n</b>'
                                                  f'{rec[7][4]}\n'
                                                  f'Лаб. занятие (до 16 нед.) в А-407 (А)\n'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>', parse_mode='html')
    elif callback.data == 'btn5':
        bot.send_message(callback.message.chat.id,f'{rec[4][2]}\n'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>', parse_mode='html')
    elif callback.data == 'btn6':
        bot.send_message(callback.message.chat.id,f'{rec[5][2]}\n'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>', parse_mode='html')

    elif callback.data == 'btn7':
        bot.send_message(callback.message.chat.id,f'<b>РАСПИСАНИЕ НА НЕДЕЛЮ</b>\n'
                                                  f'<b>{rec[0][2]}\n</b>'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<b>{rec[0][3]}\n</b>'
                                                  f'{rec[0][4]}\n'
                                                  f'Практика (до 18 нед.) в 332а (ОП)\n'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<b>{rec[1][3]}\n</b>'
                                                  f'{rec[1][4]}\n'
                                                  f'Практика (до 16 нед.) в 404 (ОП)\n'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<b>{rec[2][3]}\n</b>'
                                                  f'{rec[2][4]}\n'
                                                  f'Практика (до 16 нед.) в спортзале (ОП)\n'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<b>{rec[1][2]}\n</b>'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<b>{rec[3][3]}\n</b>'
                                                  f'{rec[3][4]}\n'
                                                  f'Практика (до 16 нед.) в 314 (ОП)\n'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<b>{rec[3][3]}\n</b>'
                                                  f'{rec[3][4]}\n'
                                                  f'Лекция (до 16 нед.) в 514 (ОП)\n'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<b>{rec[8][3]}\n</b>'
                                                  f'{rec[8][4]}\n'
                                                  f'Лекция (до 18 нед.) в 227 (ОП)\n'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<b>{rec[2][3]}\n</b>'
                                                  f'{rec[2][4]}\n'
                                                  f'Практика (до 16 нед.) в спортзале (ОП)\n'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<b>{rec[2][2]}\n</b>'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<b>{rec[0][3]}\n</b>'
                                                  f'{rec[9][4]}\n'
                                                  f'Лекция (до 18 нед.) в 226 (ОП)\n'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<b>{rec[8][3]}\n</b>'
                                                  f'{rec[8][4]}\n'
                                                  f'Практика (до 18 нед.) в 318 (ОП)\n'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<b>{rec[4][3]}\n</b>'
                                                  f'{rec[4][4]}\n'
                                                  f'Практика (до 12 нед.) в 322 (ОП)\n'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<b>{rec[1][3]}\n</b>'
                                                  f'{rec[10][4]}\n'
                                                  f'Лаб. занятие(3-17 нед.) в 509 (ОП)\n'
                                                  f'\n'
                                                  f'<b>{rec[3][2]}\n</b>'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<b>{rec[5][3]}\n</b>'
                                                  f'{rec[5][4]}\n'
                                                  f'Лаб. занятие (до 16 нед.) в ВЦ-302 (А)\n'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<b>{rec[7][3]}\n</b>'
                                                  f'{rec[7][4]}\n'
                                                  f'Лаб. занятие (до 16 нед.) в А-407 (А)\n'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<b>{rec[4][2]}\n</b>'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<b>{rec[5][2]}\n</b>'
                                                  f'<em>1. {rec[0][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>2. {rec[1][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>3. {rec[2][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>4. {rec[3][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>'
                                                  f'\n'
                                                  f'<em>5. {rec[4][1]}\n</em>'
                                                  f'<em>{rec[6][3]}\n</em>', parse_mode='html')

    elif callback.data == 'btn8':
        bot.send_message(callback.message.chat.id, 'Следующая неделя')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')
    else:
        bot.send_message(message.chat.id, f'Такой команды не существует, <b>пропишите /help</b>, чтобы вывести команды бота', parse_mode='html')



bot.polling(none_stop=True)