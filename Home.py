import mysql.connector
import requests
import bs4

############### Connecting to DB #####################

dbconnector = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      password="@Omid1377",
                                      )

my_cursor = dbconnector.cursor()
create_db_q = "CREATE DATABASE HOME;"
use_db = "USE HOME;"
my_cursor.execute(create_db_q)
my_cursor.execute(use_db)


dbconnector.commit()
dbconnector.close()
