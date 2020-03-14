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

** A la place de faire le git init et tout ce qui suit on peut faire un git clone ssh://git@gitlab.min.epf.fr:2217/ananas/projet-ananas.git pour récupérer le projet distant **
