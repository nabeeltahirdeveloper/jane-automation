import pyautogui
import time
import subprocess
import os


time.sleep(5)
while(True):
    if not pyautogui.locateOnScreen("check_image.png", confidence=0.9):
