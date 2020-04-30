# -*- coding: utf-8 -*-
from selenium import webdriver
import argparse
import datetime
import os


def take_screenshot(drive, protocol):
    try:
        driver = webdriver.PhantomJS(drive)  # создаем экземпляр вебдрайвера на phantomjs
        driver.get(protocol + args.source)  # передаем драйверу сайт, который надо бы скриншотнуть
        screen_name = "screenshot " + args.source + " " + datetime.datetime.today().strftime(
            "%Y-%m-%d-%H.%M.%S") + " .png"
        driver.save_screenshot(screen_name)  # сохраняем скриншот
        driver.quit()  # закрываем драйвер
        return screen_name
    except ConnectionError:  # ловим возможные ошибки
        print('Protocol error')


parser = argparse.ArgumentParser(description='Website to screenshot')  # создаем парсер
parser.add_argument('source', type=str, help='Input URL')  # добавляем аргумент для парсера
parser.add_argument('OS', type=str, help='Type your OS(win/mac/linux)')  # добавляем аргумент для парсера
args = parser.parse_args()  # парсим аргументы и получаем значение

if args.OS == 'win':
    DRIVER = '\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'  # указываем путь до phantomjs
elif args.OS == 'mac':
    DRIVER = '\\phantomjs-2.1.1-macosx\\bin\\phantomjs.dmg'  # указываем путь до phantomjs
else:
    DRIVER = '\\phantomjs-2.1.1-linux-x86_64\\bin\\phantomjs.bin'  # указываем путь до phantomjs

screen = take_screenshot(DRIVER, 'https://www.')  # получаем имя файла

if os.stat(screen).st_size < 700:  # проверяем размер файла
    os.remove(screen)   # удаляем пустой файл (566 байт)
    shot = take_screenshot(DRIVER, 'http://www.')  # пробуем другой протокол
    if os.stat(shot).st_size < 700:  # проверяем размер файла
        os.remove(shot)  # удаляем пустой файл (566 байт)
        print('Site not reachable')  # невозможно достичь сайта любым протоколом => URL неверен
    else:
        print('Done!')  # уведомляем пользователя о том, что программа завершила работу
else:
    print('Done!')  # уведомляем пользователя о том, что программа завершила работу
