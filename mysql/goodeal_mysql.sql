create database goodeal character set utf8;
create user 'djangouser' identified by 'manage';
grant all on goodeal.* to 'djangouser';