import mysql.connector
########### Connecting to DB #########################
mysq_useranem = input('Enter mysql username : ')
mysql_password = input('Enter mysql password : ')

global dbconnector
dbconnector = mysql.connector.connect(host="127.0.0.1",
                                          user="%s" % mysq_useranem,
                                          password="%s" % mysql_password,
                                          )
global my_cursor
my_cursor = dbconnector.cursor()

############## building H_C data base ##################################

def HOME_CAR_creating():
    my_cursor.execute("CREATE DATABASE IF NO EXISTS H_C;")
def HOME_table_creating():
    my_cursor.execute("CREATE TABLE IF NOT EXISTS home_info (ID INTEGER AUTO_INCREMENT PRIMARY KEY ,"
                      "location VARCHAR(50),"
                      "rooms VARCHAR(50), "
                      "meterix VARCHAR(50), price VARCHAR(50)),"
                      "price VARCHAR(50);")

def CAR_table_creating():
    my_cursor.execute("CREATE TABLE IF NOT EXISTS home_info (ID INTEGER AUTO_INCREMENT PRIMARY KEY ,"
                      "model VARCHAR(50),"
                      "year_car VARCHAR (50)"
                      "color VARCHAR(50), "
                      "karkard VARCHAR(50),"
                      "price VARCHAR(50));")
dbconnector.commit()
my_cursor.close()
dbconnector.close()