import asyncio
import time
import psutil

import requests
from aiogram import Bot, types, Dispatcher
# from aiogram.utils import executor
from bs4 import BeautifulSoup
# '1794340301:AAHzJg9XNv8iQ7_VXuV9DmodsnivyJkM6Pw'
API_TOKEN = '5419808022:AAHllPCwbi4QgWTFUX-BQWSIgYzD6fcuHqI'
CHANNEL_ID = '-1001770843028'

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# def cpu_temperature():
#     return psutil.sensors_temperatures()['cpu-thermal'][0].current
#
# def disk_space():
#     st = psutil.disk_usage(".")
#     return st.free, st.total
#
# def cpu_load() -> int:
#     return int(psutil.cpu_percent())
#
# def ram_usage() -> int:
#     return int(psutil.virtual_memory().percent)

def pars(url):
    response1 = requests.get(url)
    response2 = requests.get(url + "?embed=1&mode=tme")
    soup_txt = BeautifulSoup(response1.text, 'lxml')
    soup_file = BeautifulSoup(response2.text, 'lxml')
    txt = soup_txt.find("meta", property="og:description")
    try:
        file = soup_file.find("video").get('src')
        return txt["content"], file, "vid"
    except Exception:
        try:
            file = soup_file.find('a', "tgme_widget_message_photo_wrap").get("style").split("'")[1]
            return txt["content"], file, "img"
        except Exception:
            return txt["content"], None, None

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['info'])
async def inform(msg: types.Message):
    await bot.send_message(msg.from_user.id, "lox")


last_lepa = 2090
url_lepa = "https://t.me/lepatg/"

last_fourch = 11482
url_fourch = "https://t.me/why4channel/"

last_a = 4195
url_a = "https://t.me/conhum/"


while True:
    ur_lepa = url_lepa + str(last_lepa + 1)
    ur_fourch = url_fourch + str(last_fourch + 1)
    ur_a = url_a + str(last_a + 1)
    async def main():
        global last_lepa, last_fourch, last_a

        txt, file, typee = pars(ur_lepa)
        if '@newpostkostibot' not in txt and 'https' not in txt and 'подпи' not in txt and 't.me' not in txt:
            if typee == "vid":
                await bot.send_video(CHANNEL_ID, video=file, caption="#новости \n\n" + txt.replace('@lepatg', '@inoshapotyan'))
            elif typee == "img":
                await bot.send_photo(CHANNEL_ID, photo=file, caption="#новости \n\n" + txt.replace('@lepatg', '@inoshapotyan'))
            else:
                await bot.send_message(CHANNEL_ID, "#новости \n\n" + txt.replace('@lepatg', '@inoshapotyan'))
            last_lepa += 1

        txt, file, typee = pars(ur_fourch)
        if 'ttcreator.net' not in txt and 'https' not in txt and 'подпи' not in txt and 't.me' not in txt:
            if typee == "vid":
                await bot.send_video(CHANNEL_ID, video=file, caption="#юмор \n\n" + txt.replace('why4channel 🌈', '@inoshapotyan'))
            elif typee == "img":
                await bot.send_photo(CHANNEL_ID, photo=file, caption="#юмор \n\n" + txt.replace('why4channel 🌈', '@inoshapotyan'))
            else:
                await bot.send_message(CHANNEL_ID, "#юмор \n\n" + txt.replace('why4channel 🌈', '@inoshapotyan'))
            last_fourch += 1

        txt, file, typee = pars(ur_a)
        if '@conhum_bot' not in txt and 'https' not in txt and 'подпи' not in txt and 't.me' not in txt:
            if typee == "vid":
                await bot.send_video(CHANNEL_ID, video=file, caption="#it_юмор \n\n" + txt +'\n' + '@inoshapotyan')
            elif typee == "img":
                await bot.send_photo(CHANNEL_ID, photo=file, caption="#it_юмор \n\n" + txt +'\n' + '@inoshapotyan')
            else:
                await bot.send_message(CHANNEL_ID, "#юмор \n\n" + txt +'\n' + '@inoshapotyan')
            last_a += 1



    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # executor.start_polling(dp)
    # executor.close()
    time.sleep(3600)


