#!/usr/bin/env bash

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE ask;"
mysql -uroot -e "CREATE USER 'ask_user'@'localhost' IDENTIFIED BY 'pass123';"
mysql -uroot -e "GRANT ALL ON ask.* TO 'ask_user'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"