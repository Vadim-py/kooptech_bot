import telebot
from telebot import types
from src import ui

bot = telebot.TeleBot('5200870392:AAEhHttXnxkLF2RXwPzdUWPCTjyFBPUi4yI')

keyboard = types.InlineKeyboardMarkup()


@bot.message_handler(content_types=['text'])
def msg(message):
  bot.send_message(message.from_user.id,
                   f'Привет {message.from_user.first_name}!\nЭтот бот поможет тебе с расписанием кооперативного техникума')
  key_stud = types.InlineKeyboardButton(text='Студент', callback_data='student')
  key_prev = types.InlineKeyboardButton(text='Преподователь', callback_data='prev')
  keyboard.add(key_stud)
  keyboard.add(key_prev)
  bot.send_message(message.from_user.id, text='Кто ты?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_stud(call):
  if call.data == 'student':
    msg = 'Что ты хочешь узнать?'
    key_stud_rasp = types.InlineKeyboardButton(text='Получить расписание', callback_data='rasp')
    keyboard.add(key_stud_rasp)
    bot.send_message(call.message.chat.id, msg, reply_markup=keyboard)

ui.Menu()
bot.polling(none_stop=True, interval=0)
