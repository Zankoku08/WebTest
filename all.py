from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert

import time

# Cấu hình WebDriver cho Chrome
driver = webdriver.Chrome()
driver.get("https://hoangtran99.is-a.dev/DoAn_Web1/")
time.sleep(3)  # Đợi trang tải

#Ấn vào nút bấm đăng nhập
button = driver.find_element(By.XPATH,"""/html/body/section/div[1]/div[2]/div[2]/div[1]/a""")
button.click()
time.sleep(3)

#Register
driver.find_element(By.XPATH,"""/html/body/div[2]/div/ul/li[2]/a""").click()
time.sleep(3)

driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/form/div[1]/div[1]/input""").send_keys("Teo")

driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/form/div[1]/div[2]/input""").send_keys("Ngo")

driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/form/div[2]/input""").send_keys("teo@gmail.com")

driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/form/div[3]/input""").send_keys("teocotom")

driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/form/div[4]/input""").send_keys("teocotom")

driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/form/button""").click()
alert = Alert(driver)

# Chấp nhận alert (bạn cũng có thể dùng alert.dismiss() để từ chối)
alert.accept()
time.sleep(3)
# Add product
driver.find_element(By.XPATH,"""/html/body/section/div[7]/div[3]/div/li[1]/a""").click()
time.sleep(3)

driver.find_element(By.XPATH,"""/html/body/section/div[3]/div[2]/div[2]/div[5]/a""").click()
time.sleep(3)

#Ấn vào nút bấm vao gio hang
driver.find_element(By.XPATH,"""/html/body/section/div[1]/div[2]/div[2]/div[2]""").click()
time.sleep(3)

#Thanh Toan
driver.find_element(By.XPATH,"""/html/body/section/table/tbody/tr[3]/td[3]""").click()










