{% set id = grains['id'] %}

nginx:
  pkg.installed:
    - name: nginx


/etc/nginx/sites-enabled/default:
  file.managed:
    - contents: |
        server {
                listen 80 default_server;
                listen [::]:80 default_server;

                root /var/www/html;

                # Add index.php to the list if you are using PHP

                index {{ salt['pillar.get']('web_index', 'index.yaml index.html index.htm index.nginx-debian.html') }};

                server_name _;

                location / {
                        # First attempt to serve request as file, then
                        # as directory, then fall back to displaying a 404.
                        try_files $uri $uri/ =404;
                }
        }


/var/www/html/index.yaml:
  file.managed:
    - mode: 0444
    - contents: |
        host: {{ id  }}
        special message: {{ salt['pillar.get']('message', 'Keep Austin Weird')  }}


nginx - start:
  cmd.run:
    - name: nginx
    - unless:
      - curl localhost


nginx - restart:
  cmd.wait:
    - name: kill -HUP $( cat /var/run/nginx.pid )
    - watch:
      - /etc/nginx/sites-enabled/default



