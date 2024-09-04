from aiogram import types, executor, Dispatcher, Bot
from pythonping import ping
import asyncio
import shutil
from pywebcopy import save_website
import os
from bs4 import BeautifulSoup as bs
import requests

TOKEN = 'token'
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


async def copy_website(url, folder, token):
    site_name = url.text.split("//")[1].split("/")[0]
    if token == 'create':
        save_website(
            url=url.text,
            project_folder=f"./{site_name}",
            project_name=site_name,
            bypass_robots=True,
            debug=True,
            open_in_browser=False,
            delay=(2, 5),
            threaded=False,
        )
        shutil.make_archive(site_name, 'zip', f"./{site_name}")
        print('Done')
    elif token == 'send':
        with open(f'./{site_name}.zip', 'rb') as f:
            await bot.send_document(chat_id=url.chat.id, document=f)
    elif token == 'delete':
        site_name = url.split("//")[1].split("/")[0]
        shutil.rmtree(folder)
        os.remove(f'C:/Users/Alexey/PycharmProjects/valobottelega/{site_name}.zip')
    return


def if_tilda(url):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    request = requests.get(url, headers=headers)
    soup = bs(request.text, 'html.parser')
    return len(soup.find_all('div', class_='t396')) > 1


async def delete_site(path):
    shutil.rmtree(path)
    return True


def check_size(name):
    return os.stat(f'C:/Users/Alexey/PycharmProjects/valobottelega/{name}.zip').st_size


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет, я тестовый бот')


@dp.message_handler(content_types=['text'])
async def link_copy(message: types.Message):
    try:
        site_name = message.text.split("//")[1].split("/")[0]
        if ping(site_name, count=1).success:
            if if_tilda(message.text):
                await copy_website(message,
                                   f'C:/Users/Alexey/PycharmProjects/valobottelega/{site_name}', 'create')
                await copy_website(message,
                                   f'C:/Users/Alexey/PycharmProjects/valobottelega/{site_name}', 'send')
                await copy_website(message,
                                   f'C:/Users/Alexey/PycharmProjects/valobottelega/{site_name}', 'delete')
            else:
                await bot.send_message(message.chat.id, 'Ваш сайт написан не на тильде!')
        await delete_site(f'C:/Users/Alexey/PycharmProjects/valobottelega/{site_name}')
    except RuntimeError:
        await bot.send_message(message.chat.id, 'Вы ввели неверный URL адрес!')


executor.start_polling(dp, skip_updates=True)
