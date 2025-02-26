""" Запуск приложений """
import os, requests
import subprocess
from time import sleep

# Установка переменной окружения DISPLAY
os.environ["DISPLAY"] = ":0"


while True:
    server_status = requests.get("http://tks1.local:8080/").status_code
    client_status = requests.get("http://tks1.local/").status_code
    
    if server_status == 200 and client_status == 200:
        print('ЗАПУСК - СТАТУС СЕРВЕРОВ: ', server_status, client_status)
        subprocess.run(["firefox-esr", "--kiosk", "http://tks1.local"])

    print('ОЖИДАНИЕ - СТАТУС СЕРВЕРОВ: ', server_status, client_status)
    sleep(10)

