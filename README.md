# Serveur HTTP Minimaliste avec Docker

Ce projet met en place un serveur HTTP simple en Python, exécuté dans un conteneur Docker. Il utilise uniquement les bibliothèques standard de Python.

# Structure du Projet

basic-docker-project/
├── app/
│   ├── server.py
├── Dockerfile
├── docker-compose.yml
└── README.md

# Installation et Exécution

1️ Exécution en Local (Sans Docker)

Si Docker n'est pas installé, tu peux exécuter le serveur directement avec Python :

cd app
python server.py

Le serveur s’exécutera sur http://localhost:8000/.

2️ Construction et Exécution avec Docker

. Construire l’image Docker

Avant d'exécuter le conteneur, construis l’image avec :

docker build -t my-http-server .

. Exécuter le conteneur Docker

Après la construction, exécute l’application avec :

docker run -p 8000:8000 my-http-server

Accède au serveur via http://localhost:8000/.

3️ Exécution avec Docker Compose

Si tu préfères utiliser Docker Compose, lance le projet avec :

docker-compose up -d

L’application sera accessible sur http://localhost:8000/.Pour arrêter les conteneurs :

docker-compose down

. Pousser l’Image sur DockerHub

Se connecter à DockerHubConnecte-toi à DockerHub via la ligne de commande :

docker login

Taguer l’image avant de la pousserRemplace mmdiallo4839 par ton nom d’utilisateur DockerHub :

docker tag my-http-server mmdiallo4839/my-http-server:v1.0

Pousser l’image sur DockerHub

docker push mmdiallo4839/my-http-server:v1.0

Récupérer et exécuter l’image depuis DockerHub

docker pull mmdiallo4839/my-http-server:v1.0
docker run -p 8000:8000 mmdiallo4839/my-http-server:v1.0

. Développement et Personnalisation

Modifier le serveur : édite app/server.py.

Changer le port : modifie server.py et docker-compose.yml.

Ajouter des fonctionnalités : étends la classe SimpleHandler.

. Remarque

Assure-toi d’avoir Docker et Docker Compose installés.

Le serveur s’exécute sur le port 8000.

La documentation est claire et reproductible.