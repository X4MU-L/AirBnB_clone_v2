# global variables
$data_test_root = '/data/web_static/releases/test/'
$data_shared_root = '/data/web_static/shared/'
$www_root = '/var/www/html/'

# apt update
exec { 'apt update':
    command => '/usr/bin/apt update -y',
}
exec { "mkdir ${data_test_root}":
    command => "/usr/bin/mkdir -p -m 0755 ${data_test_root}",
    onlyif  => ['/usr/bin/test ! -e /data/']
}
exec { "mkdir ${data_shared_root}":
    command => "/usr/bin/mkdir -p -m 0755 ${data_shared_root}",
    onlyif  => ['/usr/bin/test ! -e /data/']
}
exec { 'chown /data/':
    command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
}

# package resources
package { 'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt',
}

# server root files
file { "${www_root}index.html":
  ensure  => 'present',
  content => 'Hello World!\n',
  mode    =>  '0644',
  require => Package['nginx']
}

file { "${www_root}error404.html":
  ensure  => 'present',
  content => 'Ceci n\'est pas une page\n',
  mode    =>  '0644',
  require => Package['nginx']
}


file { '/data/web_static/current':
  ensure => link,
  target => $data_test_root,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   =>  '0777',
}
file { "${data_test_root}index.html":
  ensure  => 'present',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode    =>  '0755',
  content => 'this is a test page\n',
}
# server block
exec { 'server block config':
  command => '/bin/printf %s "server {
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
}" > /etc/nginx/sites-available/default',
}

# restart nginx service
service { 'nginx':
  ensure  => 'running',
  name    => 'nginx',
  require => [
    Exec['server block config'],
    Package['nginx']
    ]
}
