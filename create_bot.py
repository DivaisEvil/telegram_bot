from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage # Задаем место хранения введенных команд, оперативка

storage=MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)