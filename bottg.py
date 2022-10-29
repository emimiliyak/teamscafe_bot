import sqlite3
from requests import get
import telebot
from telebot import types, TeleBot

img = open('kill.jpg', 'rb')
token = '5413781303:AAGl7yCM7_XTy7EI0VDtS5lm4q8aCTF-ZnY'

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)

bot: TeleBot = telebot.TeleBot('5413781303:AAGl7yCM7_XTy7EI0VDtS5lm4q8aCTF-ZnY')

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str) -> object:
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Заполнить анкету")
    btn2 = types.KeyboardButton("Ивенты")
    btn3 = types.KeyboardButton("Библиотека")
    btn4 = types.KeyboardButton("Правила")
    btn5 = types.KeyboardButton("Моя анкета")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Добро пожаловать в бота Team’s cafe.-Найти нового человека, чтобы выпить кружечку кофе на перерыве или работать вместе над проектом, на это способен этот бот. -Для начала работы просим ознакомиться с правилами и заполнить небольшое анкетирование.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message, markup=None):
    if message.text == "Ивенты":
        bot.send_message(message.chat.id, text="https://www.xn----7sbb3aiknder7bw.xn--p1ai/")
    elif message.text == "Заполнить анкету":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Мужчина")
        btn2 = types.KeyboardButton("Женщина")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Ваш пол?", reply_markup=markup)
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заполнить анкету")
        btn2 = types.KeyboardButton("Ивенты")
        btn3 = types.KeyboardButton("Библиотека")
        btn4 = types.KeyboardButton("Правила")
        btn5 = types.KeyboardButton("Моя анкета")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif message.text == "Библиотека":
        bot.send_message(message.chat.id, text="Здесь пока пусто")
    elif message.text == "Правила":
        bot.send_message(message.chat.id,
                         text="Правила о заполении анкеты:вносить только правдивые данные; отвечать на вопрос “четко и по делу”, без лишней воды; не использовать нецензурную лексику.")
    elif message.text == "Мужчина" or 'Женщина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Мужчину")
        btn2 = types.KeyboardButton("Женщину")
        btn3 = types.KeyboardButton("Не имеет значения")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Кого вы хотите найти?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Я вас не понимаю")


        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

def after_text_2(message):
    print('введённый пользователем номер телефона на шаге "В каком отделе вы работаете?":', message.text)


bot.polling(none_stop=True)
