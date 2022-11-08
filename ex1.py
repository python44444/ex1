import webbrowser
import pyautogui
import pyperclip
import time
# GUIで
webbrowser.open_new_tab("https://www.google.com/")
time.sleep(1)
# left, top, width, height = pyautogui.locateOnScreen("google.png", confidence=0.1)
# pyautogui.click(left, top)
# pyautogui.click(382, 269)
pyperclip.copy("平泉町　観光")
pyautogui.hotkey("Ctrl", "v")
pyautogui.press("enter")
time.sleep(2)
pyautogui.screenshot("screenshot.png")

# セレニウム
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
# search_box = driver.find_element_by_name("q")
# search_box.send_keys("平泉")
# time.sleep(0.5)
# search_btn = driver.find_element_by_name("btnK")
# search_btn.click()
