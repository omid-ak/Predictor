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
for page in range(100):
    url = "https://bama.ir/car/all-brands/all-models/all-trims?page=%d" % (page)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    model   = soup.find('h2', attrs={"itemprop": "name"}).text.strip()
    color   = soup.find('span', attrs={"id":"ex-color"}).text.strip()
    karkard = soup.find('p',attrs={"class":"price hidden-xs"}).text.strip()
    price = soup.find('span',attrs={"itemprop":"price"}).text.strip()
########### insert to DB #################
    my_cursor.execute('INSERT INTO car_info VALUES (\'%s\', \'%s\', \'%s\', \'%s\');' % (model, color, karkard, price))

dbconnector.commit()
dbconnector.close()
my_cursor.close()