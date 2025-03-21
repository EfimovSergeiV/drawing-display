import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
current_ip = s.getsockname()[0]
s.close()



with open ('./latest_ip.txt', 'r+') as file:
    latest_ip = file.readline()
    print(latest_ip)
    print("Последний IP: ", latest_ip, "Текущий IP: ", current_ip)

    if latest_ip != current_ip:
        file.seek(0)
        file.write(current_ip)
        file.truncate()
