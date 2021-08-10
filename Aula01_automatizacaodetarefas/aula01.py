import pyautogui as pya
import pyperclip as pc
import time

pya.PAUSE = 3
pya.hotkey("win","8")
pc.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pya.hotkey("Ctrl","v")
pya.press("enter")
time.sleep(5)

pya.click(x=545,y=403,clicks=2)
time.sleep(3)
pya.click(x=455,y=439)
pya.click(x=1713,y=223)
pya.click(x=1617,y=654)

