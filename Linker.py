import os
import re
import time
import asyncio
import logging
import shutil
import webbrowser
import urllib.request
from CryptoCloud import CryptoCloudAPI
from pywebcopy import save_webpage, save_website
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, Unauthorized, RetryAfter
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Connection import Telegram_Token, api_key, shop_id, amount
from threading import Thread

cca = CryptoCloudAPI(api_key, shop_id)

# Установка логгера для aiogram
logging.basicConfig(level=logging.CRITICAL)

bot = Bot(token=Telegram_Token)
dp = Dispatcher(bot)
storage = MemoryStorage()
is_busy = {}
userslist = []

async def check_payment(invoice_id, user_id):
    timer = 0
    while is_busy[user_id]:
        await asyncio.sleep(30)
        data = cca.get_invoice(invoice_id)
        # data = {'status': 'success', 'status_invoice': 'paid'}
        # data = {'status': 'success', 'status_invoice': 'created'}
        if data['status'] == 'success' and data['status_invoice'] == 'paid':
            return True

        if timer >= 20:
            return False
        else:
            timer +=1
    return False

        
# Функция - Загрузчик сайта
async def downloading_process(message,argument):
    try:
        # Скачиваем сайт
        site_url = message.text
        site_name = site_url.split("//")[1].split("/")[0]
        site_folder = f"./{site_name}"
        if argument == 'create':
            save_website(site_url, site_folder, site_name, bypass_robots=True, debug=False, open_in_browser=False, delay=(2, 5), threaded=False)

            # Архивируем папку с сайтом
            shutil.make_archive(site_folder, 'zip', site_folder)

            # Удаляем папку с сайтом
            shutil.rmtree(site_folder)
        
        elif argument == 'send':

            # Отправляем архив пользователю
            with open(f"{site_folder}.zip", "rb") as f:
                await bot.send_document(chat_id=message.chat.id, document=f)
        
        elif argument == 'del':
            # Удаляем  архив
            os.remove(f"{site_folder}.zip")
        
        return(site_folder)

    except Exception as e:
        # Обрабатываем исключение
        logging.exception(e)
        return False

async def site_is_tilda(message):
    try:
        site_url = message.text
        response = urllib.request.urlopen(site_url)
        text = response.read().decode('utf-8')
        matches = re.findall(r'tilda', text)
        if 'tilda' in matches:
            return True
        else:
            return False
    except Exception as e:
        logging.exception(e)
        return False       

# Функция-обработчик для команды /start
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот для загрузки сайтов на Tilda, отправьте мне адрес сайта и я скачаю его для вас.")

# Функция-обработчик для любого текстового сообщения
@dp.message_handler()
async def handle_url(message: types.Message):
    user_id = message.from_user.id
    
    if user_id in userslist:
        await message.answer("Операция уже выполняется, подождите ответ, а затем попробуйте снова.")
        return
    username = message.from_user.username
    if username is None:
        await message.answer("Пожалуйста, укажите свой username в настройках Telegram и возвращайтесь ко мне.")
        return
    tempUrl = message.text
    if not tempUrl.lower().startswith("http"):
        await message.answer("Пожалуйста, отправьте мне адрес сайта в формате https://www.example.com/")
        return
    if not await site_is_tilda(message):
        await message.answer("Я умею работать только с сайтами на Tilda. Найдите другую ссылку.")
        return
    
    userslist.append(user_id)

    result = await downloading_process(message,'create')
    if result == False:
        await message.answer("Произошла ошибка загрузки, попробуйте еще раз.")
        return
    invoice = cca.create_invoice(shop_id, amount) #amount - сумма чека
    # invoice = {'status': 'success', 'pay_url': 'https://pay.cryptocloud.plus/D6MG8GBD', 'currency': 'USDT', 'invoice_id': 'D6MG8GBD', 'amount': 2.422481, 'amount_usd': 2.4224806201550386}
    url_req = invoice['pay_url']
    amount_req = invoice['amount']
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Оплатить", url=url_req))
    keyboard.add(InlineKeyboardButton('Отмена оплаты', callback_data='cancel_button'))
    await message.reply(f"Для получения результатов скачивания оплатите счет на {amount_req}$\n У вас есть 10 минут на оплату.", reply_markup = keyboard)

    invoice_id = invoice['invoice_id']
    is_busy[user_id] = True
    payment = await check_payment(invoice_id, user_id)
    if payment:
        await downloading_process(message,'send')
    await downloading_process(message,'del')
    userslist.remove(user_id)


@dp.callback_query_handler(lambda c: c.data == 'cancel_button') 
async def process_callback_payment_button(message: types.Message):
    user_id = message.from_user.id
    if user_id in is_busy and is_busy[user_id] == True:
        is_busy[user_id] = False


# Запуск бота
if __name__ == '__main__':
    print("Starting...")
    executor.start_polling(dp, skip_updates=True)