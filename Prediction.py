import mysql.connector
import requests
import bs4


import Home
import Car

############# Connecting to DB ########################

dbconnector = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      password="@Omid1377",
                                      )

my_cursor = dbconnector.cursor()


dbconnector.commit()
dbconnector.close()
