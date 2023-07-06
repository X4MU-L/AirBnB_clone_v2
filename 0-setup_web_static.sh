#!/usr/bin/env bash
# This script sets up a server for deployment of a static website.

# update machine and install nginx
apt-get update -y > /dev/null 2>&1
if [ ! -e "/usr/sbin/nginx" ]; then
    apt-get install nginx -y > /dev/null 2>&1
fi

if [ ! -d /data ]; then
    mkdir -p /data/web_static/releases/test/
    mkdir -p /data/web_static/shared
    ln -fs /data/web_static/releases/test/ /data/web_static/current
fi

# create random page for test
echo "My Static Page" > /data/web_static/releases/test/index.html

chown -R ubuntu:ubuntu /data

# update default html file that comes with nginx
echo "Hello World!" | tee /var/www/html/index.html > /dev/null 2>&1
echo "Ceci n'est pas une page" | tee /var/www/html/error404.html > /dev/null 2>&1

# configure the server block
echo  "server {
       listen 80 default_server;
       listen [::]:80 default_server;

       add_header X-Served-By $HOSTNAME;

       root /var/www/html;
       index index.html index.htm;

       location /redirect_me {
       	     return 301 https://www.google.com;
       }

       location / {
             try_files \$uri \$uri/ =404;
       }

       location /hbnb_static {
       	     alias /data/web_static/current;
             try_files \$uri \$uri/ =404;
       }

       error_page 404 /error404.html;
       # disable error404.html page for external access
       location = /error404.html {
              root /var/www/html;
      	      internal;
       }
}" > /etc/nginx/sites-available/default

# restart nginx
service nginx restart
