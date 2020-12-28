import pyautogui as pag
import time

def eqr():
    pag.moveTo(29, 441)  # discord 아이콘 위치
    pag.click()

    pag.moveTo(216, 421)  # 도박방1 위치
    pag.click()

    time.sleep(1)
    pag.typewrite(["!", "e", "q", "r", "enter"])

    pag.moveTo(40, 64)  # chrome 아이콘 위치
    pag.click()


eqr()
last_time = time.time()

while True:
    if last_time+60<time.time():
        eqr()
        last_time=time.time()