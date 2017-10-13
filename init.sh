sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#sudo pip install --upgrade django; sudo pip install --upgrade gunicorn
sudo rm -r /etc/gunicorn.d/*
#sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf   /etc/gunicorn.d/gunicorn_ask.conf
sudo /etc/init.d/gunicorn restart
