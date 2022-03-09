from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_button2= KeyboardButton('/start')
button_help = KeyboardButton("/help")

keyboard_stat = ReplyKeyboardMarkup(resize_keyboard=True)


keyboard_stat.row(button_help, button_button2)
