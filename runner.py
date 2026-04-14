""" Запуск приложений """
from server.main.conf import SERVER, CLIENT
import os, requests
import subprocess
from time import sleep

# Установка переменной окружения DISPLAY
os.environ["DISPLAY"] = ":0"


# Генерация конфигурационного файла для клиента
nuxt_config = {
  "name": "TKS-2",
  "urlBase": CLIENT,
  "apiBase": f"{SERVER}/",
  "socketBase": f"ws://{SERVER.split('://')[1]}/"
}

with open("./client/public/config.json", "w") as f:
    f.write(str(nuxt_config).replace("'", '"'))


while True:
    print('ПРОВЕРКА СТАТУСА СЕРВЕРОВ...')
    server_status = requests.get(SERVER).status_code
    client_status = requests.get(CLIENT).status_code

    if server_status == 200 and client_status == 200:
        print('ЗАПУСК - СТАТУС СЕРВЕРОВ: ', server_status, client_status)
        # subprocess.run(["firefox-esr", "--kiosk", CLIENT])
        subprocess.run(["firefox-esr", CLIENT])

    print('ОЖИДАНИЕ - СТАТУС СЕРВЕРОВ: ', server_status, client_status)
    sleep(10)

