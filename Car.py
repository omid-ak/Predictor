import mysql.connector
import requests
import bs4
########### creating DB and table #########
import DBConfig
DBConfig.CAR_DB_creating()
DBConfig.CAR_DB_table_creating()

############ Connecting to DB #############
dbconnector = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      password="@Omid1377",
                                      database="CAR"
                                      )
my_cursor = dbconnector.cursor()
########### Connecting to site ############
for page in range(291):
    url = "https://takhtegaz.com/car/sale?page=%i" % page
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
########### insert to DB #################
    for m in  soup.find_all('h3', attrs={"class":"card-main__title"}):
        temp = m.get_text().strip()
        year = temp[0:5]
        model = temp[5:len(temp)-11]
        for kc in soup.find_all('ul', attrs={"class":"specs hidden-md-down clearfix"}):
            templs = kc.get_text().strip().split()
            karkard  = templs[0]
            color = templs[3]
            for p in soup.find_all('div', attrs={"class":"card__price money-format"}):
                price = p.get_text().strip(" تومان")
                my_cursor.execute("INSERT INTO car_info VALUES(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');" % (model, year, color, karkard, price))
dbconnector.commit()
dbconnector.close()
my_cursor.close()
