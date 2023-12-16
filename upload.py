import time
import subprocess
import pyautogui
import pydirectinput
import os

pyautogui.FAILSAFE = False

subprocess.call(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe","/max"])
sb = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\searchbar.png")
pyautogui.moveTo(sb)
pyautogui.write('https://studio.youtube.com/channel/UCZTvVm7l7fbCG3ZPd89m9ww/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D')
pyautogui.press('enter')
time.sleep(2)

sf = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\select.png")
pyautogui.moveTo(sf)
pyautogui.click() 
time.sleep(2)

se = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\find.png")
pyautogui.write('out.mp4') 
time.sleep(5)

op = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\open.png")
pyautogui.moveTo(op)
pyautogui.click() 
time.sleep(3)

pyautogui.write('Tweetfactory🙌')
time.sleep(2)
pyautogui.scroll(-100)

no = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\no.png")
pyautogui.moveTo(no)
pyautogui.click() 
time.sleep(2)

next = pyautogui.locateCenterOnScreen("C:\\Users\\TJ\Documents\\pragyam\\py\\python\\twibot\\nxt.png")
pyautogui.moveTo(next)
pyautogui.click() 
time.sleep(2)

    