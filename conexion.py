import mysql.connector

cnx = mysql.connector.connect(user='root', password='Contre_01rtorres*',
                              host='localhost',
                              database='Urban'
                              )
cnx.ping(attempts=3, delay=0)
cnx.close()