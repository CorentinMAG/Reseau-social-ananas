# Projet Ananas ! [Work in progress]

Ce guide récapitule les principales étapes pour faire fonctionner le projet.

## Requirements

* base de données mysql / mariadb

## Mise en marche du projet

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
        root /home/YOUR_USER/Reseau-social-ananas; # on peut également faire un lien symbolique dans /var/www
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
* sudo certbot --nginx (pour obtenir un certificat let's encrypt)
* sudo systemctl reload nginx
* python manage.py collectstatic
* python manage.py makemigrations
* python manage.py migrate

---
**NOTE**

Il faut modifier le fichier settings.py
Ne pas oublier de rajouter son nom de domaine dans ALLOWED_HOSTS
et de modifier STATIC_ROOT (qui devrait pointer vers /home/YOUR_USER/Reseau-social-ananas/static)

---