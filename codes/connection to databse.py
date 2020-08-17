import pymysql
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='idfproject-1.cncp58rbjwbv.ap-south-1.rds.amazonaws.com',database='idfproject',user='idf',password='idf12345')
if connection.is_connected():
    print("Connected to MySQL Server version ", connection.get_server_info())
    cursor = connection.cursor()
    first_name=input()
    keyword=input()
    cursor.execute('SELECT txt_name FROM USERS U INNER JOIN TEXT_FILES T ON U.user_id = T.user_id WHERE First_Name = %s AND  ( txt_keyword_1 = %s  ) ;',(first_name,keyword))
    record = cursor.fetchall()
    print(str(record[0][0]))

