# Projet Ananas ! [Work in progress]

Ce guide récapitule nos principales étapes.

## Se connecter depuis chez soi au gitlab de l'epf

Il faut tout d'abord installer git for windows (https://gitforwindows.org/). Une fois que c'est fait il faut lancer le git bash et taper ssh-keygen -t rsa -b 4096 -C "prenom.nom@epfedu.fr". Faire tout le temps entré quand on demande de remplir des champs.
Une fois que les clés sont générés, elles devraient apparaitre dans le dossier C:\Users\votreutilisateur\.ssh
Il faut ensuite ouvrir la clé publique (avec l'extension .pub) et copier son contenu.
Se rendre ensuite sur le gitlab de l'epf (https://gitlab.min.epf.fr/users/sign_in), se connecter, cliquer sur l'icone de notre avatar puis settings et enfin ssh keys. Copier la clé dans le champs dédié.
Ensuite dans le git bash on se rend la ou on veux faire le projet puis on fait:
- git init
- git config --local user.name prenom
- git config --local user.email prenom.nom@epfedu.fr
- git remote add origin ssh://git@gitlab.min.epf.fr:2217/ananas/projet-ananas.git

On fait nos modification en local puis une fois qu'on a fini:
- git add .
- git commit -m "votre message"
-git push origin nom_de_la_branche

Pour récupérer les modifications qu'on n'a pas en local:
- git fetch origin nom_de_la_branche
- git pull origin nom_de_la_branche (merge avec le depot local)

**A la place de faire le git init et tout ce qui suit on peut faire un git clone ssh://git@gitlab.min.epf.fr:2217/ananas/projet-ananas.git pour récupérer le projet distant**

## Intégration continue des fichiers sur le serveur

A chaque fois qu'un commit est effectué, le serveur pull les changements. 
Pour cela il faut créer des clés ssh sur le serveur et copier la clé public dans la section deploy key de gitlab. On fait un git clone puis on crée un fichier github-sync.py avec os.system('git pull') à l'intérieur (on peut également faire un bash).
Dans gitlab, dans la partie intégration on copie l'url d'accès à ce fichier et on coche:
- push event 
- merge request events 
- enable SSL verification.

## comment push sur le serveur de production

Pour cela il faut définir une autre url dans notre dépot local:
* git remote add production ssh://min@ananas.min.epf.fr:2248/home/min/ananas.min.epf.fr/projet-ananas.git

Maintenant un git push production master enverra toutes les modifications directement sur le serveur
Avant il faut bien sûr envoyer une clé public sur le server (la copier dans ~/.ssh/authorized_keys)

**Attention de ne pas push n'importe quoi sur le serveur de prod**

# La base de données
Il s'agit d'une base de données Mysql 

Afin de faire bien fonctionner l'application, il est impératif de créer un Tag.

text_tag = Tous les tags

type_tag = invisible