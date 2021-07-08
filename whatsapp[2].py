import pyautogui as pt
from time import sleep
import pyperclip
import processing_message
poss=pt.locateOnScreen("whatsapp_icon.PNG", confidence= .6)
pt.click(poss[0]+20,poss[1]+20)
sleep(5)
position= pt.locateOnScreen("Capture.JPG", confidence= .6)
if position is not None:
    x, y = position[0], position[1]
else: x, y = 476, 659
def get_message():
    position = pt.locateOnScreen("Capture.JPG", confidence= .6)
    pt.moveTo(position[0]+80,position[1]-45)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,12)
    pt.click()
    msg = pyperclip.paste()
    return msg
def send_message(mess):
    position = pt.locateOnScreen("Capture.JPG", confidence=.6)
    pt.click(position[0]+200,position[1]+20)
    pt.typewrite(processing_message.message(mess))
    sleep(1)
    pt.typewrite('\n')
pt.click(x + 80, y - 40)
while True:
    pt.click(976, 620)
    sleep(2)
    if (pt.pixel(int(x + 80), int(y - 40)) == (255, 255, 255)): send_message(get_message())
    position = pt.locateOnScreen("green.PNG", confidence= .7)
    if position is not None:
        pt.click(position[0]-100,position[1])
        pt.moveTo(x + 80, y - 40)