from selenium import webdriver

from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.common.by import By
import time

import os

os.system(r'START /B "" "C:\Users\pianxd\Documents\Python\automation with selenium\msedge_automation.bat"')

print("PROGRAM IS RUNNING.. PLEASE WAIT..")
print("(1/4) Opening Edge..")

link = 'https://share.streamlit.io'

opt = EdgeOptions()
opt.use_chromium = True
opt.add_experimental_option("debuggerAddress", "localhost:6969")

edge_services = Service(r"C:\Users\pianxd\Documents\Python\automation with selenium\edgedriver\msedgedriver.exe")

driver = webdriver.Edge(service=edge_services, options=opt)

time.sleep(3)
print("(2/4) Accessing Streamlit..")
driver.get(link)
input('Silahkan login ke streamlit terlebih dahulu.. Jika sudah tekan ENTER untuk melanjutkan automation\n')
print('Melanjutkan proses automation..')


# RESTARTING LSTM-SKRIPSI
time.sleep(5)
print("(3/4) Restarting App LSTM-SKRIPSI..")
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/main/table/tbody/tr[1]/td[5]/button')
button.click()

time.sleep(1)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/ul/li[2]/button')
button.click()

time.sleep(1)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/button')
button.click()


## RESTARTING LSTM-RNN-PROJECTS
time.sleep(1)
print("(4/4) Restarting App LSTM-RNN..")
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/main/table/tbody/tr[2]/td[5]/button')
button.click()

time.sleep(1)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/ul/li[2]/button')
button.click()

time.sleep(1)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/button')
button.click()

print("\n\n\n\n\n\n\n\n\n\n=== Rebooting complete.. attempting to stop automation in 5 ===")

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

print("\n\n\n(7/7) Attempting to close ms edge in 3..")

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
    