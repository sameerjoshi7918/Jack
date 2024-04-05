import os
import pyautogui as pg

name_of_image=pg.prompt('Enter the name of the image file')


if os.path.exists(r'C:\Users\samee\Pictures\Camera Roll\{}.jpg'.format(name_of_image)):
    print('location found')
    a=r'C:\Users\samee\Pictures\Camera Roll\{}.jpg'.format(name_of_image)
    print(a)
else:
    print('location not found')
