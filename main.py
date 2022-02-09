from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
from PIL import Image, ImageGrab
from time import sleep

webdriver_url = "C:\chromedriver\chromedriver.exe"

service = Service(webdriver_url)
driver = webdriver.Chrome(service=service)
driver.get("https://chromedino.com/")

sleep(3)


def hit(key):
    pyautogui.press(key)
    return

def collison(data):
    for i in range(380, 420):
        for j in range(410, 450):
            if data[i, j] < 100:
                hit("Up")
                return

    for i in range(380, 420):
        for j in range(380, 400):
            if data[i, j] < 100:
                hit("Down")
                return

    return


hit("Up")

while True:
    img = ImageGrab.grab().convert("L")
    data = img.load()
    collison(data)



