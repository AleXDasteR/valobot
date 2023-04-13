from aiogram import types, executor, Dispatcher, Bot
from pythonping import ping
from test_link_copy import copy_website, if_tilda, delete_site, check_size
import asyncio

TOKEN = '6249542940:AAHXwe6eklIPc4dFnbPx2-Q8L5_bkZbkKYw'
bot = Bot(TOKEN, connections_limit=128)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет, я тестовый бот')


@dp.message_handler(content_types=['text'])
async def link_copy(message: types.Message):
    try:
        if ping(message.text, count=1).success:
            if if_tilda('https://' + message.text):
                await bot.send_message(message.chat.id,
                                       copy_website('https://' + message.text,
                                                    'C:/Users/Alexey/PycharmProjects/valobottelega/icons',
                                                    '1'))
                if check_size() < 10485760 * 2:
                    await message.reply_document(
                        open('C:\\Users\\Alexey\\PycharmProjects\\valobottelega\\downloaded_site1.zip',
                             'rb'))
                else:
                    await bot.send_message(message.chat.id, 'Архив с файлом весит больше разрешенного!')
            else:
                await bot.send_message(message.chat.id, 'Ваш сайт написан не на тильде!')
    except RuntimeError:
        await bot.send_message(message.chat.id, 'Вы ввели неверный URL адрес!')
    finally:
        await asyncio.sleep(1)
        #await delete_site('C:/Users/Alexey/PycharmProjects/valobottelega/icons/1')


executor.start_polling(dp, skip_updates=True)
