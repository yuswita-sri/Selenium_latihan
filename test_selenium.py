from selenium import webdriver

#buka browser dengan chrome
driver = webdriver.Chrome()

#Buka Google
driver.get("https://www.google.com")

#cetak judul halaman
print("Judul Halaman:", driver.title)

#tutup browser
driver.quit()