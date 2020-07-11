It's a Simple REST API to handle a Virtual Store

## This project was done with:

* Python 3.8.2
* Django 2.2.13

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

## How to execute

* create an `.env` file, use `.env.sample` as example  

### Run Tests:  
> docker-compose -f docker-compose-test.yml run --rm  web_test python manage.py test  

#### Run Application
> docker-compose up -d --build

#### Execute Migration
* creates a database with the same name as `SQL_DATABASE` in your `.env` file
 
> docker-compose exec web python manage.py makemigrations  
> docker-compose exec web python manage.py migrate

##### Create User
> docker-compose exec web python manage.py createsuperuser

##### Auth User
> curl -X POST -d "username=username&password=password" http://52.90.141.227:8000/login/

##### Refresh Token
> curl -X POST -H "Content-Type: application/json" -d '{"token":"<EXISTING_TOKEN>"}' http://52.90.141.227:8000/refresh-token/


##### API End-Points

> customers/  
> products/  
> orders/  

##### How to call endpoints with auth 

> curl -X <METHOD> -H "Authorization: JWT <EXISTING_TOKEN>" http://52.90.141.227:8000/<end-point>/

* see [docs](http://52.90.141.227:8000/docs/) to see available methods


## Api Documentation

[http://52.90.141.227:8000/docs/](http://52.90.141.227:8000/docs/)


* you need to be logged in to access all end points

## DEMO

[http://52.90.141.227:8000/](http://52.90.141.227:8000/)

user: demo  
pass: teste123
