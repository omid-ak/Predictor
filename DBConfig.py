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
    my_cursor.execute("CREATE TABLE home_info (ID INTEGER AUTO_INCREAMENT PRIMARY KEY ,"
                      "location VARCHAR(50),"
                      "building_age VARCHAR(50), "
                      "rooms VARCHAR(50), "
                      "meterinx VARCHAR(50), price VARCHAR(50));")

def CAR_DB_creating():
    my_cursor.execute("CREATE DATABASE CAR;")
def CAR_DB_table_creating():
    my_cursor.execute("CREATE TABLE home_info (ID INTEGER AUTO_INCREAMENT PRIMARY KEY ,"
                      "model VARCHAR(50),"
                      "clor VARCHAR(50), "
                      "karkard VARCHAR(50),"
                      "price VARCHAR(50));")
dbconnector.commit()
my_cursor.close()
dbconnector.close()