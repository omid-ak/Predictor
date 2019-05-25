import mysql.connector
from sklearn import tree


############# car Prediction ########################

def car_predicting(model, year_car, color,karkerd):
    dbconnector_C = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          password="@Omid1377",
                                          database="H_C",
                                          table="car_info"
                                          )


    my_cursor_C = dbconnector_C.cursor()

    
    X = []
    Y = [] #price of car

    my_cursor_C.execute("SELECT model, year_car, color, karkard FROM car_info;")
    res1 = my_cursor_C.fetchall()
    for row1 in res1:
        X.append(row1)
    my_cursor_C.execute("SELECT price FROM car_info;")
    res2 = my_cursor_C.fetchall()
    for row2 in res2:
        Y.append(row2)
    person1 = [[model, year_car, color, karkerd]]
    carpred = tree.DecisionTreeClassifier()
    carpred = carpred.fit(X, Y)
    answer1 = carpred.predict(person1)
    dbconnector_C.commit()
    dbconnector_C.close()
    my_cursor_C.close()
    return answer1

############ Home Prediction ########################
def home_predicting(location, rooms, meterix):
    dbconnector_H = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          password="@Omid1377",
                                          database="H_C",
                                          table="home_info"
                                          )
    my_cursor_H = dbconnector_H.cursor()

    X2 = [location, building_age, rooms, meterix]
    Y2 = []#price of home

    my_cursor_H.execute("SELECT location, rooms, meterix FROM home_info;")
    res3 = my_cursor_H.fetchall()
    for row3 in res3:
    	X2.append(row3)
    my_cursor_H.execute("SELECT price FROM home_info;")
    res4 = my_cursor_H.fetchall()
    for row4 in res43:
    	Y2.append(row4)
    person2 = [[location, rooms, meterix]]
    hompred = tree.DecisionTreeClassifier()
    hompred = hompred.fit(X2, Y2)
    answer2 = hompred.predict(person2)
    dbconnector_H.commit()
    dbconnector_H.close()
    my_cursor_H.close()
    return answer2