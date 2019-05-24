import mysql.connector
from sklearn import tree


############# car Prediction ########################

def car_predicting(model, color, year_car,karkerd):
    dbconnector_C = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          password="@Omid1377",
                                          database="H_C",
                                          table="car_info"
                                          )

    my_cursor_C = dbconnector_C.cursor()

    #TODO: predict cars
    X = []
    Y = [] #price of car


    dbconnector_C.commit()
    dbconnector_C.close()
    my_cursor_C.close()



############ Home Prediction ########################
def home_predicting(location, building_age, rooms, meterix):
    dbconnector_H = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          password="@Omid1377",
                                          database="H_C",
                                          table="home_info"
                                          )

    X = [location, building_age, rooms, meterix]
    Y = []#price of home

    my_cursor_H = dbconnector_H.cursor()

    #TODO: Predict Home



    dbconnector_H.commit()
    dbconnector_H.close()
    my_cursor_H.close()