# Note cours docker #

 ##cmd pour lancer une image 

````
docker run [version de l'image] 
```` 
(possibilite d'aller chercher sur le docker hub des images preconstruites par les utilisateurs)


## utiliser la console de notre image 
```
docker run -it [version de l'image]
```
## redaction d'un docker file # 

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

## cmd pour voir tout les containers en cours 

 ```
 docker ps 

 docker ps -a 
 pour voir l'historique

````

## cmd pour etre en mode détaché du container (attaché par defaut)

```
docker run -p 3000:80 -d [id]
```
## dockerfile avec volume 

````
FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

VOLUME [ "/app/feedback" ]

CMD [ "node", "server.js" ]
````
Pour persister les données dans notre conteneur nous devons créer un volume qui sera partagé entre notre conteneur et notre machine en local.
Important de nommer ce volume avec la même syntaxe pour conserver les données entre deux commande run 

## cmd pour nommer le volume 

 ````
 docker run -p 3000:80 --rm --name [nomdevotrechoix] -v [exactement le meme volume]:/app/feedback [container name]
 ````
Si le volume n'est pas nommé docker donnera un nom aleatoire et sera suprrimer a chaque
 --rm du container.

## Supprimer un volume anonyme

 ````
docker volume rm VOL_NAME
 ````
 or 

  ````
docker volume rm prune
 ````