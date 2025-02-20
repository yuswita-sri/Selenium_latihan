from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1️⃣ Buka browser dan akses halaman login
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# 2️⃣ Masukkan username
username_input = driver.find_element(By.ID, "username")  # Cari elemen input username
username_input.send_keys("student")  # Masukkan username

# 3️⃣ Masukkan password
password_input = driver.find_element(By.ID, "password")  
password_input.send_keys("Password123")  
# 4️⃣ Klik tombol login
login_button = driver.find_element(By.ID, "submit")  # Cari tombol login
login_button.click()  # Klik tombol login

# 5️⃣ Tunggu sebentar supaya hasil bisa terlihat
time.sleep(3)

# 6️⃣ Tutup browser
driver.quit()
