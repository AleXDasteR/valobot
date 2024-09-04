import pywebcopy
import asyncio


async def copylink(link):
    site_name = link.split('//')[1].split('/')[0]
    pywebcopy.save_website(url=link, project_folder=f"./{site_name}", project_name=site_name, debug=True,
                           bypass_robots=True,
                           threaded=False)

a = input('Введи первый адрес сайта:')
b = input('Введите второй адрес сайта:')


asyncio.run(copylink(a))
asyncio.run(copylink(b))
