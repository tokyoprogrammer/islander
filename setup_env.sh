#!/usr/bin/bash
sudo yum -y update
sudo yum -y install yum-utils
sudo yum -y groupinstall development
sudo yum -y install setuptool
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install python36u

sudo yum --enablerepo=extras -y install epel-release
sudo yum install -y python-pip

sudo pip install --upgrade setuptools --user python
sudo pip install --upgrade pip
sudo pip install -r requirements.txt

sudo pip install pipenv
pipenv --python 3.6
pipenv install
