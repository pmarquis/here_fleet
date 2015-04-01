Here fleet
==========
This is a demo application to display the real time data and history of here fleet.

Pre-requisite
--------------------
### Database pre-requisite ###
Postgres and Postgis should be installed. If not you can install it with apt: 
* sudo apt-get install postgresql-9.3					
* sudo apt-get install postgresql-9.3-postgis-2.1

### Python pre-requisite ###
Tornado, psycopg2, nose, fabric should be installed: 
* pip install tornado
* pip install psycopg2
* pip install nose
* pip install fabric


Database
-------
### Install
* To create the database, follow instructions in db/create_db.txt
* To create the tables and add some data:
~~~
fab fill_database
~~~


Web service
-------
### Pre-requisite ###
Tornado and psycopg2 should be installed: 
* pip install tornado
* pip install psycopg2			

### Start server ###
~~~
fab start
~~~
You can also check if the server is started using this URL:
[http://127.0.0.1:8888](http://127.0.0.1:8888)

### Test the web service ###
You should have start the server from an other terminal
~~~
fab functional_tests
~~~

Web page
--------
You can visualize data on the web page web/here_fleet.html

You will find 2 functions:
* Display the real time positions.
* Display the routes of a vehicle between two dates.

The second function use a simplification of the polyline to avoid to display every points.
Note that at the moment the data are a sample and there is no real time data.
