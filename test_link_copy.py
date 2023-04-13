from bs4 import BeautifulSoup as bs
from pywebcopy import save_website
import requests
import shutil
import os
import time


def copy_website(url, folder, name):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    request = requests.get(url, headers=headers)
    soup = bs(request.text, 'html.parser')
    if len(soup.find_all('div', class_='t396')) > 1:
        save_website(
            url=url,
            project_folder=folder,
            project_name=name,
            bypass_robots=True,
            debug=True,
            open_in_browser=False,
            delay=None,
            threaded=True,
        )
        shutil.make_archive('downloaded_site1', 'zip', 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/1',
                            'C:/Users/Alexey/PycharmProjects/valobottelega/icons/')
        time.sleep(0.5)
        return 'Копирование сайта прошло успешно!'


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


def check_size():
    time.sleep(2)
    return os.stat('C:/Users/Alexey/PycharmProjects/valobottelega/downloaded_site1.zip').st_size
