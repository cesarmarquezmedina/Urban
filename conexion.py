import mysql.connector

cnx = mysql.connector.connect(user='cesar', password='CESAR_2606952_*cmarquez',
                              host='127.0.0.1',
                              database='Urban',
                              port='3306')
cnx.ping(attempts=3, delay=0)
cnx.close()