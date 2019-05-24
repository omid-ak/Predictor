import mysql.connector
import requests
import bs4
############ creating DB and table ###################
import DBConfig
DBConfig.HOME_CAR_creating()
DBConfig.HOME_table_creating()

############### Connecting to DB #####################

dbconnector = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      password="@Omid1377",
                                      database="H_C",
                                      table="home_info"
                                      )
my_cursor = dbconnector.cursor()
############### Connecting to site ###################
id = 0
id2 = 0
for page in range(50049):
    url = "https://www.ihome.ir/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A7%D9%85%D9%84%D8%A7%DA%A9/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86/%d/" % page
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
############### insert datas to DB ###################
    for l in soup.find_all('div', attrs={'class':'location'}):
        location = l.get_text().strip()
        my_cursor.execute("INSERT INTO home_info(location) VALUES (\'%s\');" % location)
    for rome in soup.find_all('ul', attrs={"class":"left slider_pinfo"}):
        id += 1
        templs = rome.get_text().strip().split()
        rooms = rome[0]
        meterix = rome[2]
        my_cursor.execute("UPDATE home_info SET rooms = \'%s\', meterix = \'%s\' WHERE ID = \'%d\';" % (rooms, meterix, id))
    for p in soup.find_all('div', attrs={'class':'price','data-cur-area':'Sq. M.'}):
        id2 += 1
        price = p.get_text().strip().strip('تومان')
        my_cursor.execute("UPDATE home_info SET price = \'%s\' WHERE ID = \'%d\';" % (price, id2))
dbconnector.commit()
dbconnector.close()
my_cursor.close()