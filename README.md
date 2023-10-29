# homebase
an little backend homework from homebase, details: https://docs.google.com/document/d/1OEMYkafhtKZjdH5sSVBPiE2sBoUFaj2_uFc_5LdSvow/

## Overview for this app

### A nodejs server, port 3000

with CRUD for the user model.
Database: sqlite

**APIs**:
- GET /users : list all users
- GET /users/<id> : list user by id
- DELETE /users/<id> : delete user by id
- POST /users : create a user
- PUT /users/<id>: update existing users


### Django server, port 8000
Database: sqlite (seperate from that of node js)
Have admin control for the product model. 

**Single API** (this fetches users from the Nodejs server via Flask proxy server):
- GET /v1/users : list all users
- GET /v1/users/<id>: list a user


### (API proxy) Flask, port 5001
Server as a proxy for django and node js servers

## Installation:
0. Make sure you have the latest stable versions of **python** + **nodejs** in your machine
1. Fetch this repo
2. Install python packages, ideally in a new **virtual enviroment**, with
```
 pip install -r requirements.txt
```
3. Run Django server (port 8000): open a terminal, cd to *django_server* directory and run:
```
python manage.py runserver
python manage.py migrate # migrations to sqlite db
```
4. Create an admin account to sign in to Django admin:
```
python manage.py createsuperuser
```

5. Run Flask server (port 5001): open a seperate terminal window/tab, cd to *proxy* directory and run:
```
python proxy.py
```
6. Run Node.js/Express server (port 3000): open a seperate terminal window/tab, cd to *express* directory and do the following:
```
# install dependecies
npm install

# then run server
npm start
```

## To do:
- Unittest for django and nodejs
- Error handling for django and node js

## Question to the engineers:
- Why doing this instead of using one backend?
