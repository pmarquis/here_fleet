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
fill_fleet_positions.py
fill_fleet_positions_by_day.py
~~~

