from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton# ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('/ю', request_contact=True)
# b5 = KeyboardButton('/Ме', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)
# resize_keyboard=True размеры кнопок пропорциональны
# one_time_keyboard=True скрыть клаву после выбора

kb_client.add(b1).row(b2).add(b3)#.add(b4).insert(b5)
# add все кнопки ро очереди row все в одну строку insert попытаться виестить если есть место