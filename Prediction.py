import mysql.connector
import requests
import bs4



############# car Prediction ########################

def car_predicting():
    dbconnector_C = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          password="@Omid1377",
                                          database="CAR"
                                          )

    my_cursor_C = dbconnector_C.cursor()

    #TODO: predict cars



    dbconnector_C.commit()
    dbconnector_C.close()
    my_cursor_C.close()



############ Home Prediction ########################
def home_predicting():
    dbconnector_H = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          password="@Omid1377",
                                          database="HOME"
                                          )

    my_cursor_H = dbconnector_H.cursor()

    #TODO: Predict Home



    dbconnector_H.commit()
    dbconnector_H.close()
    my_cursor_H.close()