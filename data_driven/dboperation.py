import mysql.connector

con=mysql.connector.connect(host="localhost",port="port=3306",user="root",passwd="root")
ur=con.cursor()
ur.execute()