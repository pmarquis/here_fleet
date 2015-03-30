Here fleet
==========
This is a demo application to display the real time data and history of here fleet.

Database
-------
### Pre-requisite ###
Postgres and Postgis should be installed. If not you can install it with apt: 
* sudo apt-get install postgresql-9.3					
* sudo apt-get install postgresql-9.3-postgis-2.1			

### Install
* To create the database, follow instructions in db/create_db.txt
* To create the tables and add some data:
~~~
python fill_fleet_positions.py
python fill_fleet_positions_by_day.py
~~~



Web service
-------
### Pre-requisite ###
Tornado and psycopg2 should be installed: 
* pip install tornado
* pip install psycopg2			

### Start server
~~~
python webservice/server.py
~~~
You can check if the server is started using this URL:
[http://127.0.0.1:8888](http://127.0.0.1:8888)

Web page
--------
You can visualize data on the web page here_fleet.html

You will find 2 functions:
* Display the real time positions.
* Display the routes of a vehicle between two dates.

The second function use a simplification of the polyline to limit the display.
Note that at the moment the data are a sample and there is no real time data.
