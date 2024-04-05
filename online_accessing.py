#control from other device using whatsapp

import time
import pyautogui as pg
from datetime import datetime
import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def check():
    time.sleep(3)
    if os.path.exists('images\online_access.png'):
        os.remove('images\online_access.png')
        im = pg.screenshot('images\online_access.png',region=(1107,838,716,65))
    else:
        im = pg.screenshot('images\online_access.png',region=(1107,838,716,65))#1107,838,716,65

    try:
        print('try strarted')
        query1=pytesseract.image_to_string(Image.open('images\online_access.png'))
        query=query1.split()
        print(query)
        for i in range(len(query)):
            if query[i]=='python' and query[i+1]=='start':
                print('started the main extracting program')
                titles=pg.getAllTitles()
                for i in range(len(titles)):
                    if titles[i]=='WhatsApp - Brave':
                        openit=titles[i]
                        pg.getWindowsWithTitle(openit)[0].minimize()
                        pg.getWindowsWithTitle(openit)[0].maximize()
                        break
                pg.moveTo(988,956)
                pg.write('PROGRAM IS STARTED')
                pg.press('enter')
                kd.wait('`')
                print('program ended')
            else:
                print('not started after scrapping')
                check()
    except:
        print('check started from except')
        check()
    check()
check()

