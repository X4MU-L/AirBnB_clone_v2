#!/usr/bin/env bash
# this script sets up a static page for a sever

PKG="nginx"
# check if nginx is installed
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $PKG |
	     grep "install ok installed")
if [ "$PKG_OK" = "" ];
then
    apt update -y > /dev/null 2>&1;
    apt install nginx -y > /dev/null 2>&1;
fi

# check if root /data directory is created
if [ ! -d /data ];
then
    # create /data directory and sub directories
    mkdir -p /data/web_static/releases/test/
    mkdir -p /data/web_static/shared/
    # link /data/web_static/current to /data/web_static/releases/test
      # like with nginx sites-enabled and sites-avaliable
    ln -sf /data/web_static/releases/test/ /data/web_static/current
fi

# create a test page to serve
echo "Hello Holberton!" > /data/web_static/releases/test/index.html

# change group and owner of /data/
chown -R ubuntu:ubuntu /data/

# create static pages for nginx root
echo "Hello World!" | tee /var/www/html/index.html > /dev/null 2>&1
echo "Ceci n'est pas une page" | tee /var/www/html/error404.html > /dev/null 2>&1

# create server block
echo "
 server {
        listen 80 default_server;
        listen [::]:80 default_server;

	add_header X-Served-By $HOSTNAME;
        root /var/www/html;

        index index.html index.htm;

        location ~* (/redirect_me|/redirect_me/)$ {
                return 301 www.google.com;
        }

        location / {
                # FIRST ATTEMPT TO SERVE REQUEST AS FILE, THEN
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }

        # location ^~ /redirect {
               # return 200 \"hello redirect\";
        # }

	location /hbnb_static {
		 alias /data/web_static/current;
		 try_files \$uri \$uri/ =404;
		 access_log /data/web_static/current/access_log;
	}

        error_page 404 /error404.html;

        location = /error404.html {
                 root /var/www/html;
                 internal;
        }
}
" > /etc/nginx/sites-available/default

# restart nginx
service nginx restart
