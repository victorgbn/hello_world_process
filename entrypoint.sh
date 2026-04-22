#!/bin/bash

# Remplacer la variable d'environnement firstname dans index.html
sed -i "s/{firstname}/${FIRSTNAME:-World}/g" /usr/share/nginx/html/index.html

# Démarrer nginx
nginx -g "daemon off;"
