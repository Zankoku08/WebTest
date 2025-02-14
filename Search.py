from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time

# Cấu hình WebDriver cho Chrome
driver = webdriver.Chrome()
driver.get("https://hoangtran99.is-a.dev/DoAn_Web1/")
time.sleep(5)  # Đợi trang tải

try:
    # Tim kiem san pham
    search = driver.find_element(By.ID,'search-box')
    search.send_keys('iphone')

    search.send_keys(Keys.ENTER)
            
except Exception as e:
        print("❌ Lỗi trong quá trình kiểm thử:", e)
    
finally:
        print("🛑 Đã kết thúc kiểm thử")

