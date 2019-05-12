import mysql.connector
########### Connecting to DB #########################
global dbconnector
dbconnector = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          password="@Omid1377",
                                          )
global my_cursor
my_cursor = dbconnector.cursor()

############## building HOME data base ##################################

def HOME_DB_creating():
    my_cursor.execute("CREATE DATABASE HOME;")

def HOME_DB_table_creating():
    my_cursor.execute("USE HOME;")
    my_cursor.execute("CREATE TABLE home_info (ID INTEGER AUTO_INCREAMENT PRIMARY KEY , year INTEGER(5), );")

def CAR_DB_creating():
    my_cursor.execute("CREATE DATABASE CAR;")
def CAR_DB_table_creating():
    my_cursor.execute("CREATE TABLE home_info (ID INTEGER AUTO_INCREAMENT PRIMARY KEY , );")
dbconnector.commit()
my_cursor.close()
dbconnector.close()