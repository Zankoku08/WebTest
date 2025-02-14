from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time

# Cấu hình WebDriver cho Chrome
driver = webdriver.Chrome()
driver.get("https://hoangtran99.is-a.dev/DoAn_Web1/")
time.sleep(5)  # Đợi trang tải

#Ấn vào nút bấm đăng nhập
button = driver.find_element(By.XPATH,"""/html/body/section/div[1]/div[2]/div[2]/div[1]/a""")
button.click()

# Đăng nhập

# User
driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[1]/form/div[1]/input""").send_keys("teocotom")

# Pass
driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[1]/form/div[2]/input""").send_keys("teocotom")

# Click đăng nhập
driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[1]/form/button""").click()
