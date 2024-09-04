import asyncio

from bs4 import BeautifulSoup as bs
from pywebcopy import save_website
import requests
import shutil
import os


async def copy_website(url, folder, token):
    if token == 'create':
        site_name = url.split("//")[1].split("/")[0]
        save_website(
            url=url,
            project_folder=folder,
            project_name=site_name,
            bypass_robots=True,
            debug=True,
            open_in_browser=False,
            delay=(2, 5),
            threaded=True,
        )
        shutil.make_archive(site_name, 'zip', 'C:/Users/Alexey/PycharmProjects/valobottelega/')
    elif token == 'delete':
        site_name = url.split("//")[1].split("/")[0]
        shutil.rmtree(folder)
        os.remove(f'C:/Users/Alexey/PycharmProjects/valobottelega/{site_name}.zip')


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
