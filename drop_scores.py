import pymysql

connection = pymysql.connect(host="localhost", user="root", passwd="", database="euros_quiz")

cursor = connection.cursor()

drop = "DROP TABLE Scores;"

cursor.execute(drop)

connection.close
