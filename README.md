Крепление для мониторов DEXP Fence LDT63-C012GL
https://www.dns-shop.ru/product/68280fe7e455d6b2/kreplenie-dla-monitorov-dexp-fence-ldt63-c012gl/
3 499 ₽


===
Бюджетное решение (управление мышью)

Mini PC Intel Pentium
https://aliexpress.ru/item/1005003096277756.html?sku_id=12000029991121971&spm=a2g2w.productlist.search_results.8.10b816b24mXadi
8 170 ₽

27" Монитор Digma Progress 27P404F черный
https://www.dns-shop.ru/product/692f3f1cb12b4a84/27-monitor-digma-progress-27p404f-cernyj/
11 299 ₽

Мышь беспроводная Acer OMR010 черный
https://www.dns-shop.ru/product/4326c510ee853332/mys-besprovodnaa-acer-omr010--cernyj/
500 ₽

23470 ₽
===

===
Бюджетное решение (Сенсорное управление) (требует аккуратного обращения)

Mini PC Intel Pentium
https://aliexpress.ru/item/1005003096277756.html?sku_id=12000029991121971&spm=a2g2w.productlist.search_results.8.10b816b24mXadi
8 170 ₽

21.5" Монитор ASUS VT229H, 1920x1080, IPS, 1хHDMI
https://www.citilink.ru/product/monitor-asus-21-5-vt229h-chernyi-ips-16-9-hdmi-m-m-mat-250cd-touch-1363561/
27 890 ₽

39560 ₽
===

===
IFC-521WC - промышленный панельный компьютер 21.5"
https://www.rusavtomatika.com/ifc/IFC-521WC/
1700 usd === 170 670руб

174300 ₽
===



### Настройка ОС

```bash
# GNOME + GDM

# Для автоматического входа в GDM на Debian:
sudo nano /etc/gdm3/daemon.conf

# Найдите строку [daemon] и добавьте или измените следующие параметры:
AutomaticLoginEnable=true
AutomaticLogin=<your_username>

nano ~/.config/autostart/chrome-fullscreen.desktop

[Desktop Entry]
Type=Application
Exec=google-chrome --kiosk
Hidden=false
X-GNOME-Autostart-enabled=true
Name=Chrome Fullscreen
```






```bash
# LightDM и LXDE

sudo nano /etc/lightdm/lightdm.conf

# Найдите секцию [Seat:*] и добавьте или измените строки:
autologin-user=<your_username>
autologin-user-timeout=0

mkdir -p ~/.config/autostart
nano ~/.config/autostart/firefox-fullscreen.desktop

[Desktop Entry]
Type=Application
Exec=firefox --kiosk
Hidden=false
X-LXDE-Autostart-enabled=true
Name=Firefox Fullscreen


sudo nano /etc/default/grub

GRUB_DEFAULT=0
GRUB_TIMEOUT=0
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash loglevel=0"
GRUB_CMDLINE_LINUX=""

sudo update-grub
```

```bash
#Настроить безпарольный доступ для конкретной команды

sudo visudo
username ALL=(ALL) NOPASSWD: /usr/sbin/shutdown

```


```bash
# Настройка курсора в LXDE

sudo cat /usr/share/icons/default/index.theme
[Icon Theme]
Inherits=Adwaita

# Распаковываем курсоры
unzip DMZhaloA32.zip 
sudo mv DMZhaloA32 /usr/share/icons

sudo nano /usr/share/icons/default/index.theme
[Icon Theme]
Inherits=DMZhaloA32




```

```bash
# Управление треем LXDE
lxappearance

# Настройка hosts
sudo nano /etc/hosts


127.0.0.1       localhost
127.0.1.1       mon1
127.0.1.1       mon1.local

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

```



### Ошибки на промышленных ПК

```log
ACPI BIOS Error (bug): Could not resolve symbol [\_SB._OSC.CDW1].
AE_NOT_FOUND
ACPI Error: Aborting method \_SB._OSC due to previous error (AE_NOT_FOUND)
```

```bash
sudo nano /etc/default/grub

GRUB_DEFAULT=0
GRUB_TIMEOUT=0
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash loglevel=0"
GRUB_CMDLINE_LINUX=""

sudo update-grub
```


### NGINX конфиги

```bash
# Backend 
sudo nano /etc/nginx/sites-enabled/dapp

```

```text
server {
    listen 8080 default_server;
    listen [::]:8080 default_server;

    client_max_body_size 3G;

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000/;
    }

    location /static/ {
        alias /home/user/drawing-display/server/static/;
    }

    location /files/ {
        alias /home/user/drawing-display/server/files/;
    }

    location /ws/api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_read_timeout 60s;
        proxy_send_timeout 60s;
        proxy_connect_timeout 60s;

        proxy_buffering off;
    }

}


```

```bash
# Front 
sudo nano /etc/nginx/sites-enabled/napp

```

```text
map $sent_http_content_type $expires {
    "text/html"                 epoch;
    "text/html; charset=utf-8"  epoch;
    default                     off;
}

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    gzip            on;
    gzip_types      text/plain application/xml text/css application/javascript;
    gzip_min_length 1000;

    location / {
        expires $expires;

        proxy_redirect                      off;
        proxy_set_header Host               $host;
        proxy_set_header X-Real-IP          $remote_addr;
        proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto  $scheme;
        proxy_read_timeout          1m;
        proxy_connect_timeout       1m;
        proxy_pass                          http://localhost:3000/;
    }
}



```