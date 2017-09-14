# Post installation instructions
- Copy nginx configutation files from nginx-conf folder to their respecitve locations:
	- evolitve.conf ---> /etc/nginx/sites-available
		- create a symlink to site-enabled
	- both key and pem file to locations specified in the nginx-conf image.
		- create symlinks as specified in the image
		- you can rename the links in /etc/nginx, however you have to include new names in evolitve.conf
- Install uWSGI: `pip install uwsgi`
- Install MariaDB (MySQL) drivers for Django:
	- `sudo-apt get install libmariadbclient-dev`
	- `pip install django mysqlclient`
	
## How to run the server?

For now use the run-server.sh script in shared folder. Later on I will add instructions on how to run the server
as a deamon on startup.

## How to access the site?

Nginx configuration file is set to listen on the evolitve.si domain name, however your computer will have to be configured to not go and search for this site on the internet. For this you will have to modify your hosts file. [Here](https://support.rackspace.com/how-to/modify-your-hosts-file/) you can find extended instructions for all operating systems.

Add the following lines to the hosts file:
```
192.168.8.10 evolitve.si
192.168.8.10 www.evolitve.si
```

Note that all requests to evolitve.si are going to be directed to the virtual machine, so you can't access the actual web page on the internet unless you change the hosts file.

---

# Credentials
#### User account:
- admin:
	- username: admin
	- password: kriptogram
	- email: admin@evolitve.si
#### Database:
- name: evolitve
- username: evolitve
- password: evolitve

