# Post installation instructions:
- Copy nginx configutation files from nginx-conf folder to their respecitve locations:
	- evolitve.conf ---> /etc/nginx/sites-available
		- create a symlink to site-enabled
	- both key and pem file to locations specified in the nginx-conf image.
		- create symlinks as specified in the image
		- you can rename the links in /etc/nginx, however you have to include new names in evolitve.conf
- Install uWSGI: pip install uwsgi
- Install MariaDB (MySQL) drivers for Django:
	- `sudo-apt get install libmariadbclient-dev`
	- `pip install django mysqlclient`

## How to run a server?

For now use the run-server.sh script in shared folder. Later on I will add instructions on how to run the server
as a deamon on startup.


---

# Credentials:
- user account:
	- admin:
		- username: admin
		- password: kriptogram
		- email: admin@evolitve.si
- database:
	- name: evolitve
	- username: evolitve
	- password: evolitve

