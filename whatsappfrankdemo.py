import random
import pyautogui as pg
import time
comment=('Beautifull','looking Good','handsome','monkey','Lion',)
time.sleep(8)
for i in range(500):
    a=random.choice(comment)
    pg.write("you are a"+a)
    pg.press("enter")

