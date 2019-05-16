import mysql.connector
import requests
import bs4
############ creating DB and table ###################
import DBConfig
DBConfig.HOME_DB_creating()
DBConfig.HOME_DB_table_creating()

############### Connecting to DB #####################

dbconnector = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      password="@Omid1377",
                                      database="HOME"
                                      )
my_cursor = dbconnector.cursor()
############### Connecting to site ###################
for page in range(50049):
    url = "https://www.ihome.ir/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A7%D9%85%D9%84%D8%A7%DA%A9/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86/%d/" % page
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    location     = soup.find('div', attrs={'class':'location'}).text.strip()
    building_age = soup.find('i', attrs={'class':'ihome-building-age'}).text.strip()
    rooms        = soup.find('i', attrs={'class':'ihome-bed'}).text.strip()
    meterix      = soup.find('i',attrs={'class':'ihome-arrows'}).text.strip()
    price        = soup.find('div', attrs={'class':'price','data-cur-area':'Sq. M.'}).text.strip()

############### insert datas to DB ###################
    my_cursor.execute("INSERT INTO home_info VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');") % (location, building_age, rooms, meterix, price)

dbconnector.commit()
dbconnector.close()
my_cursor.close()