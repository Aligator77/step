sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#sudo pip install --upgrade django; sudo pip install --upgrade gunicorn
sudo rm -r /etc/gunicorn.d/*
#sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf   /etc/gunicorn.d/gunicorn_ask.conf
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start
echo 'if need create table press 1'
read create_db
if [ $create_db -eq 1] ; then
	#sudo rm -r /etc/mysql/my.cnf
	#sudo ln -sf /home/box/web/etc/my.cnf  /etc/mysql/my.cnf
	sudo /etc/init.d/mysql start

	mysql -uroot -e "CREATE DATABASE qa"
	mysql -uroot -e "CREATE USER 'qauser'@'localhost' IDENTIFIED BY 'qapass';
				 GRANT ALL ON qa.* TO 'qauser'@'localhost';"

	#sudo python /home/box/web/ask/manage.py syncdb
fi
