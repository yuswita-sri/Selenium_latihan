from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#inisialisasi webdriver
driver = webdriver.Chrome()

#buka google
driver.get("https://www.google.com")

#cari elemen input (search box) dan ketikan kata kunci
search_box = driver.find_element(By.NAME, "q")  
search_box.send_keys("QA Automation dengan selenium")
search_box.send_keys(Keys.RETURN)

# Tunggu beberapa detik agar halaman hasil pencarian dimuat
time.sleep(10)

# Ambil judul dari hasil pencarian pertama
results = driver.find_elements(By.CSS_SELECTOR, "h3")
if results:
    print("Hasil pertama:", results[0].text)
else:
    print("Tidak ada hasil ditemukan.")

# Tutup browser
