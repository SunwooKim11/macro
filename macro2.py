import pyautogui as pag
import time

#pag.screenshot("images/GambleRoom2_Icon.png", region=(153, 349, 184, 20))

def eqr():

    discord = pag.locateCenterOnScreen("images/Discord_Icon.png")
    pag.moveTo(discord)  # discord 아이콘 위치
    pag.click()
    #time.sleep(5)

    gambleroom = pag.locateCenterOnScreen("images/GambleRoom2_Icon.png")
    pag.moveTo(gambleroom)  # 도박방 위치
    pag.click()
    time.sleep(1)

    pag.typewrite(["!", "e", "q", "r", "enter"])
    #time.sleep(1)

    chrome = pag.locateCenterOnScreen("images/Chrome_Icon.png")
    pag.moveTo(chrome)  # chrome 아이콘 위치
    pag.click()


eqr()
last_time = time.time()

while True:
    if last_time+65<time.time():
        eqr()
        last_time=time.time()
