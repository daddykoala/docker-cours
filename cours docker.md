# Note cours docker #

cmd pour lancer une image 

````
docker run [version de l'image] 
```` 
(possibilite d'aller chercher sur le docker hub des images preconstruites par les utilisateurs)


utiliser la console de notre image 
```
docker run -it [version de l'image]
```
 redaction d'un docker file 

 ````
 # ON UTILISE LE DOCKERFILE POUR CREER UNE IMAGE AVEC LES INSTRUCTIONS SUIVANTES
FROM node
# ON DEFINIT LE REPERTOIRE DE TRAVAIL
WORKDIR /app
# ON COPIE LE FICHIER PACKAGE.JSON DANS LE REPERTOIRE DE TRAVAIL
# le premier opoint est le chemin du fichier sur la machine locale et le deuxieme est le chemin du fichier dans le conteneur
COPY . /app
# ON INSTALLE LES DEPENDANCES               
RUN npm install
# ON EXPOSE LE PORT 80 POUR LE CONTENEUR PARCE QUE LE CONTENEUR EST UN SERVEUR WEB ET QUE ICI ON PARLE DU PORT 80 DE NOTRE CONTENEUR ET NON DE NOTRE MACHINE EN LOCAL
EXPOSE 80
# ON EXECUTE LA COMMANDE node server.js ?LA DIFFERENCE AVEC LA COMMANDE RUN EST QUE LA COMMANDE CMD EST EXECUTEE A LA CREATION DU CONTENEUR

CMD ["node","server.js"]
 ````

 cmd pour voir tout les containers en cours 

 `````
 docker ps 

 docker ps -a 
 pour voir l'historique

````

cmd pour etre en mode détaché du container (attaché par defaut)

````
docker run -p 3000:80 -d [id]
```

````
