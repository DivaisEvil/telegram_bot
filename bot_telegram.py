import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os, json, string

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot)

async def on_startup(_):
    print('Bot started online')
# ++++++++++
# @dp.message_handler(commands=['start','help'])
# async def command_start(message : types.Message):
#     try:
#         await bot.send_message(message.from_user.id, 'Hi my freand')
#         await message.delete()
#     except:
#         await message.reply('Bot не добавлен, напишите ему')

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита')
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ем')

# @dp.message_handler()
# async def echo_send(message : types.Message):
#     # if message.text == 'Привет':
#     #
#     #     await message.answer('Привет Бро!')
#     # # await message.reply(message.text)
#     # # await bot.send_message(message.from_user.id, message.text)
#     if {i.lower().translate(str.maketrans('', '', string.punctuation))for i in message.text.split(' ')}\n
#     .intersection(set(json.load(open('cenz.json')))) != set():
#         await message.reply('не материться!')
#         await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
