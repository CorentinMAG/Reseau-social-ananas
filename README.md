# Projet Ananas ! [Work in progress]

This file is a tutorial to set up the project.

## Requirements

* database mysql / mariadb
* memcached:11211
* redis:6379

## Set up

* git clone https://github.com/CorentinMAG/Reseau-social-ananas.git
* sudo apt update
* sudo apt upgrade
* sudo apt install python3-pip
* pip3 install virtualenvwrapper
* export WORKON_HOME=~/envs
* export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
* mkdir -p $WORKON_HOME
* source ~/.local/bin/virtualenvwrapper.sh
* mkvirtualenv ananasenv
* add2virtualenv Reseau-social-ananas
* cd Reseau-social-ananas
* pip install -r requirements.txt
* sudo apt install supervisor
* sudo vim /etc/supervisor/conf.d/ananas-daphne.conf

```bash
[program:ananas-daphne]
command=~/envs/ananasenv/bin/daphne -p 8080 ananas.asgi:application
user=YOUR_USER
autostart=true
autorestart=true
```
* sudo systemctl restart supervisor
* sudo supervisorctl start ananas-daphne
* sudo apt install nginx
* sudo apt-get install certbot python-certbot-nginx
* sudo vim /etc/nginx/default

```bash
upstream channels-backend {
        server localhost:8080;
}
server {
        server_name SERVER_NAME;

        # you can also create a symbolic link in /var/www
        root /home/YOUR_USER/Reseau-social-ananas; 
        location / {
                try_files $uri @proxy_to_app;
        }
        location @proxy_to_app {
                proxy_pass http://channels-backend;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";

                proxy_redirect off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Host $server_name;
        }
        location /static/ {
                alias /home/YOUR_USER/Reseau-social-ananas/static;
        }
}
```
* sudo certbot --nginx (to get a let's encrypt certificate)
* sudo systemctl reload nginx
* python manage.py collectstatic
* python manage.py makemigrations
* python manage.py migrate

---
**NOTE**

You have to modify the settings.py file  
* add your domain name in ALLOWED_HOST
* STATIC_ROOT must point to /home/YOUR_USER/Reseau-social-ananas/static
---