import telebot
from telebot import types
import sqlite3
from src import ui
from src import parser

bot = telebot.TeleBot('5200870392:AAEhHttXnxkLF2RXwPzdUWPCTjyFBPUi4yI')

keyboard = types.InlineKeyboardMarkup()
key_stud = types.InlineKeyboardButton(text='Студент 👨‍🎓', callback_data='student')
key_prev = types.InlineKeyboardButton(text='Преподователь 👨‍🏫', callback_data='prev')
keyboard.add(key_stud)
keyboard.add(key_prev)

conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(content_types=['text'])
def msg(message):
  bot.send_message(message.from_user.id,
                   f'👋 Привет {message.from_user.first_name}!\nЭтот бот поможет тебе с расписанием кооперативного техникума')
  bot.send_message(message.from_user.id, text='Кто вы?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_stud(call):
  if call.data == 'student':
    msg = 'Что ты хочешь узнать?'
    key_stud_rasp = types.InlineKeyboardButton(text='Получить расписание 📅', callback_data='rasp')
    key_stud_zvon = types.InlineKeyboardButton(text='Получить расписание звонков 🔔', callback_data='zvon')
    keyboard_stud = types.InlineKeyboardMarkup()
    keyboard_stud.add(key_stud_rasp)
    keyboard_stud.add(key_stud_zvon)
    bot.send_message(call.message.chat.id, msg, reply_markup=keyboard_stud)

  elif call.data == 'zvon':
    rasp_zvon = open('rasp.jpg', 'rb')
    key_prev_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data='back')
    keyboard_back = types.InlineKeyboardMarkup()
    keyboard_back.add(key_prev_back)
    bot.send_photo(call.message.chat.id, rasp_zvon, reply_markup=keyboard_back)

  elif call.data == 'prev' or call.data == 'back':
    msg = 'Что вы хотите узнать?'
    key_prev_rasp = types.InlineKeyboardButton(text='Получить расписание 📅', callback_data='rasp')
    key_prev_zvon = types.InlineKeyboardButton(text='Получить расписание звонков 🔔', callback_data='zvon')
    keyboard_prev = types.InlineKeyboardMarkup()
    keyboard_prev.add(key_prev_rasp)
    keyboard_prev.add(key_prev_zvon)
    bot.send_message(call.message.chat.id, msg, reply_markup=keyboard_prev)
ui.Menu()
bot.polling(none_stop=True, interval=0)