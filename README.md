# dedmoroz

## System requirements:
```
$ sudo apt-get install -y python  python3-dev  python3-setuptools python3-pip
$ sudo pip3 install virtualenv
$ sudo apt-get install -y graphviz libgraphviz-dev pkg-config libenchant1c2a
$ sudo apt-get install mysql-server mysql-client
$ sudo apt-get install libjpeg8-dev zlib1g-dev libfreetype6-dev
$ sudo apt-get install libmysqlclient-dev
```
## Install
```
$ mkdir dedmoroz
$ cd dedmoroz
$ git clone https://github.com/kairatomurbek2/dedmoroz.git
$ virtualenv --no-site-packages --distribute -p /usr/bin/python3 venv
$ source ./venv/bin/activate
$ pip install -r req.txt
$ cd web-application
$ ./manage.py makemigrations thumbnail
$ ./manage.py migrate
