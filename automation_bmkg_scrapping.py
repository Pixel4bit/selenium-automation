from selenium import webdriver

from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.common.by import By
import time

import os

os.system(r'START /B "" "C:\Users\pianxd\Documents\Python\automation with selenium\msedge_automation.bat"')

print("PROGRAM IS RUNNING.. PLEASE WAIT..")
print("(1/7) Opening Edge..")

link = 'https://dataonline.bmkg.go.id/home'

opt = EdgeOptions()
opt.use_chromium = True
opt.add_experimental_option("debuggerAddress", "localhost:6969")

edge_services = Service(r"C:\Users\pianxd\Documents\Python\automation with selenium\edgedriver\msedgedriver.exe")

driver = webdriver.Edge(service=edge_services, options=opt)

time.sleep(3)
print("(2/7) Mengkases BMKG..")
driver.get(link)

# PAUSE
input("Silahkan login terlebih dahulu.. Jika sudah login tekan ENTER\n")

print("\n\n\n\n\nMelanjutkan proses automation..")

## Kehalaman pengambilan data
time.sleep(1)
print("(3/7) Mengarahkan ke halaman pengambilan data..")
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/ul/li[3]/a')
button.click()

button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/ul/li[3]/ul/li[1]/a')
button.click()

## Proses scrapping data
time.sleep(3)
print("(4/7) Scrapping data..")
### Jenis Stasisun
print("(4.1/4.5) Scrapping jenis stasiun..")
button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div[1]/div[2]/div/div[2]/form/div[1]/span/span[1]/span/span[1]')
button.click()

button = driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')
button.click()

### Parameter
print("(4.2/4.5) Scrapping parameter dataset..")
button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[1]/input')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[3]/input')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[4]/input')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[5]/input')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[6]/input')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[7]/input')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[8]/input')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[9]/input')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/div/div[2]/div[10]/input')
button.click()

### Parameter propinsi
print("(4.3/4.5) Scrapping parameter propinsi..")
button = driver.find_element(By.XPATH, '//*[@id="select2-idrefprovince-container"]')
button.click()

button = driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[6]')
button.click()

### Parameter kabupaten
print("(4.4/4.5) Scrapping parameter kabupaten..")
button= driver.find_element(By.XPATH, '//*[@id="select2-idrefregency-container"]')
button.click()

button= driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[4]')
button.click()

### Nama Stasiun
print("(4.5/4.5) Scrapping parameter kabupaten..")
button= driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div[1]/div[2]/div/div[2]/form/div[5]/span/span[1]/span/span[1]')
button.click()

button = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys("k")

time.sleep(2)
button = driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')
button.click()


### Rentang Waktu
print("\n(5/7) Scrapping rentang data..")
from datetime import datetime, timedelta

# Tanggal mulai
tahun = int(input("Masukkan tahun awal: "))
print(f'Scrapping dari 01-01-{tahun} s.d 01-06-2024')

start_date = datetime(tahun, 1, 1)

# Tanggal saat ini
end_date = datetime(2024, 6, 1)

# Menghitung jumlah bulan
n_bulan = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month
print(f'Total bulan: {n_bulan} bulan\n')
print('Memulai proses scrapping...')


for i in range(n_bulan):
    time.sleep(3)
    
    iter_end_date = start_date + timedelta(days=31)
    iter_end_date = iter_end_date.replace(day=1)

    print(f'({str(i+1)}/{str(n_bulan)}) Scrapping data bulan ke-{str(i+1)}..')
    
    # Kirim tanggal mulai
    button = driver.find_element(By.XPATH, '//*[@id="from"]')
    button.clear()
    button.send_keys(start_date.strftime("%d-%m-%Y"))
    
    # Kirim tanggal saat ini
    button = driver.find_element(By.XPATH, '//*[@id="to"]')
    button.send_keys(iter_end_date.strftime("%d-%m-%Y"))
    
    button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/div/div[1]/div[2]/div/div[1]/span')
    button.click()    
    
    time.sleep(1)
    button= driver.find_element(By.XPATH, '//*[@id="form"]/div[7]/div/div/button')
    button.click()
    button= driver.find_element(By.XPATH, '//*[@id="form"]/div[7]/div/div/button')
    button.click()

    ### Rating
    time.sleep(2)
    button= driver.find_element(By.XPATH, '//*[@id="form-feedback"]/div[1]/div/div[1]/ul/a[3]')
    button.click()

    button= driver.find_element(By.XPATH, '//*[@id="form-feedback"]/div[2]/div/div[1]/ul/a[3]')
    button.click()

    button= driver.find_element(By.XPATH, '//*[@id="form-feedback"]/div[3]/div/div[1]/ul/a[3]')
    button.click()

    button= driver.find_element(By.XPATH, '//*[@id="form-feedback"]/div[4]/div/div[1]/ul/a[3]')
    button.click()

    
    ### Proses download
    button= driver.find_element(By.XPATH, '//*[@id="form-feedback"]/div[6]/div/button')
    button.click()
    button= driver.find_element(By.XPATH, '//*[@id="form-feedback"]/div[6]/div/button')
    button.click()

    time.sleep(1)
    button= driver.find_element(By.XPATH, '//*[@id="form-download"]/button[1]')
    button.click()
    
    
    ### Reset
    start_date = iter_end_date

print("\n\n\n\n(6/7) Proses Scrapping Data selesai.. attempting to stop automation in 5..")

time.sleep(1)
print('5..')

time.sleep(1)
print('4..')

time.sleep(1)
print('3..')

time.sleep(1)
print('2..')

time.sleep(1)
print('1..')

## END THE AUTOMATION PROGRAM
time.sleep(1)
print("Stopping automation..")
driver.close()
driver.quit()
print('Automation has been stopped.')

print("\n\n\n(7/7) Attempting to close ms edge in 3..")

time.sleep(1)
print('3..')

time.sleep(1)
print('2..')

time.sleep(1)
print('1..')

time.sleep(1)
print('Closing..')
os.system("taskkill /im msedge.exe -f -t")

print('\nMs Edge has closed.')
input('Program completed. You can close this program.\n')
