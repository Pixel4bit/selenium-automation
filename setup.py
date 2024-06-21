import os

print('List of Programs')
print('1. Streamlit auto-restart')
print('2. BMKG Web Scrapping automation')
print('3. Whatsapp Messages Spam automation')
print('4. Exit')
print('======================================\n')

while True:
    choose = int(input("Pilih program yang ingin dijalankan:\n"))
    if choose == 1:
        print('\nPilihan 1:')
        print('1. Streamlit auto-restart')
        input('Press ENTER to start the program\n')
        os.system('python automation_streamlit_reboot.py')
        break
    elif choose == 2:
        print('\nPilihan 2:')
        print('BMKG Web Scrapping automation')
        input('Press ENTER to start the program\n')
        os.system('python automation_bmkg_scrapping.py')
        break
    elif choose == 3:
        print('\nPilihan 3:')
        print('Whatsapp Messages Spam automation')
        input('Press ENTER to start the program\n')
        os.system('python automation_whatsapp_spam.py')
        break
    elif choose == 4:
        print('\nPilihan 4:')
        print('Exit the programs')
        input('Press ENTER to exit')
    else:
        print('\nWrong input. Try again.\n')

os.system('taskkill -im msedge.exe -f -t')