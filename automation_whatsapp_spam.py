from selenium import webdriver

from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.common.by import By
import time

import os

os.system(r'START /B "" "C:\Users\pianxd\Documents\Python\automation with selenium\msedge_automation.bat"')

print("PROGRAM IS RUNNING.. PLEASE WAIT..")
print("(1/5) Opening Edge..")

link = 'https://web.whatsapp.com/'

opt = EdgeOptions()
opt.use_chromium = True
opt.add_experimental_option("debuggerAddress", "localhost:6969")

edge_services = Service(r"C:\Users\pianxd\Documents\Python\automation with selenium\edgedriver\msedgedriver.exe")

driver = webdriver.Edge(service=edge_services, options=opt)

time.sleep(3)
print("(2/5) Mengkases Whatsapp..")
driver.get(link)

# PAUSE
input("Silahkan login terlebih dahulu.. Jika sudah login tekan ENTER\n")

print("\n\n\n\n\nMelanjutkan proses automation..")

## TARGET SPAM
time.sleep(1)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]/p')
button.click()
button.clear()

print('(3/5) Masukkan nama lengkap kontak yang ingin dispam..')
target = str(input('Nama lengkap kontak target yang ingin dispam: '))

button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(target)
input('Silahkan pilih chat target.. jika sudah tekan ENTER..\n')

# PESAN SPAM
time.sleep(1)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
button.click()

print('(4/5) Atur pesan yang ingin di spam..')
pesan = str(input("Masukkan pesan: "))

button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(pesan)

time.sleep(1)
print('(5/5) Atur jumlah pesan yang ingin dikirim..')
jumlah = int(input("Jumlah: "))
input('\nTekan ENTER untuk mengirim spam.')

for i in range(jumlah):
    print(f'{str(i+1)}/{str(jumlah)} Mengirim spam ke-{i+1}')
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(pesan)
    
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    button.click()    
print('SELESAI')

print("\n\n\n\n\n\n\n\n\n\n=== Spamming complete.. attempting to stop automation in 5 ===")

time.sleep(1)
print("5..")

time.sleep(1)
print("4..")

time.sleep(1)
print("3..")

time.sleep(1)
print("2..")

time.sleep(1)
print("1..")

## END THE AUTOMATION PROGRAM
time.sleep(1)
print("Stopping automation..")
driver.close()
driver.quit()
print('Automation has been stopped.')

print("\n\n\nAttempting to close ms edge in 3..")

time.sleep(1)
print("3..")

time.sleep(1)
print("2..")

time.sleep(1)
print("1..")

time.sleep(1)
print("Closing Edge..")
os.system("taskkill /im msedge.exe -f -t")

print('\nMs Edge has closed')
input('Program completed. You can close this program.\n')