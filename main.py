import xml.etree.ElementTree as ET
import mysql.connector
mytree = ET.parse('sample.xml')
myroot= mytree.getroot()
for x in myroot:
    print(x.tag,x.text)

mysql=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="parsertest"
)

mycursor=mysql.cursor()
sql="INSERT INTO parsertest(ID,NAME,LINK,DOUBLESIZE,PURPLECOLOR,ICON) VALUES (%s,%s,%s,%s,%s,%s)"
val=(myroot[0].text,myroot[1].text,myroot[2].text,myroot[3].text,myroot[4].text,myroot[5].text)
mycursor.execute(sql,val)
mysql.commit();
print("data is saved")
