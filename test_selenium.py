from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("Judul Halaman :", driver.title)

time.sleep(20)

driver.quit()